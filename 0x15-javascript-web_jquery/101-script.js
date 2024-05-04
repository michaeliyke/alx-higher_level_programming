
const jQuery = $;

jQuery(function ($) {
  // When the user clicks on DIV#add_item: a new element is added to the list
  $('DIV#add_item').click(function () {
    $('UL.my_list').append(newItem());
  });

  // When the user clicks on DIV#remove_item: the last element is removed from
  //  the list
  $('DIV#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
  });

  // When the user clicks on DIV#clear_list: all elements of the list are rem'd
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});

/* Create new LI element with textcontent = Item */
function newItem () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  return li;
}
