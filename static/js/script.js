var slideIndex = 0;

function showSlides() {
    var slides = document.getElementsByClassName("full-width-img");
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 4000); // Change image every 4 seconds
}

showSlides(); // Initial call to start the slideshow

// Get the product container element
var productContainer = document.querySelector(".product-container");

// Function to check if an element is in view
function isInView(element) {
    var bounding = element.getBoundingClientRect();
    return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to check if the product container is in view and add class to show products
function checkProductVisibility() {
    if (isInView(productContainer)) {
        productContainer.classList.add("appear");
    }
}

// Initial check when the page loads
checkProductVisibility();

// Check when the user scrolls
window.addEventListener("scroll", function () {
    checkProductVisibility();
});

