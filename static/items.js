let form = document.getElementById("form");

let input_error = document.getElementById("input_error");

form.onsubmit = function()
{
    if (!form.item.value)
    {
        input_error.textContent = "Item is a required field!";
        form.item.style.border = "1px solid red";
        form.item.focus();

        form.price.style.border = "2px groove";

        return false;
    }

    else if (!form.price.value)
    {
        input_error.textContent = "Unit Price is a required field!";
        form.price.style.border = "1px solid red";
        form.price.focus();

        form.item.style.border = "2px groove";

        return false;
    }

    return true;
}