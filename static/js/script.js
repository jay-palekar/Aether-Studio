const sections = document.querySelectorAll(
    ".service-card, .project-card, .about-container, .contact-container"
);

const observer = new IntersectionObserver((entries) => {

    entries.forEach((entry) => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        } else {

            entry.target.classList.remove("show")

        }

    });

}, {

    threshold: 0.2 
});

sections.forEach((section) => {

    observer.observe(section);

});