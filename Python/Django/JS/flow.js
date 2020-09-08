// // if statements

// if (condition) {
//     // is true - execute this code;
// }
// else if(condition){
//     // is true - execute this code;
// }
// else {
//     //if prevoius conditions, didn't match, run this code;
// }

// // while loop

// while (condition) {
//     //execute while condition is true
//     //you can break from the loop by using the break key word
//     //
// }

// //for loops

// for (var i = 0; i < 5; i++) {
//     //execute code
// }

// //functions

// function firstFunction(param1, param2="defaultValue") {
//     //code to execute
//     //return or not a value with the key word return
// }

//Arrays

var exampleArray = ['avi', 'tali', 'etc']

//Accessing array elements

exampleArray[1]

//Assigning elemets

exampleArray[2] = 'moshe'

//Remove the last item in the array

exampleArray.pop()

console.log(exampleArray)

//Insert an element at the end of the array

exampleArray.push('baruch')

console.log(exampleArray)

//Iterating over arrays

for (var i = 0; i < exampleArray.length; i++){
    console.log(exampleArray[i])
}

for (name of exampleArray) {
    console.log(name)
}

exampleArray.forEach(console.log);

function isAwesome (name) {
    console.log(name + " is aswesome!")
}

exampleArray.forEach(isAwesome)

//Objects

var carInfo = {make: "Toyota", year: 1990, model: "Camry", list:[1,2,3], dict: {inside:['a','b']}}

//get a value

console.log(carInfo["make"])

console.log(carInfo["list"][2])

console.log(carInfo["dict"]['inside'][0])

//Change a value

carInfo['year'] = 2000

console.log(carInfo)
    
//Iterating over an object

for (key in carInfo) {
    console.log(carInfo[key])
}

//you can call a function from one of the values in the object

carInfo['theif'] = function() {alert('the car is being stolen')}

carInfo.theif()

//Using the this key word

var myObj ={
    name: 'avi',
    greet: function(){
        console.log('hello ' + this.name)
    }
}

myObj.greet()