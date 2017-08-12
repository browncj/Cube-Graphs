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

$(document).ready(function(){
    $('#timer-page').toggleClass('active');
    setTime(count);

    $('.btn#start').click(function(){
        if (clock == null){
            clock = setInterval(function(){
                count = count + 1;
                setTime(count);
                }, 10);
        }
    });

    $('.btn#stop').click(function() {
        clearInterval(clock);
        clock = null;
    });

    $('.btn#reset').click(function(){
        clearInterval(clock);
        clock = null;
        count = 0;
        setTime(count);
    });
});