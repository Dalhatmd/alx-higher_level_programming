#!/usr/bin/node

const request = require('request');

const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < data.results.length; i++) {
      const characters = data.results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
