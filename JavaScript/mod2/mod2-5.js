const uniqueNumbers = [];
let isDuplicate = false;

while (!isDuplicate) {
    const input = prompt("Enter a number (or enter a number you've already given to stop):");

    if (input === null || input.trim() === "") {
        break;
    }

    const currentNumber = parseInt(input);

    if (isNaN(currentNumber)) {
        continue;
    }

    if (uniqueNumbers.includes(currentNumber)) {
        isDuplicate = true;
        console.log("Stopping.");
    } else {
        uniqueNumbers.push(currentNumber);
    }
}

uniqueNumbers.sort((a, b) => a - b);

console.log("--- Sorted Numbers ---");

if (uniqueNumbers.length === 0) {
    console.log("No numbers entered.");
} else {
    for (let i = 0; i < uniqueNumbers.length; i++) {
        console.log(uniqueNumbers[i]);
    }
}