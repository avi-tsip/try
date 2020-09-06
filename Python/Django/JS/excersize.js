var keepScore = 0

alert('Welcome to my site. Let me ask you some questions')
var firstName = prompt('What is your first name? ')
var lastName = prompt('What is your last name ')

if (firstName[0] === lastName[0]) {
    keepScore++
}
console.log('The score is: ' + keepScore)
var age = prompt('What is your age? ')

if (age > 20 && age < 30) {
    keepScore++
}
console.log('The score is: ' + keepScore)
var height = prompt('What is your height in cm? ')

if (height > 170) {
    keepScore++
}
console.log('The score is: ' + keepScore)
 var petName = prompt('What is your pets name? ')

 if (petName[petName.length - 1] === "y") {
     keepScore++
 }
 console.log('The score is: ' + keepScore)

 if (keepScore === 4) {
     console.log('שתי גדות לירדן. זו שלנו זו גם כן')
 }
 else {
     console.log('Hater')
 }

