const togglePassword1 = document.querySelector('#togglePassword1');
    const password1 = document.querySelector('#pass');
    togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
    password1.setAttribute('type', type);
    // toggle the eye icon
    this.classList.toggle('fa-eye-slash');
    });

    function RemoveSpecialChar(tags) {
      if (tags.value != '' && tags.value.match(/^[\w]+$/) == null ) {
      tags.value = tags.value.replace(/[\W]/g, '');
      }
    }

$(document).ready(function() { $('#loginModal').modal('show');
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
});

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()