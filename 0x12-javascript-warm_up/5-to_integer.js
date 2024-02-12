#!/usr/bin/node
const args = process.argv.slice(2);
const value = isNaN(args[0]) ? 'Not a number' : parseInt(args[0]);

console.log(`My number: ${value}`);
