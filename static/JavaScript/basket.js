document.addEventListener("DOMContentLoaded", () => {
    const quantityInputs = document.querySelectorAll(".quantity-input");
    const totalAmount = document.getElementById("total-amount");
  
    function updateTotal() {
      let total = 0;
      const itemTotals = document.querySelectorAll(".item-total");
  
      quantityInputs.forEach((input, index) => {
        const price = parseFloat(input.dataset.price);
        const quantity = parseInt(input.value) || 1;
        const itemTotal = price * quantity;
        itemTotals[index].textContent = `$${itemTotal.toFixed(2)}`;
        total += itemTotal;
      });
  
      totalAmount.textContent = `$${total.toFixed(2)}`;
    }
  
    quantityInputs.forEach((input) => {
      input.addEventListener("input", updateTotal);
    });
  
    updateTotal();
  });
  