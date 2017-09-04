class Solve {
  constructor(centiseconds){
    var d = new Date();
    this.date = d.getTime(); // unix timestamp
    this.centiseconds = centiseconds;
  }
}

var clock = null;
var count = 0;
times = [];

function ajax_prep() {
  var csrftoken = $('[name=csrfmiddlewaretoken]').val();

  function csrfSafeMethods(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethods(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
}

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
    ajax_prep();

    $('.btn#main').on('click', function(){
      if (clock == null) {
        startTimer();
        $(this).removeClass('btn-primary');
        $(this).addClass('btn-success');
        $(this).text('Done');
      } else {
        stopTimer();
        var solve = new Solve(count);
        times.push(solve);
        console.log(times);

        count = 0;
        setTime(count);
        $(this).removeClass('btn-success');
        $(this).addClass('btn-primary');
        $(this).text('Start');
      }

      $(this).blur();
    });

    $(window).keypress(function(e) {
        if (e.which === 32){  // space bar
          e.preventDefault();  // prevent scrolling
          $('.btn#main').click();
        }
    });

    $('.btn#save').on('click', function(){
      if (!$(this).hasClass('disabled')){
        console.log('save');
      }

      $(this).removeClass('disabled');

      $(this).blur();  // prevent from triggering on pressing space
    });

    $('.btn#delete').on('click', function(){
      if (!$(this).hasClass('disabled')) {
        console.log('delete');
      }

      $(this).removeClass('disabled');

      $(this).blur();
    });

});
