#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const url = args[0];
const filePath = args[1];

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
