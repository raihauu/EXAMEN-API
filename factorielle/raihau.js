function factorielle(number) {
    acc = 1
    for (let i = 1; i <= number; i++) {
        acc = acc * i
    }
    return acc
}

console.log(factorielle(3));


