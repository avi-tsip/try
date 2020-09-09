var restart = document.querySelector("#b");
var tds = document.querySelectorAll("td")
console.log(typeof tds)

function squareMaker() {
    if (this.textContent === ""){
        this.textContent = "x";
    }
    else if (this.textContent === "x") {
        this.textContent = "o";
    }
    else {
        this.textContent = "";
    }
}

for (var i = 0; i < tds.length; i++) {
    tds[i].addEventListener("click", squareMaker)
}

restart.addEventListener("click", function(){
    for (key in tds) {
        tds[key].textContent = "";
    }
})