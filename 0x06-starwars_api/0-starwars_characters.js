#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacter (characters, index) {
  if (characters.length === index) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      getCharacter(characters, index + 1);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    getCharacter(characters, 0);
  }
});
