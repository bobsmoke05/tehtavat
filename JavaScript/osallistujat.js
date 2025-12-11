const osallistujat = [];

const input = prompt("Monta osallistujaa")

monta = parseInt(input)

for (let i = 0; i < monta; i++) {
    const moi = prompt("Nimi:")
    osallistujat.push(moi)
}

osallistujat.sort();
console.log (osallistujat);