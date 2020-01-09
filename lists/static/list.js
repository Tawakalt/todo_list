window.Superlists = {}; // there are better ways of dealing with namespace in js
window.Superlists.initialize = () => {
    $('input[name="text"]').on('keypress', () => {
        $('.has-error').hide();
    })
}
