function clean_word(word) {
    word = word.replaceAll("é","e");

    word = word.replaceAll("à","a");
    word = word.replaceAll("è","e");
    word = word.replaceAll("ù","u");

    word = word.replaceAll("ç","c");

    word = word.replaceAll("â","a");
    word = word.replaceAll("ê","e");
    word = word.replaceAll("î","i");
    word = word.replaceAll("ô","o");
    word = word.replaceAll("û","u");

    word = word.replaceAll("ë","e");
    word = word.replaceAll("ï","i");
    word = word.replaceAll("ü","u");

    word = word.replaceAll("’","'");
    word = word.toLowerCase();
    return word;
}

var words = [
    "t",
    "tableautin",
    "tacite",
    "tailleur","tambourin","tangage","tante","tapeur","tarder","tas","taurillon","teck","tele","teleski","temperance","tenable","tenace","tendrement","-","tennis","tente","terminaison","termite","terrasse","terreau","territoire","tete","tete-a-queue","texture","theoreme","thesauriseur","tien","timbre-poste","tiraillement","-","tiret","titillation","toc","tolee","-","tombereau","tondu","tonsure","tordu","torticolis","torve","touche-a-tout","touiller","tourbe","tourmentant","-","tournesol","-","tout-a-l'egout","toxicomanie","traditionalisme","tragiquement","traine","traitable","traitreusement","tranquille","transferer","transitaire","transpiration","transversalement","travailler","travers","traviole","tremblote","trepied","triage","tricorne","trio","tripotee","trois-mats","trop","troubadour","trousseau","trublion","tubercule","tunisien","tympan"]
const zeroPad = (num, places) => String(num).padStart(places, '0')
var cur_page = 0;
$("#btn").on("click", function (e) {
    var word =  document.getElementById("word").value;
    word = clean_word(word);
    var i = 0;
    for(i = 0; i < words.length; i += 1) {
        words[i] = clean_word(words[i]);
    }
    i = 0
    while(words.length && (words[i]=='-' || words[i]<=word)) {
        i+=1;
    }
    if(i>0) i-=1;
    while (i>=0 && words[i]=='-'){
        i-=1;
    }
    cur_page = i;
    var html = "<img style=\"width:50%\" src=\"larousse-"+zeroPad(cur_page + 1512,4)+".png\">"
    $("#page").html(html)
});
$("#prev").on("click", function (e) {
    if(cur_page > 0) {
        cur_page -= 1;
        var html = "<img style=\"width:50%\" src=\"larousse-"+zeroPad(cur_page + 1512,4)+".png\">"
        $("#page").html(html)
    }
});
$("#next").on("click", function (e) {
    if(cur_page < words.length - 1){
        cur_page += 1;
        var html = "<img style=\"width:50%\" src=\"larousse-"+zeroPad(cur_page + 1512,4)+".png\">"
        $("#page").html(html)
    }
});