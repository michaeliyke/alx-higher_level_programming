#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c) {
      this.printChar = c;
    }
    this.print();
  }
};
