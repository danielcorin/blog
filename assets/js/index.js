// Add hotkey listeners if we're on the homepage
if (window.location.pathname === '/') {
    document.addEventListener('keydown', function (event) {
        switch (event.key.toLowerCase()) {
            case 'a':
                window.location.href = '/about/';
                break;
            case 'g':
                window.location.href = '/garden/';
                break;
            case 'l':
                window.location.href = '/logs/';
                break;
            case 'n':
                window.location.href = '/now/';
                break;
            case 'p':
                window.location.href = '/posts/';
                break;
            case 's':
                window.location.href = '/search/';
                break;
            case 't':
                window.location.href = '/til/';
                break;
            case 'u':
                window.location.href = '/uses/';
                break;
        }
    });
}
