function togglePasswordVisibility() {
  var passwordInput = document.getElementById("pass");
  var passHide = document.getElementById("pass-hide");
  var passShow = document.getElementById("pass-show");
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