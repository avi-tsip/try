import express from "express";

const app = express();
const port = 3000;

var message = '';

const day = new Date();
const today = day.getDay();

function createMessage(req, res, next) {
    if (today === 0 || today === 6) {
        message = "Hey It's a weekend, it's time to have fun";
    } else {
        message = "Hey It's a weekeday, it's time to work hard";
    }
    next();
}

console.log(today);

app.use(createMessage);

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
  });

app.get("/", (req, res) => {
    res.render("index.ejs", {message: message});
 });
