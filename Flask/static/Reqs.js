/* Function trigger by click on the submit button. Parse the json response from Flask and display variables received */

$(function() {
    $('.btn').on('click', function() {
        var $this = $(this); /* Make a variable from the button */
        $this.button('loading'); /* Add a loading state that display an animated icon */
        $.ajax({
            url: '/update_map', /* Route where is the parser */
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var obj = JSON.parse(response); /* Parse the json replied by flask */
                var audio = new Audio('/static/notif.wav');
                audio.play();
                $("#txtHint").text(obj.answer); /* Display in the page the answer of PaPYbot */
                $("#link").attr("href", obj.link); /* Display the link of wikipedia */
                if (obj.link) {
                   $("#wiki").text("La suite sur Wikipédia"); /* Bind the link */
                } else {
                   $("#wiki").text("");
                }
                $this.button('reset'); /* Stop the loading animation */
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(function() {
    $('.btn').on('click', function() {
        $.ajax({
            url: '/answer',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var ans = JSON.parse(response);
                setTimeout(codeAddress(), 2000);
                $("#know_it").text(ans.know); /* Display the sentence relative to the address (@route.app /answer ) */
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

/* The next two functions are barely the same of the ones above except that they are executed when "enter" is pressed */

$(function() { /* Function that execute the script when the key "enter" is pressed */
$('#research').on('keypress', function(e) {
    if(e.which == 13) { /* 13 == enter */
        var $this = $('#submit');
        $this.button('loading');
        event.preventDefault();
        $.ajax({
            url: '/update_map',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var obj = JSON.parse(response);
                var audio = new Audio('/static/notif.wav');
                audio.play();
                $("#txtHint").text(obj.answer);
                $("#link").attr("href", obj.link);
                if (obj.link) {
                   $("#wiki").text("La suite sur Wikipédia");
                } else {
                   $("#wiki").text("");
                }
                $this.button('reset');
            },
            error: function(error) {
                console.log(error);
            },
        });
    }
});
});

$(function() { /* Function that execute the script when the key "enter" is pressed */
  $('#research').on('keypress', function(e) {
       if(e.which == 13) { /* 13 == enter */
           event.preventDefault();
           $.ajax({
               url: '/answer',
               data: $('form').serialize(),
               type: 'POST',
               success: function(response) {
                   console.log(response);
                   var ans = JSON.parse(response);
                   setTimeout(codeAddress(), 2000);
                   $("#know_it").text(ans.know);

               },
               error: function(error) {
                  console.log(error);
               },
           });
       }
  });
});
