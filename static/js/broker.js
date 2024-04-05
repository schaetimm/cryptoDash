document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.read-more').forEach(button => {
        button.addEventListener('click', () => {
            var card = button.closest('.broker-card');
            var description = card.querySelector('.broker-description');
            var isShort = description.classList.toggle('short');
            card.classList.toggle('expanded');
            button.textContent = isShort ? 'Mehr anzeigen' : 'Weniger anzeigen';
        });
    });
});


