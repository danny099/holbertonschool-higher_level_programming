#!/usr/bin/node
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach(function (peli) {
    $('UL#list_movies').append('<li>' + peli.title + '</li>');
  });
});
