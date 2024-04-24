#!/usr/bin/node
const request = require('request');

// Function that makes request and returns the parsed JSON object with Promise
function makeRequest(options) {
  return new Promise((resolve, reject) => {
    request(options, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          resolve(JSON.parse(body));
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}

const options = {
  headers: {
    'User-Agent': 'request'
  },
  url: process.argv[2]
};

async function check() {
  try {
    const films = await makeRequest(options);

    let count = 0;
    const characterPromises = [];
    for (const film of films.results) {
      for (const characterUrl of film.characters) {
        options.url = characterUrl;
        characterPromises.push(makeRequest(options));
      }
    }

    const characters = await Promise.all(characterPromises);

    for (const info of characters) {
      if (info.name === 'Wedge Antilles') {
        count++;
      }
    }
    console.log(count);
  } catch (error) {
    console.log(error);
  }
}

check();
