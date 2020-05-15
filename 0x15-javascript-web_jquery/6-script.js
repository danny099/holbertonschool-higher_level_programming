#!/usr/bin/node
$('DIV#update_header').click(function () {
  $('header').replaceWith('New Header!!!<br>');
});
