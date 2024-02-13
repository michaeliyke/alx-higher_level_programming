#!/usr/bin/node
exports.converter = function converter (base) {
  return (x) => {
    return (Number(x).toString(base));
  };
};
