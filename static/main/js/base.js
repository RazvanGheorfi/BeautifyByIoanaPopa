function showGallery() {
    var x = document.getElementById("dropdown_menu");
    var xx = document.getElementById("dropdown_menu2");
    var y = document.getElementById("sort-up");
    var z = document.getElementById("sort-down");
    x.classList.toggle("mystyle");
    xx.classList.remove("mystyle2");
    if (z.style.display === "inline") {
        z.style.display = "none";
        y.style.display = "inline";
    } else {
        y.style.display = "none";
        z.style.display = "inline";
    }
}

function showLearn() {
    var x = document.getElementById("dropdown_menu2");
    var xx = document.getElementById("dropdown_menu");
    var y = document.getElementById("sort-up2");
    var z = document.getElementById("sort-down2");
    x.classList.toggle("mystyle2");
    xx.classList.remove("mystyle");
    if (z.style.display === "inline") {
        z.style.display = "none";
        y.style.display = "inline";
    } else {
        y.style.display = "none";
        z.style.display = "inline";
    }
}


function hamburgers() {
    var hamburger = document.getElementById("hamburger");
    var closed = document.getElementById("closed");
    var navigation = document.getElementById("navbar");
    hamburger.classList.toggle("ham-hide");
    closed.classList.toggle("clo-show");
    navigation.classList.toggle("clo-show");
}