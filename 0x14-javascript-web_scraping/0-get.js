#!/usr/bin/node
const request = require('request');
const url = 'https://api.github.com/users/octocat';
options = {
  headers: {
    'User-Agent': 'request'
  },
  url: url
};
request(options, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
    console.log(body);
  }
});
