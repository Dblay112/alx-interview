#!/usr/bin/node


const request = require('request');

function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, function(error, response, body) {
        if (!error && response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const characters = movieData.characters;
            characters.forEach(function(characterUrl) {
                request(characterUrl, function(error, response, body) {
                    if (!error && response.statusCode === 200) {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                    } else {
                        console.log(`Failed to fetch character data: ${response.statusCode}`);
                    }
                });
            });
        } else {
            console.log(`Failed to fetch movie data: ${response.statusCode}`);
        }
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
