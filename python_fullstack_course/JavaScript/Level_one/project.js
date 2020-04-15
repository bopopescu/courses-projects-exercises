var first = prompt("Hello, please enter your first name: ");
var last = prompt("Enter your last name: ");
var age = prompt("What is your age?");
var tall = prompt("How tall are you?");
var pet = prompt("Waht is the name of your pet?");
var lastchar = pet[pet.length - 1];
alert('Thank you for answers!!!');


if (first[0]===last[0] && 20 <= age && age >= 30 && tall>=170 && lastchar === "y") {
  console.log("Welcome Commrade!");
} else {
  console.log("Nothing to see here!");
}
