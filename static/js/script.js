$(document).ready(function() {
    $("#match-button").click(function() {
        $.ajax({
            type: 'GET',
            url: '/getMap',
            success: function(response) {
                $("body").html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});