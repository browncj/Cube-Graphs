class Solve {
  constructor(centiseconds, scramble){
    var d = new Date();
    this.date = d.getTime(); // unix timestamp
    this.centiseconds = centiseconds;
    this.scramble = scramble;
  }
}

var clock = null;
var count = 0;
times = [];

$(document).ready(function(){
  $('#timer-page').addClass('active');
  updateDisplay();
  setTime(count);
  ajax_prep();

  $('.btn#main').on('click', function(){
    if (clock == null) {
      startTimer();
      $(this).removeClass('btn-primary');
      $(this).addClass('btn-success');
      $(this).text('Done');
    } else {
      var scramble = $('p.scramble').text().trim();
      stopTimer();
      var solve = new Solve(count, scramble);
      times.push(solve);
      updateDisplay();

      // update scramble
      $.get( 'scramble/', function(data) {
        $('.scramble').text(data);
      });

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
    var post_data = {'times': times};
    var post_data_string = JSON.stringify(post_data);
    $.ajax({
      type: "POST",
      url: 'submit/',
      data: post_data_string,
      statusCode: {
        204: function(response) {
          times = [];
          updateDisplay();
        },
        404: function(response) {
          $('#login_modal').modal('show');
        },
      },
    });

    $(this).blur();  // prevent from triggering on pressing space
  });

  $('.btn#delete').on('click', function(){
    // delete local data
    times = [];
    updateDisplay();
    $(this).blur();
  });
});

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


function formatTime(total_centiseconds){
    var centiseconds = total_centiseconds % 100;
    var seconds = Math.floor(total_centiseconds / 100) % 60;
    var minutes = Math.floor(total_centiseconds / 6000);

    if (centiseconds < 10)
        centiseconds = '0' + centiseconds;

    if (seconds < 10)
        seconds = '0' + seconds;

    if (minutes < 10)
        minutes = '0' + minutes;

    return minutes + ':' + seconds + ':' + centiseconds;
}

function setTime(total_centiseconds){
  $('#time').text(formatTime(total_centiseconds));
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

function updateDisplay() {
  $('#pending').html(times.length);
  $('#times-list').html('');

  var max = times.length <= 4 ? times.length : 4;
  var highlight;

  // each time keeps same level of highlighting as it descends the list
  if (times.length % 3 == 0)
    highlight = 0;
  else if (times.length % 3 == 1)
    highlight = 1;
  else
    highlight = 2;

  for (var i = 0; i < max; i++){
    var html = '<button type="button" class="list-group-item highlight">';

    // cycle through highlight intensities
    var html;
    if (highlight == 0)
      html = '<button type="button" class="list-group-item">';
    else if (highlight == 1)
      html = '<button type="button" class="list-group-item highlight1">';
    else
      html = '<button type="button" class="list-group-item highlight2">';
    
    highlight = highlight > 0 ? highlight - 1 : 2;

    html += formatTime(times[times.length-i-1].centiseconds);
    html += '</button>';
    $('#times-list').append(html);
  }
}
