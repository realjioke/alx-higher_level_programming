#!/usr/bin/node

const argNoPath = process.argv.slice(2);
const num = Number(argNoPath[0]);

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
