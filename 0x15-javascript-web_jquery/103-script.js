const jQuery = $;

jQuery(function ($) {
  $('INPUT#btn_translate').click(translate);

  $(document).keypress((event) => {
    if (event.which === 13) {
      $('INPUT#btn_translate').trigger('click');
    }
  });
});

function translate () {
  let lang = $('INPUT#language_code').val();
  if (lang === '') {
    lang = 'en-US';
  }
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
  $.get(url, ({ hello }) => {
    $('DIV#hello').text(hello);
  });
}
