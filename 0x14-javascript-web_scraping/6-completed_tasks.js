#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) console.log(err);
  else {
    const jsonData = JSON.parse(body);
    const userIDs = [...new Set(jsonData.map(entry => entry.userId))];
    const completeTasks = {};

    userIDs.forEach(id => {
      const tasks = jsonData.filter(task => task.userId === id && task.completed);
      if (tasks.length > 0) completeTasks[id] = tasks.length;
    });
    console.log(completeTasks);
  }
});
