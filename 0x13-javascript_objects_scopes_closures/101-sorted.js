#!/usr/bin/node

const { dict } = require('./101-data');
const obj = {};

/* For each object value, build array of  keys with same value */
for (const value of Object.values(dict)) {
  obj[value] = getRelatedKeysOf(value);
}

/* Gte all keys with a certain value */
function getRelatedKeysOf (value) {
  return (Object.keys(dict).filter((key) => dict[key] === value));
}

console.log(obj);
