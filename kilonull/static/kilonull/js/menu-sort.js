jQuery(function($) {
  // Make menu items draggable
  $('div.inline-group').sortable({
    items: 'div.inline-related',
    handle: 'h3:first',
    update: function (event, ui) {
      var counter = 0;
      $(this).find('div.inline-related').each(function(i) {
        if ($(this).find('select[id$=post]') &&
            $(this).find('input[id$=link_url]').val() != '') {
          $(this).find('input[id$=order]').val(counter+1);
          ++counter;
        }
      });
    }
  });
  $('div.inline-related h3').css('cursor', 'move');

  // Fill out link url and text fields based on post selection (fill order too)
  var path_arr = location.href.split('/');
  var protocol = path_arr[0];
  var host = path_arr[2];
  var api = protocol + '//' + host + '/api/posts/';
  $('div.inline-related').find('select[id$=post]').change(function() {
    var id_arr = $(this).attr('id').split('-');
    var n_item = id_arr[1];
    var post_id = $(this).val();
    var post_info = $.getJSON( api + post_id + '/?format=json',
      function(data) {
        // Set link_url, link_text, then order
        $('#id_menuitem_set-' + n_item + '-link_url').val(
          protocol + '//' + host + data['path']
        );
        $('#id_menuitem_set-' + n_item + '-link_text').val( data['title'] );
        $('#id_menuitem_set-' + n_item + '-order').val( n_item );
      }
    );
  });
});
