document.addEventListener("DOMContentLoaded", () => {
    // Retrieve basketTotal from localStorage or default to 0.00
    const basketTotal = localStorage.getItem("basketTotal") || "0.00";

    // Update the basket total display
    document.getElementById("basket-total").textContent = `€${basketTotal}`;

    const checkoutForm = document.getElementById("checkout-form");
    checkoutForm.addEventListener("submit", (Event) => {
        Event.preventDefault();

        const address = document.getElementById("address").value;

        const confirmation = confirm(`Your total is €${basketTotal}.\nDeliver to: ${address}`);
        if (confirmation) {
            localStorage.removeItem("basket");
            localStorage.removeItem("basketTotal");

            alert("Thank you for your order. Your order will be delivered soon")
            window.location.href = "/";
        }
        
    })
});