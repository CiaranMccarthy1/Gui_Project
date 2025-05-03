function updateTotal() {
    let total = 0;
    document.querySelectorAll('.quantity-input').forEach(input => {
        const quantity = parseInt(input.value) || 1;
        const price = parseFloat(input.dataset.price);
        const itemTotal = quantity * price;

        input.closest('li').querySelector('.item-total').textContent = `$${itemTotal.toFixed(2)}`;
        total += itemTotal;
    });
    document.getElementById('total-amount').textContent = `$${total.toFixed(2)}`;
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('input', updateTotal);
    });
    updateTotal();
});
