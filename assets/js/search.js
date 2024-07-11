// modeled off of https://victoria.dev/blog/add-search-to-hugo-static-sites-with-lunr/

function displayResults (results, store) {
  const searchResults = document.getElementById('search-results')
    if (results.length) {
      let resultList = ''
      // Iterate and build result list elements
      for (const n in results) {
        const item = store[results[n].ref]
        resultList += '<article class="post search-result"><div><a href="' + item.url + '">' + item.title + '</a></div>'
        if (item.date) {
            resultList += '<div class="search-result-date">' + item.date + '</div>'
        }
        resultList += '<div>' + item.content.substring(0, 150) + '...</div>'
        // Add tags to search results
        if (item.tags && item.tags.length > 0) {
            resultList += '<div class="search-tags"><ul class="tags">'
            item.tags.forEach(tag => {
                resultList += '<li class="' + "tag-" + tag + '"><a href="/tags/' + tag.toLowerCase() + '">' + tag + '</a></li>'
            })
            resultList += '</ul></div>'
        }
        resultList += '</article>'
      }
      searchResults.innerHTML = resultList
    } else {
      searchResults.innerHTML = 'No results found.'
    }
  }

  // Get the query parameter(s)
  const params = new URLSearchParams(window.location.search)
  const query = params.get('query')

  // Perform a search if there is a query
  if (query) {
    // Retain the search input in the form when displaying results
    document.getElementById('search-input').setAttribute('value', query)

    const idx = lunr(function () {
      this.ref('id')
      this.field('title', {
        boost: 15
      })
      this.field('tags')
      this.field('content', {
        boost: 10
      })

      for (const key in window.store) {
        this.add({
          id: key,
          title: window.store[key].title,
          tags: window.store[key].tags,
          content: window.store[key].content,
          date: window.store[key].date,
        })
      }
    })

    // Perform the search
    const results = idx.search(query)
    // Update the list with results
    displayResults(results, window.store)
  }
