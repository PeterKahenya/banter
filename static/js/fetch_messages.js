function fetch_messages() {
      $.ajax({
        url: window.location.origin+"/livechats/"+window.location.pathname.split("/")[2],
        success: function(response) {
            chats=""
            $(".chatlogs").empty();
            response.map(chat=>{
                console.log(chat.fields.sender)
                myid=parseInt($("#myid").val())
                if (parseInt(chat.fields.sender)===myid) {
            
                    chats+='<div class="chat self">'+
                    '<div class="user-photo">'+
                        '<img src="https://randomuser.me/api/portraits/men/73.jpg" alt="">'+
                    '</div>'+
                   ' <div class="chat-message">'+
                       chat.fields.msg+
                    '</div></div>'
                } else {
                    chats+='<div class="chat friend">'+
                    '<div class="user-photo">'+
                        '<img src="https://randomuser.me/api/portraits/men/79.jpg" alt="">'+
                    '</div>'+
                   ' <div class="chat-message">'+
                       chat.fields.msg+
                    '</div></div>'
                }
            })
            $(".chatlogs").append(chats) 
        },
        error: function(xhr) {
        }
    });
    setTimeout("fetch_messages()",1000);
}

$(document).ready(function () {
    fetch_messages()
});