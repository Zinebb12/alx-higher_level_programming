#!/usr/bin/node

const fs = require('fs');
const arg1 = process.argv[2];

fs.readFile(`${arg1}`, 'utf8', function (err, data) {
  console.log(data);

  if (err) {
    console.error(err);
  }
});
