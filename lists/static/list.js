window.Superlists = {}; // there are better ways of dealing with namespace in js
window.Superlists.initialize = () => {
    $('input[name="text"]').on('keypress click', () => {
        $('.has-error').hide();
    })
}
