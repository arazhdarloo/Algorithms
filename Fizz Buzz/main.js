const number = 15

for(i = 1; i <= number; i++){
    if(i % 3 == 0 && i % 5 == 0) console.log("FIZZ BUZZ")
    else if(i % 3 == 0) console.log("FIZZ")
    else if(i % 5 == 0) console.log("BUZZ")
    else console.log(i)
}