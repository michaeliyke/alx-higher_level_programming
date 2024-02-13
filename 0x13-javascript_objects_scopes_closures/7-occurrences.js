#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;

  for (const item of list) {
    if (item === searchElement) occ++;
  }

  return (occ);
};
