$(document).ready(function() {
    "use strict";

    $(function() {
        var current_fs, next_fs, previous_fs; //fieldsets
        var left, opacity, scale; //fieldset properties which we will animate
        var animating; //flag to prevent quick multi-click glitches   

        $(".next").click(function() {
            var form = $("#msform");
            form.validate({
                // Specify validation rules
                errorElement: 'span',
                errorClass: 'help-block',
                highlight: function(element, errorClass, validClass) {
                    $(element).closest('.loan_input').addClass("has-error");
                },
                unhighlight: function(element, errorClass, validClass) {
                    $(element).closest('.loan_input').removeClass("has-error");
                },
                rules: {
                    // The key name on the left side is the name attribute
                    // of an input field. Validation rules are defined
                    // on the right side
                    dependents: "required",
                    applicant_income: "required",
                    coapplicant_income: "required",
                    loan_amount: "required",
                    loan_amount_term: "required",
                    credit_history: "required",
                },
                // Specify validation error messages
                messages: {
                    dependents: "Enter amount of dependents",
                    applicant_income: "Enter applicant income",
                    coapplicant_income: "Enter co-applicant income",
                    loan_amount: "Enter loan amount",
                    loan_amount_term: "Enter loan amount in months",
                    credit_history: "Enter your credit history",
                },
                submitHandler: function(form) {
                    $.ajax({
                        type: form.method,
                        url: form.action,
                        data: {
                            gender: $('#id_gender').val(),
                            married: $('#id_married').val(),
                            dependents: $('#id_dependents').val(),
                            education: $('#id_education').val(),
                            self_employed: $('#id_self_employed').val(),
                            applicant_income: $('#id_applicant_income').val(),
                            coapplicant_income: $('#id_coapplicant_income').val(),
                            loan_amount: $('#id_loan_amount').val(),
                            loan_amount_term: $('#id_loan_amount_term').val(),
                            credit_history: $('#id_credit_history').val(),
                            property_area: $('#id_property_area').val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        },
                        dataType: 'json',

                        success: function(json, response) {
                            document.forms["msform"].reset();
                            console.log('Post Successful')

                            var obj = json
                            var myJSON = JSON.stringify(obj);
                            console.log(myJSON)

                            var jsonString = JSON.parse(myJSON);
                            var prediction = jsonString.prediction;

                            response = prediction


                            if(response == 'approved') {
                                $("#response_dict").html("<span href='#' class='don_icon'>\
                                                              <i class='ion-android-done'></i>\
                                                          </span>\
                                                          <h6>Your loan status is approved!</h6>");
                            } else{
                                $("#response_dict").html("<span href='#' class='don_icon error_icon'>\
                                                              <i class='ion-android-close'></i>\
                                                          </span>\
                                                          <h6>Your loan status is rejected!</h6>");
                            }

                            console.log(response);
                        },
                        error: function(xhr, errmsg, err) {
                            console.log('Post Failed')
                        }
                    });
                }
            });


            if (form.valid() === true) {
                if ($('#personal_info').is(":visible")) {
                    current_fs = $(this).parent();
                    next_fs = $(this).parent().next();
                }
                //show the next fieldset
                next_fs.show();

                //activate next step on progressbar using the index of next_fs
                $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

                if (animating) return false;
                animating = true;
                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function(now, mx) {
                        //as the opacity of current_fs reduces to 0 - stored in "now"
                        //1. scale current_fs down to 80%
                        scale = 1 - (1 - now) * 0.2;
                        //2. bring next_fs from the right(50%)
                        left = (now * 50) + "%";
                        //3. increase opacity of next_fs to 1 as it moves in
                        opacity = 1 - now;
                        current_fs.css({
                            'transform': 'scale(' + scale + ')',
                            'position': 'absolute'
                        });
                        next_fs.css({
                            'left': left,
                            'opacity': opacity
                        });
                    },
                    duration: 800,
                    complete: function() {
                        current_fs.hide();
                        animating = false;
                    },
                    //this comes from the custom easing plugin
                    easing: 'easeInOutBack'
                });
            }

        });

        $(".reload").click(function(){
            location.reload(true);
        });

        $(".previous").click(function() {
            if (animating) return false;
            animating = true;

            current_fs = $(this).parent();
            previous_fs = $(this).parent().prev();

            //de-activate current step on progressbar
            $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

            //show the previous fieldset
            previous_fs.show();
            //hide the current fieldset with style
            current_fs.animate({
                opacity: 0
            }, {
                step: function(now, mx) {
                    //as the opacity of current_fs reduces to 0 - stored in "now"
                    //1. scale previous_fs from 80% to 100%
                    scale = 0.8 + (1 - now) * 0.2;
                    //2. take current_fs to the right(50%) - from 0%
                    left = ((1 - now) * 50) + "%";
                    //3. increase opacity of previous_fs to 1 as it moves in
                    opacity = 1 - now;
                    current_fs.css({
                        'left': left
                    });
                    previous_fs.css({
                        'transform': 'scale(' + scale + ')',
                        'opacity': opacity
                    });
                },
                duration: 800,
                complete: function() {
                    current_fs.hide();
                    animating = false;
                },
                //this comes from the custom easing plugin
                easing: 'easeInOutBack'
            });
        });

        $(".submit").click(function() {
            var form = $("#msform");

            if (form.valid() === true) {
                if ($('#loan_info').is(":visible")) {
                    current_fs = $(this).parent();
                    next_fs = $(this).parent().next();
                }

                //show the next fieldset
                next_fs.show();

                //activate next step on progressbar using the index of next_fs
                $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

                if (animating) return false;
                animating = true;
                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function(now, mx) {
                        //as the opacity of current_fs reduces to 0 - stored in "now"
                        //1. scale current_fs down to 80%
                        scale = 1 - (1 - now) * 0.2;
                        //2. bring next_fs from the right(50%)
                        left = (now * 50) + "%";
                        //3. increase opacity of next_fs to 1 as it moves in
                        opacity = 1 - now;
                        current_fs.css({
                            'transform': 'scale(' + scale + ')',
                            'position': 'absolute'
                        });
                        next_fs.css({
                            'left': left,
                            'opacity': opacity
                        });
                    },
                    duration: 800,
                    complete: function() {
                        current_fs.hide();
                        animating = false;
                    },
                    //this comes from the custom easing plugin
                    easing: 'easeInOutBack'
                });
            }
        })
    });

    //* Select js
    function nice_Select() {
        if ($('.product_select').length) {
            $('select').niceSelect();
        };
    };
    /*Function Calls*/
    nice_Select();
});

$(document).on({
    ajaxStart: function() {
        $("#response_loading").html("<div class='container'>\
                                        <div class='row'>\
                                            <div class='col-12'>\
                                                <img class='loading_img mx-auto d-block img-fluid' src='static/app/img/loading.gif'>\
                                            </div>\
                                        </div>\
                                    </div>");
    },
    ajaxStop: function() {
        $("#response_loading").html("");
    }
});