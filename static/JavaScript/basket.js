// Waits for the dom to load before executing codw
document.addEventListener("DOMContentLoaded", () => {
  // gets all quantity input feilds and the total amount 
    const quantityInputs = document.querySelectorAll(".quantity-input");
    const totalAmount = document.getElementById("total-amount");
  
    // Function updates the total price in real time
    function updateTotal() {
      let total = 0;
      const itemTotals = document.querySelectorAll(".item-total");
  
      // Loops through each quantity input to claculate item total 
      quantityInputs.forEach((input, index) => {
        const price = parseFloat(input.dataset.price);
        const quantity = parseInt(input.value) || 1; // Gets the quantity or sets it to 1 if invalid 
        const itemTotal = price * quantity;
        itemTotals[index].textContent = `€${itemTotal.toFixed(2)}`;
        total += itemTotal;
      });
  
      // Updates the total amount display
      totalAmount.textContent = `€${total.toFixed(2)}`;
      localStorage.setItem("basketTotal", total.toFixed(2));
    }
    
    // Event listerner for when quantity input is changed
    quantityInputs.forEach((input) => {
      input.addEventListener("input", updateTotal);
    });
    
    // Inititial call when page is loaded
    updateTotal();
  });
  