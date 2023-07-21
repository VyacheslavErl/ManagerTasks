$("#add-task").submit(function(event) {
  var nameInput = $("input[name='name']").eq(0);
  var textInput = $("input[name='text']").eq(0);
  var dateInput = $("input[name='do_before']").eq(0);

  if (nameInput.val() === "") {
    event.preventDefault();
    nameInput.next().css("display", "block");
  }

  if (textInput.val() === "") {
    event.preventDefault();
    textInput.next().css("display", "block");
  }

  if (dateInput.val() === "") {
    event.preventDefault();
    dateInput.next().css("display", "block");
  }
});