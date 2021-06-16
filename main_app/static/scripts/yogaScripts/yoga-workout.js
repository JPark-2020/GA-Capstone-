// masterTime
const clockDuration = 5; 
let time = clockDuration * 60; 


let clock = document.querySelector(".timer")
let exercise1 = document.querySelector(".exercise1")

const startRound = () => {
    const minutes = Math.floor(time/60);
    let seconds = time % 60; 

    clock.innerHTML = `${minutes}:${seconds}`;
    time--;
}
const yogaExercises = (exercise, delay, nextExercise) => {

    setTimeout(()=>{
        exercise1.innerHTML = exercise;
        // exerciseTimer.innerHTML = `${minutes3}:${seconds3}`
        // CHECKS IF THERE IS A NEXT EXERCISE OTHERWISE IT WOULD PASS UNDEFINED 
        nextExercise && nextExercise();  
    }, delay)
}

document.querySelector(".startTimer").addEventListener("click", ()=>{
    let id = setInterval(startRound,1000);
    setTimeout(() => {
        clearTimeout(id);
        clock.innerHTML = "WORKOUT DONE"
    }, 300000)
    yogaExercises('Mountain Pose', 1000, ()=>{
        yogaExercises('Raised Arms Pose', 30000, () =>{
            yogaExercises('Standing Forward Bend', 30000, () =>{
                yogaExercises('Garland Pose', 30000, () =>{
                    yogaExercises('Lunge', 30000, () =>{
                        yogaExercises('Plank', 30000, () =>{
                            yogaExercises('Staff Pose', 30000, () =>{
                                yogaExercises('Seated Forward Bend', 30000, () =>{
                                    yogaExercises('Happy Baby', 30000, () => {
                                        yogaExercises('Head to Knee Pose', 30000, () =>{
                                        })
                                    })
                                })
                            })
                        })
                    })
                })
            })
        })
    });
})

// let id2 = setInterval(yogaExercises, 1000);
// setTimeout(()=>{
//     clearTimeout(id2);
    
// })

