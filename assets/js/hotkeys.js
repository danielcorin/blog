// Add hotkey listeners
document.addEventListener('keydown', function (event) {
    if (window.location.pathname === '/') {
        switch (event.key.toLowerCase()) {
            case 'a':
                window.location.href = '/about/';
                break;
            case 'f':
                window.location.href = '/feeds/';
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
    } else if (window.location.pathname !== '/search/' && event.key.toLowerCase() === 'h') {
        window.location.href = '/';
    }
});
