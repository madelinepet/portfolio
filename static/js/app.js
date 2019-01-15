

$( document ).ready(function() {
    var counter = 10;
    $(".frogicorn").click(function() {
        $(this).slideUp(100);
        counter -= 1;
        if (counter === 0) {
            $("#click").text("Good job!");
        }
    });
});
