

$(function() {
    $(window).on('scroll', function() {
        if($(window).scrollTop() > 880) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
    });
});