function toggleSidenote(wrapper) {
    const isClicked = wrapper.getAttribute('data-clicked') === 'true';

    if (isClicked) {
        wrapper.setAttribute('data-clicked', 'false');
    } else {
        document.querySelectorAll('.sidenote-wrapper[data-clicked="true"]').forEach(el => {
            el.setAttribute('data-clicked', 'false');
        });
        wrapper.setAttribute('data-clicked', 'true');
    }
}

document.addEventListener('click', function (event) {
    const clickedSidenote = event.target.closest('.sidenote-wrapper');

    if (!clickedSidenote) {
        document.querySelectorAll('.sidenote-wrapper[data-clicked="true"]').forEach(el => {
            el.setAttribute('data-clicked', 'false');
        });
    }
});
