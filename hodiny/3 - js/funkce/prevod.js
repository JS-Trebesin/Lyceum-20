let vysledek = document.querySelector("#result"),
    tlacitko = document.querySelector("#button"),
    inputCF = document.querySelector("#inputCF"),
    inputValue = document.querySelector("#inputValue")

tlacitko.addEventListener("click", prevod)

function prevod() {
    let inputValueAsNo = parseInt(inputValue.value)
    if (inputCF.value === "C") {
        vysledek.innerText = CelToF(inputValueAsNo)
    } else if (inputCF.value === "F") {
        vysledek.innerText = FToCel(inputValueAsNo)
    } else {
        vysledek.innerText = "Chybný údaj"
    }
}

function CelToF(c) {
    let f = c * 1.8 + 32
    return f
}

function FToCel(f) {
    let c = f - 32 * 0.5556
    return c
}
