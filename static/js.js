
//
// document.addEventListener("DOMContentLoaded", function() {
//
// });

window.addEventListener("DOMContentLoaded", function() {
  console.log("Hello World!");
  document.getElementById("submit_button").addEventListener("click", myFunction);
});

function myFunction() {
  console.log("clicked")
  x = document.getElementById("add_new_item").value
  fetch("/add_new_item", {
  method: "POST",
  body: JSON.stringify({
    item: x,
    completed: false
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});
  console.log(x);
  // document.getElementById("demo").innerHTML = "YOU CLICKED ME!";
}
