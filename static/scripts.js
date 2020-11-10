$(document).ready(function() {
	var i = 0;
	var txt = "his is an example of a typing effect";
	var speed = 50;

	$("#typingeffect").click(function(event) {
		while (i < txt.length) {
			var newHTML = $("#testheader").html() + txt.charAt(i);
			console.log($("#testheader").html());
			console.log(txt.charAt(i));
			console.log("i = " + i);
    		$("#testheader").html(newHTML);
    		++i;
    		// setTimeout(typeWriter, speed);
  		}
	});


	$("#addbutton").click(function(event) {
		$("#testheader").html("This is a test");; // Uses jQuery selector :hidden, referenced from https://api.jquery.com/hidden-selector/, and .first() referenced from https://api.jquery.com/first-selector/
		return false;
	});

    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('#navigation').css('background', 'white');
        } else {
            $('#navigation').css('background', 'black');
        }
    });
});