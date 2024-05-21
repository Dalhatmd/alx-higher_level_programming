#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const link = process.argv[2];
const file = process.argv[3];

request(link, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonData = body;
  fs.writeFile(file, jsonData, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
