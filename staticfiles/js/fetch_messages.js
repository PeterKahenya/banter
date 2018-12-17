function fetch_messages() {
      $.ajax({
        url: window.location.origin+"/livechats/"+window.location.pathname.split("/")[2],
        success: function(response) {
            chats=""
            $("#previous-messages").empty();
            response.map(chat=>{
                chats+='<div class="card"><div class="card-body">'+
                chat.fields.msg+'</div></div>'
            })
            $("#previous-messages").append(chats) 
        },
        error: function(xhr) {
        }
    });
    setTimeout("fetch_messages()",1000);
}

$(document).ready(function () {
    fetch_messages()
});