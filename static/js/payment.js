function changePaymentStatus(value) {
    var checked = false;
  if (document.querySelector('#id_is_confirmed:checked')) {
     checked = true;
  }

  console.log(checked);
}