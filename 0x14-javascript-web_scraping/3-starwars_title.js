#!/usr/bin/node
const request = require('request');

const options = {
  headers: {
    'User-Agent': 'request'
  },
  url: 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2]
};

request(options, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
