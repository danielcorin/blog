// modeled off of https://victoria.dev/blog/add-search-to-hugo-static-sites-with-lunr/

function displayResults(results, store) {
  const searchResults = document.getElementById('search-results');

  if (results.length === 0) {
    searchResults.innerHTML = 'No results found.';
    return;
  }

  const resultList = results.map(result => {
    const item = store[result.ref];
    const highlightedTitle = highlightText(item.title, query);
    const contentSnippet = getContentSnippet(item.content, query);
    const highlightedContent = highlightText(contentSnippet, query); return `
      <article class="post search-result">
        <div><a href="${item.url}">${highlightedTitle}</a></div>
        ${item.date ? `<div class="search-result-date">${item.date}</div>` : ''}
        <div>${highlightedContent}</div>
        ${renderTags(item.tags)}
      </article>
    `;
  }).join('');

  searchResults.innerHTML = resultList;
}

function getContentSnippet(content, query) {
  const maxSnippetLength = 150;
  const words = query.split(/\s+/).filter(word => word.length > 0);
  const regex = new RegExp(words.join('|'), 'gi');
  const match = content.match(regex);

  if (match) {
    const firstMatchIndex = content.indexOf(match[0]);
    const startIndex = Math.max(0, content.lastIndexOf(' ', firstMatchIndex - 75));
    const endIndex = Math.min(
      content.length,
      content.indexOf(' ', firstMatchIndex + 75) !== -1 ?
        content.indexOf(' ', firstMatchIndex + 75) : content.length);
    let snippet = content.substring(startIndex, endIndex);

    // Trim the snippet and add ellipsis if necessary
    if (startIndex > 0) {
      snippet = '...' + snippet.trimStart();
    }
    if (endIndex < content.length) {
      snippet = snippet.trimEnd() + '...';
    }

    return snippet;
  }

  // At this point, we didn't find anything to highlight

  // If content is 150 characters or less, return it as is
  if (content.length <= maxSnippetLength) {
    return content;
  }

  // Otherwise, return the first 150 characters
  return content.substring(0, maxSnippetLength);
}

function highlightText(text, query) {
  const words = query.split(/\s+/).filter(word => word.length > 0);
  let highlightedText = text;
  words.forEach(word => {
    const regex = new RegExp(`\\b(${word})`, 'gi');
    highlightedText = highlightedText.replace(regex, '<span class="search-highlight">$1</span>');
  });
  return highlightedText;
}

function renderTags(tags) {
  if (!tags || tags.length === 0) return '<div class="search-tags" style="margin-bottom: 1em;"></div>';

  const tagList = tags.map(tag =>
    `<li class="tag-${tag}"><a href="/tags/${tag.toLowerCase()}">${tag}</a></li>`
  ).join('');

  return `<div class="search-tags"><ul class="tags">${tagList}</ul></div>`;
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
