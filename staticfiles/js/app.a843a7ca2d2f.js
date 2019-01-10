

// $( document ).ready(function() {
//     $("#projects").hide();
//     $("#game").hide();
// });

// $("#projlink").click(function() {
//     $("#projects").show();
//     $("#about").slideUp();
//     $("#game").slideUp();
// });

// $("#home").click(function() {
//     $("#about").show();
//     $("#projects").slideUp();
//     $("#game").slideUp();
// });

// $("#game-link").click(function() {
//     $("#game").show();
//     $("#about").slideUp();
//     $("#projects").slideUp();
// });

var counter = 10;
$(".frogicorn").click(function() {
    $(this).slideUp(100);
    counter -= 1;
    console.log(counter);
    if (counter === 0) {
        $("#click").text("Good job!");
    }
});