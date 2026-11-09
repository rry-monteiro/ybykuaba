// fechamenbto da janela com esc
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' || event.key === 'Esc') {
        pywebview.api.close();
    }
});
