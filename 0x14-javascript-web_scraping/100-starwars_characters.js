#!/usr/bin/node
const request = require('request');

// Function that makes request and returns the parsed JSON object with Promise
function makeRequest (options) {
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
  url: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`
};

async function check () {
  try {
    const film = await makeRequest(options);

    const characterPromises = [];
    for (const characterUrl of film.characters) {
      options.url = characterUrl;
      characterPromises.push(makeRequest(options));
    }

    const characters = await Promise.all(characterPromises);

    for (const info of characters) {
      console.log(info.name);
    }
  } catch (error) {
    console.log(error);
  }
}

check();
