let cislo1 = parseInt(prompt("Zadej prvn číslo"))
let cislo2 = parseInt(prompt("Zadej druhé číslo"))


if (cislo1 > cislo2) {
    console.log("První číslo, " + cislo1 + ", je větší")
} else if (cislo2 > cislo1) {
    console.log("Druhé číslo, " + cislo2 + ", je větší")
} else {
    console.log("Čísla se rovnají")
}