<?php
// Obtem os dados digitados
$_username = $_POST["username"];
$_senha = $_POST["senha"];

// Acesso ao banco de dados
include "conecta_postgresql.inc";
$query = "SELECT * FROM usuario WHERE username='$_username'";
$result = pg_query($conexao,$query);
if ($result==0) // testa se a consulta voltou alguma linha
{
    echo "<html><body>";
	 echo "<p align=\"center\">Usuário não encontrado!$result</p>";
	 echo "<p align=\"center\"><a href=\"login.html\">Voltar</a></p>";
	 echo "</body></html>";
}
else
{
    if ($_senha != pg_result($result,0,"senha")) // confere senha
    {   
        echo "<html><body>";
		  echo "<p align=\"center\">A senha está incorreta!</p>";
		  echo "<p align=\"center\"><a href=\"login.html\">Voltar</a></p>";
		  echo "</body></html>";
    }   
    else // usuario e senha coretos. Criar cookies
    {
        // setcookie("nome_usuario",$_username); Trocado cookies por sessao
        // setcookie("senha_usuario",$_senha);
        session_start();
        $_SESSION['nome_usuario'];
        $_SESSION['senha_usuario'];        
        // direciona para a pagina inicial dos usuarios cadastrados
        header("Location: pagina_inicial.html");
    } 
}  
pg_close($conexao);    

?>
