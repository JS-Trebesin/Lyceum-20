// querySelector nám umožňuje vybírat prvky z HTML
// je univerzální classy, id, celé prvky
let tlacitko = document.querySelector("#tlacitko")

// getElementById umožní vybírat pouze ID z HTML (nemusím ale psát #)
let nadpis = document.getElementById("nadpis")

let input = document.querySelector("#input")

tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {
    // .value bere hodnotu z html prvku
    let textInput = input.value
    nadpis.style.color = "red"
    nadpis.style.fontSize = "50px"
    if (textInput === "ráno") {
        // .innerText mění text html prvku
        nadpis.innerText = "Zakázané slovo"
    } else {
        nadpis.innerText = textInput
    }
}
