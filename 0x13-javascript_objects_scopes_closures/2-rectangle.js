#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h)) return;
    if (w < 1 || h < 1) return;

    this.width = w;
    this.height = h;
  }
};