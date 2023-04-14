#!/usr/bin/node

// Define a class named Rectangle with a constructor that takes width and height arguments
class Rectangle {
  constructor(width, height) {
    // Check if the width and height arguments are both greater than or equal to 1
    if (width >= 1 && height >= 1) {
      // If they are, assign them to instance properties
      this.width = width;
      this.height = height;
    }
  }
}

// Export the Rectangle class so it can be used in other modules
module.exports = Rectangle;

