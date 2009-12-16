<?php
   /* Alterado para trabalhar com sessao
	setcookie("nome_usuario");
	setcookie("senha_usuario");
	*/
	session_start();
	$_SESSION = array();
	session_destroy();
	header ("Location: index.html");
?>

