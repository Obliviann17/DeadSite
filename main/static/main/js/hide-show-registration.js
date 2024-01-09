function togglePasswordVisibility(fieldNumber) {
    var passwordInput = document.getElementById("pass" + fieldNumber);
    var passHide = document.getElementById("pass-hide" + fieldNumber);
    var passShow = document.getElementById("pass-show" + fieldNumber);
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        passHide.style.display = "none";
        passShow.style.display = "inline";
    } else {
        passwordInput.type = "password";
        passHide.style.display = "inline";
        passShow.style.display = "none";
    }
}