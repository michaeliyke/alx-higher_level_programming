const jQuery = $;

jQuery(function ($) {
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then((response) => {
      const responsePromise = response.json();
      return responsePromise;
    }).then(({ results: movies }) => {
      for (const movie of movies) {
        $('UL#list_movies').append(`<li>${movie.title}</li>`);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
