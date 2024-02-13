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
  let oldMaxInt = Number.MIN_SAFE_INTEGER;

  for (const int of ints) {
    if (int > maxInt) { /* Only chage maxInt if a lager int if found */
      oldMaxInt = maxInt;
      maxInt = int; /* Only set oldMaxInt when maxInt is being set */
    } else if (int > oldMaxInt && int !== maxInt) {
      /* Here int is half-way between both */
      oldMaxInt = int;
    }
  }
  return (oldMaxInt === maxInt ? undefined : oldMaxInt);
}
