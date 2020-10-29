const express = require('express');

const app = express()

// Routes
app.get('/', (req,res) => {
    res.send('Hello world!');
});

// Start listening
app.listen(3000)