$(function() {
	$( "#droplist" ).sortable();
    $( "#my-sortable1" ).disableSelection();

    $('.draggable').draggable({
        connectToSortable: '#droplist',
        helper: 'clone'
    })
	
    
    $('#droppable').droppable({
        drop: function(event, ui) {
            $('#droplist').append($("ui.draggable").clone());
            $("#droplist .itemx").removeClass("itemx").removeClass("draggable").addClass("item_new");
            $(".item_new .itmlnk").removeClass("itmlnk").addClass("itmlnk_new");
            
          
            
        },
        activate: function() {
            $('#droppable').css({
                border: "medium double green",
                backgroundColor: "lightGreen"
            });
        },
        deactivate: function() {
            $('#droppable').css("border", "").css("background-color", "");
        }
    });
    
	
});
$(document).on('click', ".itemlink", (function(event) {
        event.preventDefault();
        $(this).parent().parent().remove();
        
        
    })
    );

function form_submit() {
        event.preventDefault();
        var data = $('#subj_form').serializeArray();
        $
        jQuery.each( data, function( i, field ) {
      $( "#droplist" ).append( field.value + " " );
    });
    };

