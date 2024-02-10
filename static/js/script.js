document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('match-button').addEventListener('click', function() {
        // Get the PHP file path from the button's data attribute
        var phpFile = this.getAttribute('data-php-file');
    });
});