function func(){
    const form = document.querySelector('form');


    var fname=document.getElementById("fname").value
    var lname=document.getElementById("lname").value
    var mno=document.getElementById("mno").value
    var cname=document.getElementById("cname").value
    var email=document.getElementById("email").value
    var comments=document.getElementById("comments").value

    let isValid=true

    if (fname.trim() === '') {
        showErrorMessage(fname, 'Please enter your name');
        isValid = false;
        }

        if (lname.trim() === '') {
            showErrorMessage(lname, 'Please enter your name');
            isValid = false;
            }

            if (cname.trim() === '') {
                showErrorMessage(cname, 'Please enter your name');
                isValid = false;
                }

                if (comments.trim() === '') {
                    showErrorMessage(comments, 'Please enter your name');
                    isValid = false;
                    }

            if (mno.trim() === '') {
                showErrorMessage(mno, 'Please enter your mobile number');
                isValid = false;
                } else if (!validateMobileNumber(mno.value)) {
                showErrorMessage(mno, 'Mobile number should be numeric and 10 digits');
                isValid = false;
                }

                if (email.trim() === '') {
                    showErrorMessage(email, 'Please enter your email address');
                    isValid = false;
                    
                    } else if (!validateEmail(email.value)) {
                    showErrorMessage(email, 'Please enter a valid email address');
                    isValid = false;
                    }
                    if (isValid) {
                        form.reset();
                        form.style.display = 'none';
                        
                      }
                    

}

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
    }
    // Function to validate mobile number
    function validateMobileNumber(mobile) {
    const mobileRegex = /^\d{10}$/;
    return mobileRegex.test(mobile);
    }    

    function showErrorMessage(input, message) {
        
        input.textContent = message;
        
      }
      