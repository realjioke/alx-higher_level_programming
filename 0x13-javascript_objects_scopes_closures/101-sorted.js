#!/usr/bin/node

const { dict } = require('./101-data');
const nDict = {};

Object.keys(dict).map((item, index) => {
  if (nDict[dict[item]] === undefined) {
    nDict[dict[item]] = [];
  }

  nDict[dict[item]].push(item);
  return index;
});

console.log(nDict);
