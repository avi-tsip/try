// const prompt=require("prompt-sync")({sigint:true});

// function findLeapYear(year) {
//     if (year % 4 === 0) 
//     {
//         if (year % 100 !== 0) {
//             console.log("the " + year + " is a leap year");
//         }
//         else {
//             if (year % 400 === 0) {
//                 console.log("the " + year + " is a leap year");
//             }
//             else {
//                 console.log("the " + year + " is NOT a leap year");
//             }
//         }
//     }
//     else {
//         console.log("the " + year + " is NOT a leap year");
//     }
// }

// console.log(findLeapYear(4024))

// var guestList = ["me", "myself", "I", "danny", "moshe"]

// function findGuest() {
//     let guest = prompt("what is your name?");
//     if (guestList.includes(guest)) {
//         console.log("welcome!")
//     } else {
//         console.log("you are not on the guest list")
//     }
// }

// findGuest()

// numsArray = []
// count = 1

// function fizzBuzz() {
//     while (numsArray.length < 100) {
//         if (count % 3 === 0 && count % 5 === 0){
//             numsArray.push("fizzBuzz");
//         }
//         else if (count % 3 === 0) {
//             numsArray.push('fizz');
//         }
//         else if (count % 5 === 0) {
//             numsArray.push('buzz');
//         }
//         else {
//             numsArray.push(count);
//         }
//         count++
//     }
//     console.log(numsArray)
// }

// fizzBuzz()

justNums = [1, 2, 3, 4, 5, 6]
for (let x of justNums) {
    console.log(x)
}