var hot = false
var temp = 60


if (temp > 80){
    hot = true
}
console.log(hot)


var hot = false
var temp = 50

if (temp > 80) {
  hot = true
}
console.log(hot);

if (temp > 80) {
  console.log("Hot outside!");
}else {
  console.log("It's not very hot tody!");
}


temp = 75
// temp = 30

if (temp > 80){
    console.log("Hot outside!")
} else if(temp <= 80 && temp >= 50){
    console.log('Nice outside!')
} else if(temp <= 50 && temp >= 32){
    console.log("Its cooler outside!")
} else{
    console.log("Its really cold outside!")
}


// Items sold that day
var ham = 10
var cheese = 10

// Report to HQ
var report = 'blank'

if(ham >= 10 && cheese >= 10){
    report = "Strong sales of both items"

}else if(ham === 0 && cheese === 0){
    report = "Nothing sold!"
}else{
    report = 'We had some sales'
}
console.log(report)
