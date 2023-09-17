function like_idea(idea_id, like_id) {
    $.ajax({
        type: "GET",
        url: "/like_action/" + idea_id.toString() + "/" + like_id.toString(),
        success: function(response) {
            $('#lb_' + idea_id.toString()).load(location.href + ' #lb_' + idea_id.toString())
        },
        error: function(error) {
            console.log(error);
        }
    });
}


/*function like_idea(idea_id, like_id) {
    $.ajax({
        type: "GET",
        url: "/like_action/" + idea_id.toString() + "/" + like_id.toString(),
        success: function(response) {
            //var json = jQuery.parseJSON(response)
            //var json = response
            //json.forEach(l => {
            //    $('#lc_' + idea_id.toString() + "_" + l.like_id.toString()).html(l.count);
            //    //$('#lc_' + idea_id.toString() + "_" + l.like_id.toString()).parent().parent().css("border-color", "#dbdbdb")
            //});
            //div = $('#lb_' + idea_id.toString())
            $('#lb_' + idea_id.toString()).load(location.href + ' #lb_' + idea_id.toString())
            //console.log(div)
        },
        error: function(error) {
            console.log(error);
        }
    });
}
*/