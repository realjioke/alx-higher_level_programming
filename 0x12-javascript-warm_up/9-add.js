#!/usr/bin/node

const argNoPath = process.argv.slice(2);
const numA = Number(argNoPath[0]);
const numB = Number(argNoPath[1]);

function add (a, b) {
  return (a + b);
}

console.log(add(numA, numB));
