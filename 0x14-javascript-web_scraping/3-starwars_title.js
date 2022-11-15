#!/usr/bin/node

const request = require('request');

let url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const api = url + id;

request(api, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
