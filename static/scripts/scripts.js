const items = document.querySelectorAll(".nav-item");

items.forEach((item) => {
    item.addEventListener("click", (e) => {
        item.forEach((f) => {
            f.classList.remove("active");
        });
        e.target.classList.add("active");
    });
});
