$("a").on("click", function (e) {
    e.preventDefault();
    $("a").removeClass("current");
    $(this).addClass("current");
    $.get($(this).attr("href"), function (data, s) {
        var h = $(data).find("div.dictionaries.dictionary");
        $("#entry").html(h);
    });
});