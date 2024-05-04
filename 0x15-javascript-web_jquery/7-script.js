const jQuery = $;

jQuery(function ($) {
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then((response) => {
      const response_promise = response.json();
      return response_promise;
    }).then((res) => {
      $('DIV#character').text(res.name);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
