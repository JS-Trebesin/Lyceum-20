function obvodObsah(a) {
    let obsah = a * a
    let obvod = 4 * a
    console.log("obsah je", obsah)
    console.log("obvod je", obvod)
}

obvodObsah(3)

function hodnoceniRestaurace(hodnoceni) {
    if (hodnoceni === 5) {
        console.log("Super")
    } else if (hodnoceni < 5) {
        console.log("Ok")
    } else if (hodnoceni < 3) {
        console.log("Otřes")
    }
}
hodnoceniRestaurace(5)
