// Keeps track of how many items are in basket and stores it in local storage
document.querySelectorAll('form[action="/order"]').forEach(form => {
    form.addEventListener("submit", () => {
        let count = parseInt(localStorage.getItem("basketCount"));
        count += 1;
        localStorage.setItem("basketCount", count);
    })
})