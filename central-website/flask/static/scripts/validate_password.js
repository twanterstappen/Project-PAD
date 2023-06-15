function validatePassword() {
    var password = document.getElementById("password").value;

    if (password.length < 8) {
        alert("Password must be at least 8 characters long");
        return false;
    }

    if (!password.match(/[a-z]/)) {
        alert("Password must contain at least one lowercase letter");
        return false;
    }

    if (!password.match(/[A-Z]/)) {
        alert("Password must contain at least one uppercase letter");
        return false;
    }

    if (!password.match(/[0-9]/)) {
        alert("Password must contain at least one number");
        return false;
    }
    if (!password.match(/[!@#$%^&*()\-=_+{}[\]|;:'",.<>/?\\]/)) {
        alert("Password must contain at least one special character");
        return false;
    }


    return true;
}
function updatePasswordStrength() {
    var password = document.getElementById("password").value;
    var strengthBar = document.getElementById("strength-bar");
    var strengthText = document.getElementById("strength-text");

    // Calculate password strength
    var strength = 0;
    if (password.match(/[a-z]/)) {
        strength += 1;
    }
    if (password.match(/[A-Z]/)) {
        strength += 1;
    }
    if (password.match(/[0-9]/)) {
        strength += 1;
    }
    if (password.match(/[!@#$%^&*()\-=_+{}[\]|;:'",.<>/?\\]/)) {
        strength += 1;
    }
    if (password.length >= 8) {
        strength += 1;
    }


    if (password.length === 0) {
        strengthBar.style.width = "0%";
        strengthBar.style.backgroundColor = "";
        strengthText.textContent = "";
    } else {
        var strengthPercentage = (strength / 5) * 100;
        strengthBar.style.width = strengthPercentage + "%";

        if (strengthPercentage <= 20) {
            strengthBar.style.backgroundColor = "darkred";
            strengthText.textContent = "Very Weak";
            strengthText.style.color = "red";
        } else if (strengthPercentage <= 40) {
            strengthBar.style.backgroundColor = "red";
            strengthText.textContent = "Weak";
            strengthText.style.color = "red";
        } else if (strengthPercentage <= 60) {
            strengthBar.style.backgroundColor = "orange";
            strengthText.textContent = "Moderate";
            strengthText.style.color = "orange";
        } else if (strengthPercentage <= 80) {
            strengthBar.style.backgroundColor = "yellow";
            strengthText.textContent = "Strong";
            strengthText.style.color = "yellow";
        } else {
            strengthBar.style.backgroundColor = "green";
            strengthText.textContent = "Very Strong";
            strengthText.style.color = "darkgreen";
        }
    }
}