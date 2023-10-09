`
  TODO:
    Uppercase
    Confirm delete
`


$(()=> {
    $("#add-new-item").focus()
    $("#submit-button").click(addNewItem())
    $("#add-new-item").keyup(function(event) {
      if (event.keyCode === 13) {
          addNewItem()
      }
  });
});

function addNewItem() {
  let textboxValue = $("#add-new-item").val()
  textboxValue = textboxValue.charAt(0).toUpperCase()+ textboxValue.slice(1)

  if (textboxValue){
    fetch("/add-new-item", {
    method: "POST",
    body: JSON.stringify({
      item: textboxValue,
      completed: false
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  }).then(()=>{location.reload()})
  }
}
