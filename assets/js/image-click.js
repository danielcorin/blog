document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.content img');
    let modal = null;

    function createModal() {
        modal = document.createElement('div');
        modal.className = 'image-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                <img src="" alt="Expanded image">
            </div>
        `;
        document.body.appendChild(modal);

        const closeBtn = modal.querySelector('.close');
        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', function (e) {
            if (e.target === modal || e.target.classList.contains('modal-content')) {
                closeModal();
            }
        });
    }

    function openModal(imgSrc) {
        if (!modal) createModal();
        const modalImg = modal.querySelector('img');
        modalImg.src = imgSrc;
        modal.style.display = 'flex';
    }

    function closeModal() {
        if (modal) modal.style.display = 'none';
    }

    images.forEach(img => {
        img.addEventListener('click', function () {
            openModal(this.src);
        });
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeModal();
    });
});
