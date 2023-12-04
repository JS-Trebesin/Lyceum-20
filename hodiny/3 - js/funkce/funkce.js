let odpoved = document.querySelector("#odpoved")
let tlacitko = document.querySelector("#tlacitko")
let input = document.querySelector("#input")

tlacitko.addEventListener("click", obarviNadpis)

function obarviNadpis() {
    odpoved.style.color = "green"
    odpoved.innerHTML = input.value
    odpoved.style.fontSize = "50px"
}

input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        obarviNadpis()
    }
})

// funkci voláme pomocí jejího názvu a () ... nazevFunkce()
// funkce nám umožňuje schovat několik řádků kódu pod jeden název a opakovaně je zavolat

function ukazka(text) {
    console.log(text)
}

// ukazka("náhodná věta")

function scitani(cisloA, cisloB) {
    let vysledek = cisloA + cisloB
    return vysledek
}

scitani(1, 5)
let vysledekFunkce = scitani(2, 5)
// console.log(vysledekFunkce)
// console.log(scitani(3, 5))

function prevod(km) {
    let mile = km * 0.6
    return mile
}

let vzdalenostVMilich = prevod(50)
