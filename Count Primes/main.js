const number = 10
let output = 0

for (i = 2; i < number; i++) {
    let isPrime = true
    for (j = 2; j < i; j++) {
        if (i % j === 0) {
            isPrime = false
            break
        }
    }
    if (isPrime) output++
}

console.log(output)