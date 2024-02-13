#!/usr/bin/node
module.exports = {
  callMeMoby (number, cb) {
    if (typeof number !== 'number') return;

    for (let i = 0; i < number; i++) {
      cb();
    }
  }
};
