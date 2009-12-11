<?php

/* Substituido para trabalhar com sessao
if(IsSet($_COOKIE["nome_usuario"]))
    $nome_usuario = $_COOKIE["nome_usuario"];
if(IsSet($_COOKIE["senha_usuario"]))
    $senha_usuario = $_COOKIE["senha_usuario"];
*/
session_start();
if(IsSet($_SESSION["nome_usuario"]))
{
    $nome_usuario = $_SESSION["nome_usuario"];
}
else
{
    // echo $_SESSION["nome_usuario"];
    echo "O IsSet não funcionou";
    exit;
}

if(IsSet($_SESSION["senha_usuario"]))
    $senha_usuario = $_SESSION["senha_usuario"];

if(!(empty($nome_usuario) OR empty($senha_usuario)))
{
   include "conecta_postgresql.inc";
	$resultado = pg_query($conexao, "SELECT * FROM usuario WHERE username='$nome_usuario'");
	if(pg_num_rows($resultado)==1)
	{
		if($senha_usuario != pg_result($resultado,0,"senha"))
		{     /* Substituido para trabalhar com sessao
            setcookie("nome_usuario");
            setcookie("senha_usuario");
            */
            
            unset ($_SESSION['nome_usuario']);
            unset ($_SESSION['senha_usuario']);
            echo "Você não efetuou o LOGIN!1";
            exit;
        }
    }
    else
    {
        /* Substituido para trabalhar com sessao
        setcookie("nome_usuario");
        setcookie("senha_usuario");
        */
        unset ($_SESSION['nome_usuario']);
        unset ($_SESSION['senha_usuario']);
        echo "Você não efetuou o LOGIN!2";
        exit;
    }
}
else
{
    echo $nome_usuario;
    echo "Você não efetuou o LOGIN!3";
    exit;
}

pg_close($conexao);
?>
