<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: *");
function processCoverage() {
    // Your PHP function logic goes here
    echo "Coverage processing completed.";
}

// Check if the AJAX request is made and call the function
if (isset($_POST['action']) && $_POST['action'] == 'process_coverage') {
    processCoverage();
}
?>
