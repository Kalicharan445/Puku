
document.getElementById("birthdayForm").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const name = document.getElementById("name").value;
    const birthday = document.getElementById("birthday").value;
    
    // Simple birthday logic: check if today is the user's birthday
    const today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
    
    let message = "Thanks for submitting!";
    if (birthday === today) {
        message = `Happy Birthday, ${name}! 🎉`;
    }
    
    document.getElementById("message").innerText = message;
});
