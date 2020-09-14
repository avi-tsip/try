$('h1').click(function(){
    console.log('there was a click');
    $(this).text("I was changed");

});

$('li').click(function() {
    console.log('I clicked on any li item');
});

//toggle the class on every key stroke of the keyboard
$('input').eq(0).keypress(function(event) {
    $('h3').toggleClass('turnBlue');
    console.log(event);
});

//do something only when a enter key is pressed
$('input').eq(0).keypress(function(event) {
    if (event.which === 13) {
        $('h3').toggleClass('turnRed');
    }
});

//on method - acts like addeventlistner
// $('h2').on('dblclick', function() {
//     $(this).toggleClass('turnRed');
// });

//do something when mouse enters
$('h2').on('mouseenter', function() {
    $(this).toggleClass('turnRed');
});

//Effects
$('input').eq(1).on('click', function() {
    $('.container').fadeOut(2000);
});
