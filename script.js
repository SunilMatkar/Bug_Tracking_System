// Add your JavaScript code here
document.getElementById("bug-report-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const bugDescription = document.getElementById("bug-description").value;
    // Use an API call to submit the bug description to the server
});
