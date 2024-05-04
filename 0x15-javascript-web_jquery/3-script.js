const jQuery = $;

jQuery(function ($) {
  $('DIV#red_header').click(function () {
    const header = $('header');
    if (!header.hasClass('red')) {
      header.addClass('red');
    }
  });
});
