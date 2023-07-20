#!/usr/bin/node

const argL = process.argv.slice(2);
const argA = argL[0];
const argB = argL[1];

const argConcat = argA + ' is ' + argB;

console.log(argConcat);
