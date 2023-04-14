#!/usr/bin/node

class Rectangle {
  constructor(width, height) {
    if (width >= 1 && height >= 1) {
      this.width = width;
      this.height = height;
    }
  }

  print() {
    const character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

