function validateForm() {
    var password = document.getElementById('pass1').value;
    var repeatPassword = document.getElementById('pass2').value;
    var passwordInput = document.getElementById('pass1');
    var repeatPasswordInput = document.getElementById('pass2');  
    
    if (password.length < 8) {
        alert('The password must contain a minimum of 8 characters.');
        return false;
    }  
    var regex = /^[a-zA-Z0-9!@#$%^&*()_+{}|:"<>?~`\-=[\];',./\\]+$/;
    if (!regex.test(password)) {
        alert('Password must contain only English letters and symbols.');
        return false;
    }
    if (password !== repeatPassword) {
        alert("The passwords don't match.");
        passwordInput.classList.add('error');
        repeatPasswordInput.classList.add('error');
        return false;
    } else {
        passwordInput.classList.remove('error');
        repeatPasswordInput.classList.remove('error');
    }
    
    function redirectToPage() {
        window.location.href = 'index.html';
    }
    
    return true;
}
