#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonData = body;
  const tasks = JSON.parse(jsonData);
  const completedTasks = {};
  for (const task of tasks) {
    if (task.completed === true) {
      if (task.userId in completedTasks) {
        completedTasks[task.userId] += 1;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
