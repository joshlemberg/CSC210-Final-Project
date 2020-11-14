$(document).ready(function() {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('#navigation').css('background', 'white');
        } else {
            $('#navigation').css('background', 'black');
        }
    });
});