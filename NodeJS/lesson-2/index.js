// var generateName = require('sillyname');

import generateName from "sillyname";
import superheroes from "superheroes";

var sillyname = generateName();
var superHeroName = superheroes.random();

console.log(`my name is ${sillyname}`);
console.log(`my name is ${superHeroName}`);