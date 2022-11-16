#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmID}`;

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const films = JSON.parse(body);
    const characters = films.characters;
    characters.forEach(url => {
      request(url, (err, resp, body) => {
        if (err) console.log(err);
        else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
