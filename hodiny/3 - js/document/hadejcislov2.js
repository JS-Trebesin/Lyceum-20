console.log("test")

let odpoved = document.querySelector("#odpoved")

let tlacitko = document.querySelector("#tlacitko")

tlacitko.addEventListener("click", hadani)
// nejde protože event listener má špatný prvek
tlacitko.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        hadani()
    }
})

let tajneCislo = 42

function hadani() {
    console.log("test2")

    let input = document.querySelector("#input")
    let inputCislo = parseInt(input.value)

    input.style.color = "red"

    if (inputCislo > tajneCislo) {
        odpoved.innerText = "Moc"
    } else if (inputCislo < tajneCislo) {
        odpoved.innerText = "Málo"
    } else {
        odpoved.innerText = "Congratz"
    }
}
