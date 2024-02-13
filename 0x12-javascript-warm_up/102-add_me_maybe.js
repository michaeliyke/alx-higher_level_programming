#!/usr/bin/node
module.exports = {
  addMeMaybe (num, cb) {
    num += 1;
    cb(num);
  }
};
