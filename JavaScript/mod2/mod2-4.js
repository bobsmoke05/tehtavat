const numbersArray = [];

let currentinput = null;

while (currentinput !== 0) {
    const input = prompt("Anna numero, 0 lopettaa")

    currentinput = parseInt(input);

    if (currentinput !== 0) {
        numbersArray.push(currentinput);
    }

}

numbersArray.sort((a, b) => b - a );

for (let i = 0; i < numbersArray.length; i++) {
    console.log(numbersArray[i]);
}