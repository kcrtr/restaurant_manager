frappe.pages['kds'].on_page_load = (wrapper) => {
  frappe
    .call('restaurant_manager.restaurant_manager.methods.get_all_orders')
    .then((data) => {
      $(data.message).appendTo(wrapper)
    })
}

frappe.realtime.on('new_order', function (order) {
  var order = order
  frappe
    .call('restaurant_manager.restaurant_manager.methods.get_new_order', {
      order: order,
    })
    .then((data) => {
      $('#orders').prepend(data.message)
      frappe.utils.play_sound('new_order')
    })
})

$('#body').on('click', '.done', function (e) {
  e.preventDefault()
  $(this).parent().parent().remove()
})
