function cellCompete(states, days){
    let prevState = [0,...states, 0];
   for(let i = 0; i < days; i++){
       
       for(let j = 1; j <= states.length; j++){
           
           //console.log(prevState[j-1], prevState[j+1]);
           if(prevState[j-1] == prevState[j+1] ){
              states[j-1] = 0;
           }
           else{
             states[j-1] = 1;
           }
           //console.log(states)
       }
       prevState = [0, ...states, 0];
   }
   console.log(states);
   return states;
}

cellCompete([1,0,0,0,0,1,0,0], 1);
