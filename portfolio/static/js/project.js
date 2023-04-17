window.addEventListener('scroll', function() {
  var navbar = document.querySelector('.navbar');
  if (window.pageYOffset > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});
