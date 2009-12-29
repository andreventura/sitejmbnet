<?php
$gmtDate = gmdate("D, d M Y H:i:s"); 
header("Expires: {$gmtDate} GMT"); 
header("Last-Modified: {$gmtDate} GMT"); 
header("Cache-Control: no-cache, must-revalidate"); 
header("Pragma: no-cache");
header("Content-Type: text/html; charset=ISO-8859-1");


if(isset($_GET["inicio"]) || isset($_GET["busca"]) || isset($_GET["categoria"]))	// lista produtos
	include "listaProdutos.php";
	
elseif(isset($_GET["carregaFormLogin"]))	// carrega formulario de login 

 	include "form_login.php";
	
elseif(isset($_GET["novoUsuario"]))	// criação de novo usuário

	include "novoUsuario.php";

else echo "ERRO: favor acessar a home da loja!";

?>