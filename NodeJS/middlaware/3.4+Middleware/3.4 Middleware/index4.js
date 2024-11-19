import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import bodyParser from "body-parser";
const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const port = 3000;
var bandName = "";

function bandNameGenerator(req, res, next) {
  console.log(req.body);
  bandName = req.body["pet"] + req.body.street;
  next();
}

app.use(bodyParser.urlencoded({extended: true}));

app.use(bandNameGenerator);

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/submit", (req, res) => {
  res.send(`<h1>Your band name is:</h1>\n ${bandName} &#128525`);
});
