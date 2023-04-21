const toggle = document.querySelector('.toggle'),
    navbarMenu = document.querySelector('.navbar_menu'),
    cross = document.querySelector(".cross");

toggle.addEventListener('click', () => {
    navbarMenu.style.display = "flex"
    document.body.style.overflow = "hidden"
})

cross.addEventListener('click', () => {
    navbarMenu.style.display = "none"
    document.body.style.overflow = "scroll"
})
