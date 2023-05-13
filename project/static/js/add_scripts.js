function like_idea(idea_id, like_id) {
    $.ajax({
        type: "GET",
        url: "/like_action/" + idea_id.toString() + "/" + like_id.toString(),
        success: function(response) {
            //var json = jQuery.parseJSON(response)
            var json = response
            $('#lc_' + idea_id.toString() + "_" + like_id.toString()).html(json.new_count)
        },
        error: function(error) {
            console.log(error);
        }
    });
}