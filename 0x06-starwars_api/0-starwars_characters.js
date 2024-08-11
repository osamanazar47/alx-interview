#!/usr/bin/node
const request = require('request');
const APIUrl = 'https://swapi-api.hbtn.io/api/films';

if (process.argv.length > 2) {
  request(`${APIUrl}/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const characterUrl = JSON.parse(body).characters;
    const charactersName = characterUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allError => console.log(allError));
  });
}
