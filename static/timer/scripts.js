var clock = null;
var count = 0;

function setTime(total_centiseconds){
    var centiseconds = total_centiseconds % 100;
    var seconds = Math.floor(total_centiseconds / 100) % 60;
    var minutes = Math.floor(total_centiseconds / 6000);

    if (centiseconds < 10){
        centiseconds = '0' + centiseconds;
    }

    if (seconds < 10){
        seconds = '0' + seconds;
    }

    if (minutes < 10) {
        minutes = '0' + minutes;
    }

    $('#minutes').text(minutes);
    $('#seconds').text(seconds);
    $('#centiseconds').text(centiseconds);
}

function startTimer(){
    if (clock == null){
        clock = setInterval(function(){
            count = count + 1;
            setTime(count);
        }, 10);
    }
}

function stopTimer(){
    clearInterval(clock);
    clock = null;
}

$(document).ready(function(){
    $('#timer-page').addClass('active');
    setTime(count);

    $('.btn#start').click(function(){
        startTimer();
    });

    $('.btn#stop').click(function() {
        stopTimer();
    });

    $('.btn#reset').click(function(){
        stopTimer();

        count = 0;
        setTime(count);
    });

    $(window).keypress(function(e) {
        if (e.which === 32){
            // Space bar
            if (clock == null){
                startTimer();
            } else {
                stopTimer();
            }
        } else if (e.which === 13) {
            // Enter key
            // TODO: Submit time
            stopTimer();
            count = 0;
            setTime(count);
        }
    });
});