#!/usr/bin/node
const args = process.argv.slice(2);
const [file1, file2, file3] = args;
const fs = require('fs');

if (file1 && file2 && file3) {
  fs.readFile(file1, (err, data) => {
    if (err) {
      return;
    }

    fs.readFile(file2, (err, data2) => {
      if (err) {
        return;
      }

      const allData = data + data2;

      fs.writeFile(file3, allData, 'utf-8', () => { });
    });
  });
}
