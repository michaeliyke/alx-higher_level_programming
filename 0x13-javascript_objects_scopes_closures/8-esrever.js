#!/usr/bin/node
exports.esrever = function (list) {
  if (!Array.isArray(list)) return;
  const len = list.length;

  for (let left = 0, right = len - 1; left < right; left++, right--) {
    [list[left], list[right]] = [list[right], list[left]];
  }

  return (list);
};
