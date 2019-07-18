let form = document.getElementById("invoicenumber");

let error = document.getElementById("error");

form.onsubmit = function()
{
    if (form.customer.value == "")
    {
        error.textContent = "Please select a customer!";
        form.customer.style.border = "1px solid red";

        return false;
    }

    return true;
}