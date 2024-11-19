import express from "express";

const app = express();
const port = 3000;

app.listen(3000, () => {
    console.log(`Server is up and running!!! Listening on port: ${port}`);
});

app.get('/', (req, res) => {
    // res.send('Hello World!')
    // console.log(req.rawHeaders);
    //res.send(req.rawHeaders);
    res.send("<h1>hello</h1>");
  })

  app.get('/about', (req, res) => {
    // res.send('Hello World!')
    // console.log(req.rawHeaders);
    //res.send(req.rawHeaders);
    res.send("<h1>ABOUT</h1>");
  })

  app.post('/register', (req, res) => {
    res.sendStatus(201);
  })

  app.put('/replace', (req, res) => {
    res.sendStatus(200);
  })

  app.patch('/update', (req, res) => {
    res.sendStatus(202);
  })

  app.delete('/delete', (req, res) => {
    res.sendStatus(203);
  })