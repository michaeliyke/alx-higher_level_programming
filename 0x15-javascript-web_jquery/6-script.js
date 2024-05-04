const jQuery = $;

jQuery(function ($) {
  let count = 0;

  $('DIV#update_header').click(function () {
    if (count++ >= 1) {
      return;
    }
    $('HEADER').text('New Header!!!');
  });
});
