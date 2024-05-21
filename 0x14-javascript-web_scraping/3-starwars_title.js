#!/usr/bin/node

const request = require('request');

const link = `https://swapi-api.alx-tools.com/api/films/${parseInt(process.argv[2])}`;

request(link, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonData = JSON.parse(body);
  console.log(jsonData.title);
});
