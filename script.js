        document.addEventListener('DOMContentLoaded', () => {
            AOS.init({
                duration: 1000,
                once: true
            });

            const burgerMenu = document.querySelector('.burger-menu');
            const overlay = document.querySelector('.overlay');
            const overlayLinks = document.querySelectorAll('.overlay-content a');

            burgerMenu.addEventListener('click', () => {
                burgerMenu.classList.toggle('active');
                overlay.style.display = overlay.style.display === 'flex' ? 'none' : 'flex';
            });

            overlayLinks.forEach(link => {
                link.addEventListener('click', () => {
                    burgerMenu.classList.remove('active');
                    overlay.style.display = 'none';
                });
            });
        });