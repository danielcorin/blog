---
categories: code
date: "2016-07-16T17:28:00Z"
title: Custom Markdown rendering
aliases:
    - /code/2016/07/16/custom-marked.html
tags:
    - code
    - javascript
    - markdown
---

Markdown is useful tool -- these blog posts are written in it. I like Markdown because once you learn it, it feels invisible. It is minimal and intuitive. However, sometimes you need it to do things a little differently.

I ran into an issue where I had content which had to be written in only Markdown (no HTML) and later needed to be rendered as HTML and inserted onto a webpage, but I needed to add attributes to the HTML tags that were generated. The content itself needed to look like this:

{{< highlight html >}}
<p><a href="http://blog.danielcorin.com/" target="_blank">Cool site</a></p>
{{< / highlight >}}

The `target="_blank"` attribute is the part of interest. Markdown gives a terse way of expressing simple HTML markup, but no real simple way to use some of the less used features of HTML (yes you can just write HTML in markdown but I am limited to just markdown for this use case). My content is being parsed in Javascript and I am using the [`marked`](https://www.npmjs.com/package/marked) npm package. The code looks something like this:

{{< highlight js >}}
var marked = require('marked');
var myContent = "[Cool site](https://google.com)"
var htmlContent = marked(myContent);
//=> '<p><a href="https://google.com">Cool site</a></p>\n'
{{< / highlight >}}

So, we have pretty much everything we need except the `target` attribute on the link. `marked` lets us modify its renderer and pass it in as an option when rendering markdown as HTML. You can find more docs on how to modify the renderer [here](https://github.com/chjj/marked#renderer).

{{< highlight js >}}
var marked = require('marked');
var myContent = "[Cool site](https://google.com)"
var myRenderer = new marked.Renderer();
myRenderer.link = function(href, title, text) {
    return `<a href="${href}" target="_blank">${text}</a>`;
}
var htmlContent = marked(myContent, {
    renderer: myRenderer
});
//=> '<p><a href="https://google.com" target="_blank">Cool site</a></p>\n'
{{< / highlight >}}

This solutions fits my needs. I can use the modified renderer on the pieces of content that need the additional attribute without breaking any of my other markdown. Best of all, I don't need any clever hacking to add the attribute to the links.

