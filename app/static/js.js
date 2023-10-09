`
  TODO:
    Uppercase
    Confirm delete
`


$(()=> {
    $("#add-new-item").focus()
    $("#submit-button").click(()=> addNewItem())
    $("#add-new-item").keyup(function(event) {
      if (event.keyCode === 13) {
          addNewItem()
      }
    });
    $(".del-button").click((e)=>{
      delItem(e.currentTarget.id)
    })
});

function addNewItem() {
  let textboxValue = $("#add-new-item").val()
  textboxValue = textboxValue.charAt(0).toUpperCase()+ textboxValue.slice(1)

  if (textboxValue){
    fetch("/add-new-item", {
    method: "POST",
    body: JSON.stringify({
      item: textboxValue
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  }).then(()=>{location.reload()})
  }
}


function delItem(id) {

  fetch("/delete-item", {
  method: "POST",
  body: JSON.stringify({
    id: id
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
}).then(()=>{location.reload()})

}
