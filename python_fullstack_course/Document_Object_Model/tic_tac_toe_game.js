console.log("conected!");

var restart = document.querySelector('#button');

var cells = document.querySelectorAll('td');

function clearBord() {
  for (var i = 0; i < cells.length; i++) {
    cells[i].textContent = ''
  }
}

restart.addEventListener('click', clearBord);


function changeMarker() {
  if (this.textContent === '') {
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O'
  }else {
    this.textContent = ''
  }
}

for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener('click', changeMarker)
}
