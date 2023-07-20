#!/usr/bin/node

const argNoPath = process.argv.slice(2);
const num = Number(argNoPath[0]);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(num));
