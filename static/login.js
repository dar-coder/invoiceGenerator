let form = document.getElementById("login");

let username_error = document.getElementById("username_error");

let password_error = document.getElementById("password_error");

form.onsubmit = function() {
    if (!form.username.value)
    {
        username_error.textContent = "Username is required!";
        form.username.style.border = "1px solid red";
        form.username.focus();
        password_error.textContent = "";
        form.password.style.border = "2px groove";
        return false;
    }

    else if (!form.password.value)
    {
        password_error.textContent = "Password is required!";
        form.password.style.border = "1px solid red";
        form.password.focus();
        username_error.textContent = "";
        form.username.style.border = "2px groove";
        return false;
    }

    return true;
}