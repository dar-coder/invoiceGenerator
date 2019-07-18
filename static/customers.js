let form = document.getElementById("customers");

let customer_error = document.getElementById("customer_error");

let location_error = document.getElementById("location_error");

form.onsubmit = function()
{
    if (!form.customer.value)
    {
        customer_error.textContent = "Company/Full Name is a required field!";
        form.customer.style.border = "1px solid red";
        form.customer.focus();

        location_error.textContent = "";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";

        return false;
    }

    else if (!form.address.value)
    {
        customer_error.textContent = "Address is a required field!";
        form.address.style.border = "1px solid red";
        form.address.focus();

        location_error.textContent = "";
        form.customer.style.border = "2px groove";
        form.city.style.border = "2px groove";
        form.country.style.border = "2px groove";

        return false;
    }

    else if (!form.city.value)
    {
        location_error.textContent = "City/Town is a required field!";
        form.city.style.border = "1px solid red";
        form.city.focus();

        customer_error.textContent = "";
        form.customer.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.country.style.border = "2px groove";

        return false;
    }

    else if (!form.country.value)
    {
        location_error.textContent = "Country/State is a required field!";
        form.country.style.border = "1px solid red";
        form.country.focus();

        customer_error.textContent = "";
        form.customer.style.border = "2px groove";
        form.address.style.border = "2px groove";
        form.city.style.border = "2px groove";

        return false;
    }

    return true;
}