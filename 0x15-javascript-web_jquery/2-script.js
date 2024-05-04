const jQuery = $;

jQuery(function ($) {
  $('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
