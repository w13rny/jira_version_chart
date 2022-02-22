document.addEventListener('DOMContentLoaded', () => {

  // Get all "toggle" elements
  const $toggles = Array.prototype.slice.call(document.querySelectorAll('.toggle'), 0);

  // Check if there are any toggles
  if ($toggles.length > 0) {

    // Add a click event on each of them
    $toggles.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle
        if ($target.style.display === "none") {
          el.innerHTML = '<span class="icon"><i class="fas fa-angle-down"></i></span>';
          $target.style.display = "block";

        } else {
          el.innerHTML = '<span class="icon"><i class="fas fa-angle-up"></i></span>';
          $target.style.display = "none";
        }

      });
    });
  }

});