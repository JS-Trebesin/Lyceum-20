let holidays = document.querySelector(".holidays")
let school = document.querySelector(".school")
let buttonSun = document.querySelector("#button-sun")
let buttonBooks = document.querySelector("#button-books")


buttonBooks.addEventListener("click", goToHolidays)
buttonSun.addEventListener("click", backToSchool)


function goToHolidays() {
    holidays.style.display = "none"
    school.style.display = "block"

}


function backToSchool() {
    holidays.style.display = "block"
    school.style.display = "none"

}

