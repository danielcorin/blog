---
title: "Tradeoffs of Using a Cache at Scale"
date: 2023-05-29T13:13:36-04:00
draft: false
tags:
- architecture
- caches
- scale

---

Imagine we have a query to our application that has become slow under load demands.
We have several options to remedy this issue.
If we settle on using a cache, consider the following failure domain when we design our architecture to determine whether using a cache actually is a good fit for our use case.

## Motivations for using a cache

When the cache is available and populated it will remove load from our database.
As a result, the responses for the query will likely be faster than it was when we were making it to the underlying database.
However, we should consider how our application will behave if our cache isn't available (either expired or the infrastructure is unstable).
A starting approach in code might look like this:

```python
response = cache.get("my_key")
if not response:
  response = db.query(...)
  cache.put("my_key", response, ttl=...)
return response
```

With this approach, we attempt to fetch the needed data from cache.
If the cache isn't available, we query the underlying database, store the response in cache, the return the response to the caller.
In a low-scale, this approach works fine.
We enjoy the performance gains from using the cache and occasional a caller incurs a latency hit if the cache is unpopulated or unavailable.
With a large number of callers this approach becomes risky, particularly if the underlying datastore cannot support the full request load without the protection of the cache.

## A problematic failure domain

Consider scenario where an application is receiving 4,000 requests per second (RPS) and a call to `db.query(...)` takes 2.5 seconds.
If our cache isn't available, we enter the `if` statement in the code above.
However, this code isn't running in isolation.
Over the next second, the application will receive an additional 3,999 identical or similar calls.
Since the call to the database takes 2.5 seconds, the cache `cache.get("my_key")` will still be unpopulated, thus, all 3,999 of those calls will also be routed to the datastore in an attempt to re-populate the cache.
With our cache unavailable, our datastore is now subjected to the full load of the application.
If the datastore cannot support that load, it will likely fail to respond to the first query, preventing re-population of the cache which could have protected it from the overwhelming 4,000 RPS.

## A possible solution

If we know our underlying datastore cannot support the full load of our application, we must decouple our application's request the from the underlying datastore.

```python
response = cache.get("my_key")
if not response:
  # return an empty response or raise an exception
  return []
return response
```

Separately, run a periodic cron (with frequency determined by our application's needs and `ttl`), to fetch the data from the underlying datastore and populate the cache.

```python
response = db.query(...)
cache.put("my_key", response)
```

If we run this cron once per 10 seconds, our database receives 0.1 RPS of load, and can continue to reliably serve fresh data from cache.

## Configuring the cron

We will want to run our cron frequently enough such that the cache does not expire due to its `ttl`.
We may even consider removing the `ttl` entirely.
If our cron stops running, it may lead the cache to expire.
Depending on our application, it may be better to serve stale data rather than no data at all.
If it's important for the data to be fresh, we can leave the `ttl` and allow the application to return an empty response when it fails to find a value in cache, continuing to shield the underlying datastore from the total load.
Lastly, we'll want to monitor our cron job to ensure it's running on its scheduled frequency.
If the cron stops running, we may return stale or no data depending on the approach we've selected above.

## (Re)evaluating the architecture

Given the constraints and opportunities for failure in using caches with high loads and sensitive datastores, we may reconsider whether we want to solve scaling our datastore with a cache.
It maybe worthwhile to load testing adding indices (if using SQL) or redesigning our table access patterns or creating new ones (if using NoSQL).
It's extra work to work through failure scenarios when building and scaling applications, but worth it when they behaves as you've planned during incidents.
