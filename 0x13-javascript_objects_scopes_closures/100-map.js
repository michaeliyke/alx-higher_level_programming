#!/usr/bin/node

const { list } = require('./100-data');

const list2 = list.map((element, index) => {
  return (element * index);
});

console.log(list);
console.log(list2);
