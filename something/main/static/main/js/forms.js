function validate() {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        form.submit();
        form.clear();
      }

      form.classList.add('was-validated');
    }, false)
  })
}

function send() {
    $('#contacts_form').on('click', 'a', function() {
        const form = $('#contacts_form')[0];
        const event = new Event("submit");
        form.dispatchEvent(event);
    })
}

$(function () {
    send();
    validate();
});