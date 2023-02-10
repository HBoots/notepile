const items = document.querySelectorAll(".nav-item");

items.forEach((item) => {
    item.addEventListener("click", (e, items) => {
        setActiveClass(e, items);
    });
});

function setActiveClass(event, array) {
    array.forEach((elem) => {
        elem.classList.remove("active");
    });
    event.target.classList.add("active");
}
