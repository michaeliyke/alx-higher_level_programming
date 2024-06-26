const jQuery = $;

jQuery(function ($) {
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then((response) => {
      const responsePromise = response.json();
      return responsePromise;
    }).then((res) => {
      $('DIV#character').text(res.name);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
