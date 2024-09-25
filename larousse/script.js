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
    "a",
    "abandon",
    "abattement",
    "abdomen",
    "ablette",
    "abonner",
    "aboutissants",
    "abricotier",
    "abside",
    "absoudre",
    "absurdité",
    "académisme",
    "accélérateur",
    "accepter",
    "accessoirement",
    "accointances",
    "accomplissement",
    "accouchement",
    "accrocheur",
    "acculer",
    "acerbe",
    "achoppement",
    "acquérir",
    "acrobatie",
    "actinie",
    "activisme",
    "adaptation",
    "adhésif",
    "admettre",
    "admirer",
    "adorateur",
    "adroit",
    "adverse",
    "aérospatial",
    "affairé",
    "affectif",
    "affichette",
    "affligeant",
    "affréter",
    "africaniser",
    "agenda",
    "agile",
    "agneau",
    "agréablement",
    "agricole",
    "aide-mémoire",
    "aigu",
    "ailé",
    "aîné",
    "airain",
    "aisément",
    "alanguissement",
    "alentour",
    "aliénant",
    "aliter",
    "-",
    "allergie",
    "allonger",
    "allusion",
    "alphanumérique",
    "alto",
    "amateurisme",
    "ambre",
    "amender",
    "américanisation",
    "amidonnage",
    "amoralisme",
    "amourette",
    "ampoule",
    "anacarde",
    "ananas",
    "anciennement",
    "ânesse",
    "anglo-saxon",
    "animosité",
    "annexion",
    "annuité",
    "antagoniste",
    "anthropométrique",
    "antidémocratique",
    "antipodiste",
    "anus",
    "aperçu",
    "aplatissement",
    "apostropher",
    "apparenter",
    "appauvrissement",
    "appendicite",
    "appoint",
    "appréhension",
    "approchant",
    "approprier",
    "âpre",
    "après-midi",
    "arable",
    "arcanes",
    "architecturer",
    "argenté",
    "aristocratie",
    "armistice",
    "arracheur",
    "arrhes",
    "arrière-pensée",
    "arroger",
    "artériel",
    "artificiellement",
    "ascète",
    "aspirant",
    "assassinat",
    "asservissement",
    "assiettée",
    "assistant",
    "assommer",
    "assouvissement",
    "assureur",
    "astronaute",
    "atmosphère",
    "atrophié",
    "attaquant",
    "attelage",
    "attentatoire",
    "attiédir",
    "attrape",
    "aubade",
    "audiovisuel",
    "aulne",
    "aussitôt",
    "autarcie",
    "autocritique",
    "automobile",
    "autoroute",
    "autrefois",
    "autrichien",
    "avaliser",
    "avanie",
    "avantageux",
    "avatar",
    "aventuré",
    "aveuglant",
    "avilissant",
    "avoine",
    "axer",
    "b",
    "bacillaire",
    "bafouilleur",
    "baguer",
    "bailleur",
    "bajoue",
    "balancer",
    "baldaquin",
    "ballonné",
    "banal",
    "bandelette",
    "banqueroute",
    "baraqué",
    "barboteuse",
    "baronne",
    "barricade",
    "basalte",
    "bas-fond",
    "bas-ventre",
    "batifolage",
    "batte",
    "bauge",
    "bazarder",
    "beaucoup",
    "bécane",
    "bel",
    "bénéfice",
    "benoîtement",
    "bermuda",
    "bétail",
    "beurre",
    "biblique",
    "bien-aimé",
    "bienfaiteur",
    "bienvenu",
    "bigler",
    "bilinguisme",
    "biparti",
    "bistré",
    "blaguer",
    "blanc-bec",
    "blé",
    "bleuâtre",
    "blondeur",
    "bobiner",
    "boisé",
    "bombardier",
    "bonasse",
    "bonhomie",
    "bonus",
    "borgne",
    "botter",
    "boucherie",
    "bouddhique",
    "bougainvillée",
    "bouilloire",
    "bouleversement",
    "bourdon",
    "bourreau",
    "boursouflure",
    "boutade",
    "boutonnière",
    "braguette",
    "brandy",
    "brasero",
    "bravo",
    "brève",
    "bridger",
    "brimade",
    "brise-tout",
    "broderie",
    "brouiller",
    "bruit",
    "brumaire",
    "brutalité",
    "buissonneux",
    "bureaucratiser",
    "butiner", 
]
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
    var html = "<img src=\"larousse-"+zeroPad(cur_page + 1,4)+".png\">"
    $("#page").html(html)
});
$("#prev").on("click", function (e) {
    if(cur_page > 0) {
        cur_page -= 1;
        var html = "<img src=\"larousse-"+zeroPad(cur_page + 1,4)+".png\">"
        $("#page").html(html)
    }
});
$("#next").on("click", function (e) {
    if(cur_page < words.length - 1){
        cur_page += 1;
        var html = "<img src=\"larousse-"+zeroPad(cur_page + 1,4)+".png\">"
        $("#page").html(html)
    }
});