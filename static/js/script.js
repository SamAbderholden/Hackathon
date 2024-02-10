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

    // Initial setup
    var providerSelect = $("#provider-select");
    var planSelect = $("#plan-select");

    // Define options for the second dropdown based on the selected provider
    var planOptions = {
        "Blue Cross Blue Shield": ["HMO", "EPO", "PPO", "POS"],
        // Add more providers and their plans as needed
    };

    // Disable the second dropdown initially
    planSelect.prop("disabled", true);

    // Add a non-selectable placeholder option
    planSelect.append($("<option>").text("Select Your Plan").val("null").prop("disabled", true).prop("selected", true).attr("style", "display:none;"));
    // Populate the second dropdown based on the selected provider
    providerSelect.change(function() {
        var selectedProvider = providerSelect.val();
        var options = planOptions[selectedProvider] || [];
        
        // Clear existing options
        planSelect.find("option:not(:first-child)").remove();

        // If a provider is selected, enable the second dropdown
        if (selectedProvider) {
            planSelect.prop("disabled", false);
        } else {
            // If no provider is selected, disable and set a default placeholder
            planSelect.prop("disabled", true);
            options = [];
        }

        // Populate options for the second dropdown
        $.each(options, function(index, value) {
            planSelect.append($("<option>").text(value).val(value));
        });
    });

    // Initial call to populate the second dropdown based on the default selected provider
    providerSelect.trigger("change");
});

function iframeLoaded() {
    document.getElementById('mapIframe').style.display = 'block'; // Make the iframe visible
}
