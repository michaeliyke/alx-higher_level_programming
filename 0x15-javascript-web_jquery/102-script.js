const jQuery = $;

jQuery(function ($) {

  $('INPUT#btn_translate').click(() => {
    let lang = $('INPUT#language_code').val();
    if (lang === '') {
      lang = 'en-US';
    }
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    // const url = `https://www.fourtonfish.com/hellosalut/hello?lang=${lang}/`;
    $.get(url, ({ hello }) => {
      $('DIV#hello').text(hello);
    });

  });

});
