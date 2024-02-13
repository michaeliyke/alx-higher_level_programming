#!/usr/bin/node
exports.logMe = (function logMe () {
  let i = 0;

  return (s) => {
    console.log(`${i++}: ${s}`);
  };
}());
