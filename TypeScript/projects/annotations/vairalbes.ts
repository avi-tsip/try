// var annotations
let apples: number = 5;

apples = 'asdfasdfasd';

let speed: string = 'yes';
let isYes: boolean = true;
let nothing: null = null;
let notExist: undefined = undefined;

// object
let now: Date = new Date();

// array
let colors: string[] = ['red', 'blue']

//classes
class Car {

}

let car: Car = new Car()

//object literal
let point: {x: number, y: number} = {
    x:10,
    y:20
}

// functions
const logNumber: (i: number) => void = (i: number) => {
    console.log(i)
    return 'yes';
};

//When to use annotations
// 1 - Functions that returns the 'any' type
const json = '{"x": 10, "y": 20}';
const coordinates = JSON.parse(json); // json.parse can't guess the type of the value so it will return an 'any' type.
console.log(coordinates); // When the type is 'any' -> typescript can't do its job and check for issues
// The solution is to add annotation as we done on line 24 - 28

// 2 - wheb we declare a var on one line and initialize it later on
let words = ['red', 'green', 'blue'];
let foundWord: boolean; // The best way was to initialize the var, but if we decided not to - give it an annotation

for (let index = 0; index < words.length; index++) {
    if (words[index] === 'green') 
    {
        foundWord = true;
    }
}

// 3 - When we want a var to have a type that can't be inferred
let numbers = [-1, -12, 13];
let numberAboveZero: boolean | number = false;

for (let index = 0; index < words.length; index++) {
    if (numbers[index] > 0) {
        numberAboveZero = numbers[index];
    }
}
