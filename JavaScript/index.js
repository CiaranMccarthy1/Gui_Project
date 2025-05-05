document.querySelectorAll('form[action="/order"]').forEach(form => {
    form.addEventListener("submit", () => {
        let count = parseInt(localStorage.getItem("basketCount"));
        count += 1;
        localStorage.setItem("basketCount", count);
    })
})