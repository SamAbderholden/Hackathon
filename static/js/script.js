$(document).ready(function() {
    $("#match-button").click(function() {
        let zipcode = document.getElementById('zipcode').value;
        let plan = document.getElementById('plan-select').value;
        let provider = document.getElementById('provider-select').value;

        $.ajax({
            type: 'GET',
            url: '/getMap',
            data: {'zipcode': zipcode, 'plan': plan, 'provider': provider},
            success: function(response) {
                $("body").html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
