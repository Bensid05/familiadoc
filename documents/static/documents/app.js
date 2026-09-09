document.addEventListener('DOMContentLoaded', () => {
    const password = document.getElementById('password');
    const togglePassword = document.getElementById('toggle-password');
    const loginForm = document.getElementById('login-form');
    const loginSubmit = document.getElementById('login-submit');

    if (password && togglePassword) {
        togglePassword.addEventListener('click', () => {
            const isHidden = password.type === 'password';
            password.type = isHidden ? 'text' : 'password';
            togglePassword.textContent = isHidden ? 'Masquer' : 'Afficher';
        });
    }

    if (loginForm && loginSubmit) {
        loginForm.addEventListener('submit', () => {
            loginSubmit.disabled = true;
            loginSubmit.textContent = 'Connexion en cours...';
        });
    }

    const fileInput = document.getElementById('file');
    const fileName = document.getElementById('file-name');
    const uploadForm = document.getElementById('upload-form');
    const uploadSubmit = document.getElementById('upload-submit');

    if (fileInput && fileName) {
        fileInput.addEventListener('change', () => {
            fileName.textContent = fileInput.files[0]
                ? fileInput.files[0].name
                : 'Choisir un fichier depuis votre appareil';
        });
    }

    if (uploadForm && uploadSubmit) {
        uploadForm.addEventListener('submit', () => {
            uploadSubmit.disabled = true;
            uploadSubmit.textContent = 'Téléversement en cours...';
        });
    }

    const searchInput = document.getElementById('document-search');
    const cards = [...document.querySelectorAll('.document-card')];
    const noResults = document.getElementById('no-results');

    if (searchInput && noResults) {
        searchInput.addEventListener('input', () => {
            const query = searchInput.value.trim().toLowerCase();
            let visibleCards = 0;

            cards.forEach((card) => {
                const matches = card.dataset.search.includes(query);
                card.classList.toggle('hidden', !matches);
                if (matches) visibleCards += 1;
            });

            noResults.classList.toggle(
                'hidden',
                visibleCards > 0 || cards.length === 0,
            );
        });
    }
});
