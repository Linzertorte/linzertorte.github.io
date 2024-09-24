var words = ["t","tableautin","tacite","tailleur","tambourin","tangage","tante","tapeur","tarder","tas","taurillon","teck","tele","teleski","temperance","tenable","tenace","tendrement","-","tennis","tente","terminaison","termite","terrasse","terreau","territoire","tete","tete-a-queue","texture","theoreme","thesauriseur","tien","timbre-poste","tiraillement","-","tiret","titillation","toc","tolee","-","tombereau","tondu","tonsure","tordu","torticolis","torve","touche-a-tout","touiller","tourbe","tourmentant","-","tournesol","-","tout-a-l'egout","toxicomanie","traditionalisme","tragiquement","traine","traitable","traitreusement","tranquille","transferer","transitaire","transpiration","transversalement","travailler","travers","traviole","tremblote","trepied","triage","tricorne","trio","tripotee","trois-mats","trop","troubadour","trousseau","trublion","tubercule","tunisien","tympan"]
const zeroPad = (num, places) => String(num).padStart(places, '0')
var cur_page = 0;
$("#btn").on("click", function (e) {
    var word =  document.getElementById("word").value;
    var i = 0;
    while(words.length && (words[i]=='-' || words[i]<=word)) {
        i+=1;
    }
    if(i>0) i-=1;
    while (i>=0 && words[i]=='-'){
        i-=1;
    }
    console.log(i)
    var html = "<img style=\"width:50%\" src=\"521847b4-fed0-4c33-932b-6552e94ac54d-"+zeroPad(i,4)+".png\">"
    cur_page = i;
    $("#page").html(html)
});
$("#prev").on("click", function (e) {
    if(cur_page>0) {
        cur_page -= 1;
        var html = "<img style=\"width:50%\" src=\"521847b4-fed0-4c33-932b-6552e94ac54d-"+zeroPad(cur_page,4)+".png\">"
        $("#page").html(html)
    }
});
$("#next").on("click", function (e) {
    if(cur_page<81){
        cur_page += 1;
        var html = "<img style=\"width:50%\" src=\"521847b4-fed0-4c33-932b-6552e94ac54d-"+zeroPad(cur_page,4)+".png\">"
        $("#page").html(html)
    }
});