function func() {
    var fname = $("#fname").val();
    if (fname == '') {
        $('#fn').html("Please enter valid name!");
        $('#fn').css('color', 'red');
        return false;
    } else {
        $('#fn').html('');
    }

    var lname = $("#lname").val();
    if (lname == '') {
        $('#ln').html("Please enter valid name!");
        $('#ln').css('color', 'red');
        return false;
    } else {
        $('#ln').html('');
    }

    var mobile = $("#mno").val();
    if (!mobile.match(/^\d{10}$/)) {
        $('#mob').html('Please enter valid mobile number!');
        $('#mob').css('color', 'red');
        return false;
    } else {
        $('#mob').html('');
    }

    var cname = $("#cname").val();
    if (cname == '') {
        $('#cn').html("Please enter valid name!");
        $('#cn').css('color', 'red');
        return false;
    } else {
        $('#cn').html('');
    }

    var email = $("#email").val();
    mail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (!email.match(mail)) {
        $('#em').html('Please enter valid email!');
        $('#em').css('color', 'red');
        return false;
    } else {
        $('#em').html('');
    }

    var com = $("#comments").val();
    if (com == '') {
        $('#cm').html("Please fill  this section!");
        $('#cm').css('color', 'red');
        return false;
    } else {
        $('#cm').html('');
    }
}

$.ajax({
    url: '/submit_form_view/',
    type: 'POST',
    data: JSON.stringify(formData),
    contentType: 'application/json',
    success: function(response) {
      // Handle the success response
      displaySuccessMessage('Success! Form submitted.');
      $('#submit').prop('disabled', true);
      $('#reset').prop('disabled', true);
      $('#reset-link').show();
    },
    error: function(error) {
      // Handle the error response
      displayError('form-error', 'An error occurred. Please try again later.');
    }
  });