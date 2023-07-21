#!/usr/bin/node

// Adding the ffilesystem Moule
const fSys = require('fs');

const fileA = fSys.readFileSync(process.argv[2]).toString();
const fileB = fSys.readFileSync(process.argv[3]).toString();
fSys.writeFileSync(process.argv[4], fileA + fileB);
