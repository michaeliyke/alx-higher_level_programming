const jQuery = $;

jQuery(function ($) {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      const responsePromise = response.json();
      return responsePromise;
    }).then(({ hello }) => {
      $('DIV#hello').text(hello);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
