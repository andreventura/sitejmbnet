<?php
    $str_conexao = "host=localhost dbname=jmbnetdb port=5432 user=ventura password=172349av";
    if(!($conexao=pg_connect($str_conexao))){
        echo "Não foi possível estabelecer conexão com o banco de dados.";
        exit;
       
    }
?>