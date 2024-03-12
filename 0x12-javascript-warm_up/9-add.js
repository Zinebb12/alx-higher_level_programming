#!/usr/bin/node

function add (a, b) {
  const x = a + b;
  console.log(x);
}

add(Number(process.argv[2]), Number(process.argv[3]));
