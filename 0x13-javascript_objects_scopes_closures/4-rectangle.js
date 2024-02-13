#!/usr/bin/node
module.exports = class Rectangle {
  printChar = 'X';
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) return;
    if (w < 1 || h < 1) return;

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let width = '';

      for (let j = 0; j < this.width; j++) {
        width += this.printChar;
      }

      console.log(width);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
