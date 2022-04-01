
const SIGNUP_FORM_ID          = "signUpForm";
const SIGNUP_ALERT            = "signUpAlert";
const SIGNUP_BUTTON           = "signUpButton";

const SIGNIN_BUTTON           = "signInButton";
const CUSTOMER_SIGNUP_BUTTON  = "customerSignUpButton";
const RIDER_SIGNUP_BUTTON     = "riderSignUpButton";
const SIGNIN_ALERT            = "signInAlert";
const SIGNIN_FORM             = "signInForm";
const CUSTOMER_SIGNIN_FORM    = "customerSignUpForm";
const EMAIL_ALERT             = "emailAlert";
const EMAIL_FIELD             = "email";

$(document).ready(function() {

    // Sign Up form
    // Fix the URL properly to send the request to the back-end
    $("#" + SIGNUP_BUTTON).click(function(event) {

        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({

            url: "/",
            data: formData,
            type: "POST",

            success: function(data) {

                $('#' + SIGNUP_ALERT).removeClass("d-none");

                setTimeout(function () {
                    $('#' + SIGNUP_ALERT).addClass("d-none");
                }, 2000);

            }

        });

    });

    // Sign In form
    // Fix the URL properly to send the request to the back-end
    $("#" + SIGNIN_BUTTON).click(function(event) {

        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({

            url: "/",
            data: formData,
            type: "POST",

            success: function(data) {

                $('#' + SIGNIN_ALERT).removeClass("d-none");

                setTimeout(function () {
                    $('#' + SIGNIN_ALERT).addClass("d-none");
                }, 2000);

            }

        });

    });

    var $emailFiend = $('#' + EMAIL_FIELD);

    if ($emailFiend) {

        $emailFiend.change(function () {
            validateEmail($(this));
        });

        $emailFiend.keyup(function () {
            validateEmail($(this));
        });

    }

});

// Validates email field
function validateEmail ($emailField) {

    var emailId       = $emailField.val();
    var $form         = $emailField.closest("form");
    var $submitButton = $form.find("button");

    if (/^([A-Za-z0-9_\-\.])+\@gwmail.gwu.edu$/.test(emailId)) {

        $submitButton.prop("disabled", false);
        $('#' + EMAIL_ALERT).addClass("d-none");

    }
    else {

        $submitButton.prop("disabled", true);
        $('#' + EMAIL_ALERT).removeClass("d-none");

    }

}