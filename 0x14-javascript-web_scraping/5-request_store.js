#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const options = {
  headers: {
    'User-Agent': 'request'
  },
  url: process.argv[2]
};

request(options, handler);

function handler (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile('store', body, (err) => {
    if (err) {
      console.error(err);
    }
  });
}
