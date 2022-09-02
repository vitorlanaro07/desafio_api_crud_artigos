var texto = document.querySelector(".message__texto");
var mensagem = document.querySelector(".message")
var btn_message = document.querySelector('.message__spam');

if (texto == null){
    mensagem.classList.add("message-off");
}else{
    mensagem.classList.remove("message-off");
    btn_message.addEventListener("click", function(){
        mensagem.classList.add("message-off");
    })
}