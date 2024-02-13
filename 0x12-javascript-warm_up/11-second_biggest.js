#!/usr/bin/node
const args = process.argv.slice(2);
let state = 1;

if (isNaN(args[0])) {
  state = 0;
}

if (isNaN(args[1])) {
  state = 0;
}

if (state === 1) {
  const ints = args.map((x) => parseInt(x));
  console.log(getOldMaxInt(ints));
} else {
  console.log(0);
}

function getOldMaxInt (ints) {
  let maxInt = Number.MIN_SAFE_INTEGER;
  let oldMaxInt;

  for (const int of ints) {
    if (int > maxInt) { /* Only chage maxInt if a lager int if found */
      oldMaxInt = maxInt !== Number.MIN_SAFE_INTEGER ? maxInt : undefined;
      maxInt = int; /* Only set oldMaxInt when maxInt is being set */
    }
  }
  return (oldMaxInt === undefined ? maxInt : oldMaxInt);
}
