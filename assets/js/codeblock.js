document.addEventListener("DOMContentLoaded", function () {

    // Add title tabs to highlight blocks first
    var els = document.getElementsByClassName("highlight");
    for (var i = 0; i < els.length; i++) {
        if (els[i].title && els[i].title.length) {
            // Create a wrapper div to contain both the title and the highlight
            var wrapper = document.createElement("div");
            wrapper.className = "highlight-wrapper";

            // Create the title element
            var titleNode = document.createElement("div");
            var textNode = document.createTextNode(els[i].title);
            titleNode.appendChild(textNode);
            titleNode.classList.add("highlight-title");

            // Insert the wrapper before the highlight
            els[i].parentNode.insertBefore(wrapper, els[i]);

            // Move the highlight into the wrapper and add the title before it
            wrapper.appendChild(titleNode);
            wrapper.appendChild(els[i]);

            // Add a class to the highlight element to indicate it has a title
            els[i].classList.add("has-title");
        }
    }

    // Get code blocks
    const codeblocks = document.querySelectorAll("pre code");

    // Iterate over each to perform modifications
    codeblocks.forEach((codeblock) => {
        // Create copy button and container element
        const copyButton = document.createElement("button");
        copyButton.className = "copy-button";
        const container = document.createElement("div");
        container.className = "code-container";

        // Copy clicked closure
        copyButton.addEventListener("click", (e) => {
            e.target.className = "copy-success";
            setTimeout(() => {
                e.target.className = "copy-button";
            }, 1000);
            const code = codeblock.textContent;
            navigator.clipboard.writeText(code);
        });

        // Wrap the codeblock with the container
        codeblock.parentNode.insertBefore(container, codeblock);
        container.appendChild(codeblock);
        // Add the copy button to the container
        container.appendChild(copyButton);
    });
});
