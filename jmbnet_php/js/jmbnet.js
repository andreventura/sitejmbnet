// exibe a resposta do servidor
/*
function trataDados(wNomeDaDiv){
	var info = ajax.responseText;
	var saida = document.getElementById(wNomeDaDiv);
	saida.innerHTML = info;
}
*/

function trataDados(wNomeDaDiv){
	var info = ajax.responseText;
	var newElement = document.createElement("hr");
	var saida = document.getElementById(wNomeDaDiv)
	saida.innerHTML = info;
}

function CarregaFormLogin(){
    var secao = "carregaFormLogin";
    var parametro = 0;
    var url="jmbnet.php?"+secao+"="+encodeURIComponent(parametro);
    requisicaoHTTP("GET",url,true);
}

// exibe ou oculta a mensagem de espera
function Aviso(exibir) {
	var saida = document.getElementById("avisos");
	if(exibir){
		saida.className = "aviso";
		saida.innerHTML = "Aguarde...processando!";
	}
	else {
		saida.className = "";
		saida.innerHTML = "";
	}
}
