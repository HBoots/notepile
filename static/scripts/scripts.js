const items = document.querySelectorAll(".nav-item");

items.forEach((item) => {
    item.addEventListener("click", setActiveClass);
});

function setActiveClass(event) {
    items.forEach((item) => {
        item.classList.remove("active");
    });
    event.target.classList.add("active");
}
