 const numbersArray = [];

        for (let i = 0; i < 5; i++) {
            const input = prompt("Anna numero")

            numbersArray.push(parseInt(input));
        }

        console.log("Numerot reverses")

        for (let i =numbersArray.length - 1; i >= 0; i--){
            console.log(numbersArray[i])
        }   