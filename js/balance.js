$(document).ready(function() {
    alert("Hi")
    $(".qnt").click(function() {
        val = $(this).attr("value");
        alert(val);
    });
});