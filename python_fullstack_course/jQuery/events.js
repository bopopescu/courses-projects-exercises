console.log('events conected!');


//$('h1').click(function() {
  //console.log('There wa a click!');
//})

//$('li').click(function() {
  //console.log('Any li was clicked!');
//})

//$('h1').click(function() {
//  $(this).text("I was changed!")
//})

//$('input').eq(0).keypress(function(event) {
  //if (event.which === 13) {
    //$('h3').toggleClass('turnblue')
  //}
//})


// $('h1').on('mouseenter', function() {
//   $(this).toggleClass('turnblue')
// })


$('input').eq(1).on('click',function() {
  $('.container').fadeOut(3000)
})
