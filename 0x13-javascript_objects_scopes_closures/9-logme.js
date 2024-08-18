#!/usr/bin/node
/**
 * LogMe - a function that prints the number of arguments already printed and the new argument value
 */
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);
  this.count++;
}
