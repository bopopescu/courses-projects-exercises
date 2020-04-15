// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addName(name) {
  var name = prompt("Please enter name to add it to the list: ");
  roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript

function removeName(name) {
  var name = prompt("Please enter name to remove it from the list: ")

  const index = roster.indexOf(name);
  if (index > -1) {
  roster.splice(index, 1);
  };
};
// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
  console.log(roster);
}

// Start by asking if they want to use the web app
var answer = prompt("Welcome! Are you ready to begin? y/n: ")
while (answer == "y") {
  var action = prompt("What you want to do? add/remove/display/quit: ")
  if (action == "add") {
    addName()
  }
  else if (action == "remove") {
    removeName()
  }
  else if (action == "display") {
    display()
  }
  else if (action == "quit") {
    break
  }
}
alert("Thank you for using web app! Please refres page to start over")
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
