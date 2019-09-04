$(document).ready(function() {
    var player = document.getElementById('audio-player');
    var slider = document.getElementById("myRange");
    var rate = document.getElementById("rate");
    var rate_o = document.getElementById("trate");
    var output = document.getElementById("demo");
    var nob = document.getElementById("nob");
    var on = true;
    var total = $('tr').length;
    output.innerHTML = slider.value;
    function frac(val) {
        val = parseInt(val);
        return val/10;
    }
    slider.oninput = function() {
        output.innerHTML = this.value;
    }
    rate_o.innerHTML = frac(rate.value)
    rate.oninput = function () {
        rate_o.innerHTML = frac(this.value);
        player.playbackRate = frac(this.value);
    }
    $('tr').click(function() {
        play(player, this.id)
    });

    function play(player, id) {
        var tr = $('#' + id);
        $('table tr').css('background', 'white');
        tr.css('background', '#E8E8E8');
        var start = tr.attr('data-start');
        var end = tr.attr('data-end');
        player.currentTime = start;
        player.play();
        player.ontimeupdate = function() {
            if (player.currentTime >= end) {
                player.pause();
            }
        };
    }

    function replay(p_no, cnt) {
        if (!on) return;
        if (cnt > slider.value) cnt = 1, p_no++;
        if (p_no > total) p_no = 1;
        tr = $('#p' + p_no);
        var start = tr.attr('data-start');
        var end = tr.attr('data-end');
        player.currentTime = start;
        player.play();
        player.ontimeupdate = function() {
            if (player.currentTime >= end) {
                player.pause();
                replay(p_no, cnt + 1);
            }
        };
    }
    $('#nob').change(function() {
        if (nob.checked) {
            on = true;
            replay(1, 1);
        } else {
            on = false;
        }
    });
});
