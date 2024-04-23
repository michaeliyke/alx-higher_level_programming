#!/usr/bin/node
// Read and print the content of a file.
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
