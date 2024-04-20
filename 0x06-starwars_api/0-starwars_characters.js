#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

function req (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, async (error, res, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const result = await req(character);
    console.log(result);
  }
});
