$("a").on("click", function (e) {
    e.preventDefault();
    $("a").removeClass("current");
    $(this).addClass("current");
    if(!$("#hamburger").is(":hidden")) {
        console.log("close!");
        closeNav();
        //$("#hamburger").show();
    }
    var collins = "https://www.collinsdictionary.com/dictionary/italian-english/";
    var word = $(this).text();
    $("#sent").html($(this).data("sent"));
    console.log(word);
    console.log($(this).data("sent"));
    $.get(collins+encodeURIComponent(word), function (data, s) {
        //var h = $(data).find("div.content.definitions.dictionary");
        var h = $(data).find("div.page");
        $("#dict-entry").html(h);
    });
    
});
function openNav() {
    console.log("with");
    document.getElementById("words").style.width = "100%";
}
  
function closeNav() {
    document.getElementById("words").style.width = "0";
}
$("#hamburger").on("click", function (e) {
    openNav();
});