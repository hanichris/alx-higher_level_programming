#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const cId = 18;

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const films = JSON.parse(body);
    const results = films.results.filter(
      film => film.characters.find(
        id => id.match(cId)));
    console.log(results.length);
  }
});
