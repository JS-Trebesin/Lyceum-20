// prompt je string, text
let input = prompt("Zadej číslo")

// parseInt nám dělá int (číslo) ze string (textu)
let cislo = parseInt(input)



// pro porovnání používáme 3x = (===), <, >, !== (nerovná se),
// <=, >=

if (cislo === 5) {
    console.log("číslo je 5")

// else if nám umožňuje přidat druhou podmínku 
//(kontrolovat další věc)
} else if (cislo === 10) {
    console.log("číslo je 10")

// else nám řeší, co se stane, když není splněna žádná podmínka
//výše
} else {
    console.log("číslo není 5 ani 10")
}

// alert vypíše hlášku do okna
// alert("Test")

// prompt umožňuje zadat input
// prompt("Zadej číslo")

