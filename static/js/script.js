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

    var providerSelect = $("#provider-select");
    var planSelect = $("#plan-select");

    var planOptions = {
        "Blue Cross Blue Shield": ["HMO", "EPO", "PPO", "POS"],
        "Kaiser Permanente" : ["Choice PPO", "KP Select", "Kaiser Permanente Colorado Option for Small Group", "Child Health Plan Plus", "Commercial", "Kaiser Permanente Colorado Option for Individual & Family", "Medicaid"],
        "Medicare": ["Medicare"]
    };

    planSelect.prop("disabled", true);

    planSelect.append($("<option>").text("Select Your Plan").val("null").prop("disabled", true).prop("selected", true).attr("style", "display:none;"));
    providerSelect.change(function() {
        var selectedProvider = providerSelect.val();
        var options = planOptions[selectedProvider] || [];

        planSelect.find("option:not(:first-child)").remove();

        if (selectedProvider) {
            planSelect.prop("disabled", false);
        } else {

            planSelect.prop("disabled", true);
            options = [];
        }

        $.each(options, function(index, value) {
            planSelect.append($("<option>").text(value).val(value));
        });
    });

    providerSelect.trigger("change");
});

