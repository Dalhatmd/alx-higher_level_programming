#!/usr/bin/node

const request = require('request');

const id = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  characters.forEach((character) => {
    request(character, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
