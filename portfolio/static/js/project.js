$(document).ready(function() {
  $(".profile-link").click(function(e) {
    e.preventDefault();
    $("#profile-menu").toggleClass("d-none");
  });
});
