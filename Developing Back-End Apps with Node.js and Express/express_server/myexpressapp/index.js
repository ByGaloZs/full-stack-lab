// Import the Express.js library
const express = require('express');

// Create an instance of an Express application
const app = new express();

// Define the root route to send a welcome message
app.get('/', (req, res) => {
    res.send('Welcome to my own Express server!');
});

// Start the server and listen on port 3111
app.listen(3111, () => {
    console.log('Server is running on http://localhost:3111');
});