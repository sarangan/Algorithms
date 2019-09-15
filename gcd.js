function generalizedGCD(num, arr)
{
    let gcd = 1;
    for(let i = 0; i < num; i++){
        let temp_gcd = arr[i];
        for(let j = 0; j < num; j++){
            if(arr[j] % temp_gcd !== 0 ){
                temp_gcd = 1;
                break;
            }
        }
        if(temp_gcd != 1){
            gcd = temp_gcd;
        }
        
    }
    
    return gcd;
    
}
