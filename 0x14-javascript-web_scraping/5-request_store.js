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

  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}
