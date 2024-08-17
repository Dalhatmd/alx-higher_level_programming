#!/usr/bin/node
/**
 * Square class that defines a square
 */
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
