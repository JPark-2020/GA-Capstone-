
// 2 different functions running 
  // 1 = timer 
  // 1 = punch combos 
const roundDuration = 3; 
let time = roundDuration * 60; 

let clock = document.querySelector(".timer")

let punchOne = document.querySelector(".one")
let punchTwo = document.querySelector(".two")
let punchThree = document.querySelector(".three")
let punchFour = document.querySelector(".four")

let punches = ['Jab', 'Cross', 'Left hook', 'Right hook', 'Left uppercut', 'Right uppercut']

function startRound(){
  const minutes = Math.floor(time/60);
  let seconds = time % 60; 


  function punchRandomizer(){
    return Math.floor(Math.random()*punches.length)
  } 

  clock.innerHTML = `${minutes}:${seconds}`;
  punchOne.innerHTML = punches[punchRandomizer()]; 
  punchTwo.innerHTML = punches[punchRandomizer()]; 
  punchThree.innerHTML = punches[punchRandomizer()]; 
  punchFour.innerHTML = punches[punchRandomizer()]; 
  time--; 
}

document.querySelector(".startTimer").addEventListener("click", ()=>{
    let id = setInterval(startRound,3000);
    setTimeout(() => {
        clearTimeout(id);
        clock.innerHTML = "WORKOUT DONE"
    }, 180000)
    })




