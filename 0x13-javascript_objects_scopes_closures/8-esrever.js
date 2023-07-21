#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (const member of list) {
    revList.unshift(member);
  }

  return revList;
};
