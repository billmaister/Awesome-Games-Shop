/* global $ */
$(document).ready(function() {
  'use strict';
  var game_iframe = $("#game_iframe")[0]

  $(window).on('message', function(evt) {
    //Note that messages from all origins are accepted

    //Get data from sent message
    var data = evt.originalEvent.data;
    if (data.messageType == "SAVE"){
      $.ajax({
        url: game_iframe.getAttribute("save_url"),
        dataType: 'json',
        data: {
          'game_state': JSON.stringify(data.gameState)
        }
    });
    }
    else if (data.messageType == "LOAD_REQUEST"){
      $.ajax({
        url: game_iframe.getAttribute("load_url"),
        dataType: 'json',
        success: function (data) {
          // A response with LOAD and game state OR ERROR and info message is returned after load request
          if(data.messageType == "LOAD") {
            data.gameState = JSON.parse(data.gameState) // Convert gameState back to json format
          }
          game_iframe.contentWindow.postMessage(data, '*')
        }
      })
    }
    else if(data.messageType == "SCORE"){
      $.ajax({
        url: game_iframe.getAttribute("score_url"),
        dataType: 'json',
        data: {
          'score': data.score
        }
      })
    }
    else if(data.messageType == "SETTING") {
      //alert("received setting call: " + data.options.width + ", " + data.options.height)
      game_iframe.setAttribute("width", data.options.width)
      game_iframe.setAttribute("height", data.options.height)
    }
  });
});