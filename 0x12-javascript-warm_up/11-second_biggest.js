#!/usr/bin/node

const argS = process.argv.slice(2);
if (argS.length < 2) {
  console.log(0);
} else {
  for (let i = 0; i < argS.length; i++) argS[i] = Number(argS[i]);

  let biggest;
  let secBiggest;

  if (argS[0] >= argS[1]) {
    biggest = argS[0];
    secBiggest = argS[1];
  } else {
    biggest = argS[1];
    secBiggest = argS[0];
  }

  for (let i = 2; i < argS.length; i++) {
    if (argS[i] > biggest) {
      secBiggest = biggest;
      biggest = argS[i];
    } else if (argS[i] > secBiggest && argS[i] < biggest) {
      secBiggest = argS[i];
    }
  }

  console.log(secBiggest);
}
