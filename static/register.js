let form = document.getElementById("register");

let company_error = document.getElementById("company_error");

let address_error = document.getElementById("address_error");

let city_error = document.getElementById("city_error");

let country_error = document.getElementById("country_error");

let ceofirst_error = document.getElementById("ceofirst_error");

let ceolast_error = document.getElementById("ceolast_error");

let username_error = document.getElementById("username_error");

let password_error = document.getElementById("password_error");

let confirmation_error = document.getElementById("confirmation_error");

form.onsubmit = function() {
    if (!form.company.value)
    {
        company_error.textContent = "Company name is required!";
        form.company.style.border = "1px solid red";
        form.company.focus();

        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.address.value)
    {
        address_error.textContent = "Company address is required!";
        form.address.style.border = "1px solid red";
        form.address.focus();

        company_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.city.value)
    {
        city_error.textContent = "City field is required!";
        form.city.style.border = "1px solid red";
        form.city.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.country.value)
    {
        country_error.textContent = "Country/State field is required!";
        form.country.style.border = "1px solid red";
        form.country.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.ceofirst.value)
    {
        ceofirst_error.textContent = "CEO's first name is required!";
        form.ceofirst.style.border = "1px solid red";
        form.ceofirst.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.ceolast.value)
    {
        ceolast_error.textContent = "CEO's last name is required!";
        form.ceolast.style.border = "1px solid red";
        form.ceolast.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.username.value)
    {
        username_error.textContent = "Username field is required!";
        form.username.style.border = "1px solid red";
        form.username.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        password_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.password.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (!form.password.value)
    {
        password_error.textContent = "Password field is required!";
        form.password.style.border = "1px solid red";
        form.password.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (form.password.value.length < 8)
    {
        password_error.textContent = "Password must be at least 8 characters long!";
        form.password.style.border = "1px solid red";
        form.password.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        confirmation_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.confirmation.style.border = "2px groove";

        return false;
    }

    else if (form.confirmation.value != form.password.value)
    {
        confirmation_error.textContent = "Passwords don't match!";
        form.confirmation.style.border = "1px solid red";
        form.confirmation.focus();

        company_error.textContent = "";
        address_error.textContent = "";
        city_error.textContent = "";
        country_error.textContent = "";
        ceofirst_error.textContent = "";
        ceolast_error.textContent = "";
        username_error.textContent = "";
        password_error.textContent = "";

        form.company.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";
        form.ceofirst.style.border = "2px groove";
        form.ceolast.style.border = "2px groove";
        form.username.style.border = "2px groove";
        form.password.style.border = "1px solid red";

        return false;
    }

    return true;
}