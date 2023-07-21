#!/usr/bin/node

const argNoPath = process.argv.slice(2);
const num = Number(argNoPath[0]);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
