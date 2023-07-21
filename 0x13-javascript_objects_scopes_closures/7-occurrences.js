#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  for (const member of list) {
    if (member === searchElement) number++;
  }

  return number;
};
