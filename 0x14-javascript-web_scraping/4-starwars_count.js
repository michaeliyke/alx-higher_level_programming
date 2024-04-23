#!/usr/bin/node
const request = require('request');

const options = {
  headers: {
    'User-Agent': 'request'
  },
  url: 'https://swapi-api.alx-tools.com/api/films/'
};

request(options, handler);

function handler (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
      // console.log(film.title);
    }
  }
  console.log(count);
}
