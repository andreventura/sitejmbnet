<?php
$info = "";
if(isset($_POST["username1"]) && isset($_POST["senha1"])) {
    // Obtem os dados digitados para criar a sessao
    $username = $_POST["username1"];
    $senha = $_POST["senha1"];
    // Acesso ao banco de dados
    include "conecta_postgresql.inc";
    $query = "SELECT * FROM usuario WHERE username='$username'";
    $result = pg_query($conexao,$query);
    $num_rows = pg_num_rows($result);
    // testa se a consulta voltou alguma linha
    // if ($result==0){
    if ($num_rows==0){
        echo "<center><p class=\"erro\">Usuário não encontrado!</p></center>";
    }else{
        // confere senha 
        if($senha != pg_result($result,0,"senha")){   
            echo "<center><p class=\"erro\">A senha está incorreta!</p></center>";
        }else{
            // usuario e senha coretos. Criar cookies/sessao
            // setcookie("nome_usuario",$_username); Trocado cookies por sessao
            // setcookie("senha_usuario",$_senha);
            if (!isset($_SESSION)){
                session_start();
            }
            $_SESSION['nome_usuario']=$username;
            $_SESSION['senha_usuario']=$senha;        
            // direciona para a pagina inicial dos usuarios cadastrados
            header("Location: pagina_inicial.php");
        } 
    }  
    pg_close($conexao);
}    
?>
<form id="formAjax" action="javascript:void%200" onSubmit="enviaDados('form_login.php'); return false;" >
<!-- <form method="POST" action="login.php"> -->
<!-- <form >  -->
   &nbsp;	&nbsp;	&nbsp;	&nbsp;	&nbsp;	&nbsp;	&nbsp;	&nbsp;
  <center><select>
    <option>Empresa 1</option>
        <option>Empresa 2</option>
        <option>Empresa 3</option>
    </select></center>
    <center><p>Usuário: <input id="username1" type="text" name="username1" size="10"></p></center>
    <center><p>Senha: <input id="senha1" type="password" name="senha1"  size="10"></p></center>
    <center><p><input type="submit" value="Login" name="login"></p></center>
</form>

