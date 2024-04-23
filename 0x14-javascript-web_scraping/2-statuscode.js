#!/usr/bin/node
const request = require('request');

options = {
  headers: {
    'User-Agent': 'request'
  },
  url: process.argv[2]
};

request(options, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
