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
  url: 'https://jsonplaceholder.typicode.com/todos',
  method: 'GET'
};

const completedTasks = {};

async function check() {
  try {
    for (const todo of await makeRequest(options)) {
      const uid = String(todo.userId);
      if (todo.completed) {
        increment(uid);
      } else if (!(uid in completedTasks)) {
        completedTasks[uid] = 0;
      }
    }
  } catch (error) {
    console.log(error);
  }

}

// Function that increments the completed tasks for the user
function increment(uid) {
  if (uid in completedTasks) {
    completedTasks[uid]++;
  } else {
    completedTasks[uid] = 1;
  }
}


check().then(() => {
  console.log(completedTasks);
}).catch((error) => {
  console.log(error);
});
