function hello(){
  console.log("Hello World!");
}


function helloYou(name){
  console.log("Hello "+name);
}


function addNum(num1,num2) {
  console.log(num1+num2);
}

//if we wont get a name as a input,
//we can set up our default name - Frankie in this case!
function helloSomeone(name="Frankie") {
  console.log("Hello "+ name);
}


function formal(name="Sam", title="Sir") {
  return (title + " "+ name);
}


function timesFive(numImput) {
  // local scope
  var result = numImput * 5
  return result
}


//Global scope

var v = "GlOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func"
  console.log(stuff);
}

fun()
console.log(stuff);
