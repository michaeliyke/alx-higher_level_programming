const jQuery = $;

jQuery(function ($) {
  $('DIV#toggle_header').click(function () {
    const header = $('header');
    header.toggleClass('red green');
  });
});
