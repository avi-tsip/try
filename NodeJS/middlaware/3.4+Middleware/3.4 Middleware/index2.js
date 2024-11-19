import express from "express";
import morgan from "morgan";

const app = express();
const port = 3000;

function logger (req, res, next) {
  console.log(`Request method:  ${req.method} and url is: ${req.url}`);
  res.sendStatus(201);
  next();
}

app.use(logger)

app.use(morgan("combined"))

app.get("/", (req, res) => {
  res.send("Hello");
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
