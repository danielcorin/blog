---
draft: false
title: Observability
toc: true
---

## What you need to know
The fundamental units for metrics are that you need to count things and you need to know how long those things take.
These are counters and timers.
Metrics are useful to understand how your application is behaving in aggregate.

## Metrics vs logs

My preference is to rely largely on metrics to ensure my application is performing as expected.
Emitting metrics on success gives you confidence things are working.
Emitting metics on failure alerts you of problem areas.
In these examples, I would use [counters](https://prometheus.io/docs/concepts/metric_types/#counter).
I am not a fan of building metrics from logs and monitoring those because logs can change.
Logs from wellknown services (like Nginx or PostgreSQL) likely won't change often but logs in your service might.
Failing to get notified of an issue because a log statement was changed and your monitor didn't trigger is an unforced error.

## Warning/error logs vs error tracking tools

When things *do* go wrong, you'll want to see the stack trace.
Reading raw logs to diagnose issues isn't easy.
Even if you filter out certain levels, over time, applications can accumulate up a lot of log code and searching through all the logs becomes difficult.
Error tracking tools can help with this by grouping similar logs statements then aggregating them into categories to make it easier to figure out what errors are new and surface signal in the noise of logs.
Don't log ids in the message of the log.
Use structured logging or metadata to include ids in the log but not in the message, which may prevent similar logs from being aggregated.

Don't do this:

```python
logger.warn(f"login failed for user: {id}")
```

Do this:
```python
logger.warn("login failed", extra={"user_id": id})
```

## Emitting metrics from your application's layers
