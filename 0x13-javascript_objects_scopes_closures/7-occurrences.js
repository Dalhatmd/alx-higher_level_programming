#!/usr/bin/node
/**
 * count the number of occurences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return count;
}
