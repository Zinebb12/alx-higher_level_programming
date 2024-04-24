#!/usr/bin/node

const fs = require('fs');
const arg1 = process.argv[2];
const arg2 = process.argv[3];

fs.writeFile(`${arg1}`, arg2, 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});
