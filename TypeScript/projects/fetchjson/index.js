"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var axios_1 = require("axios");
var url = "https://jsonplaceholder.typicode.com/todos/1";
axios_1.default.get(url).then(function (res) {
    var todo = res.data;
    var ID = todo.ID;
    var title = todo.Title;
    var finished = todo.finished;
    console.log("\n        The todo with id: ".concat(ID, "\n        Has a title of: ").concat(title, "\n        Is it finished? - ").concat(finished, "\n        "));
});
