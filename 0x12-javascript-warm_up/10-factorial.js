#!/usr/bin/node
const args = process.argv.slice(2);

if (isNaN(args[0])) {
  console.log(1);
} else {
  console.log(fact(parseInt(args[0])));
}

function fact (x) {
  if (x === 1) {
    return (1);
  }
  return (x * fact(x - 1));
}
