<?php
    $str_conexao = pg_connect("dbname=jmbnetdb port=5433 user=ventura password=172349av");
    $query = "select nome_modulo from modulo";
    $result = pg_query($conexao,$query);
    if(!($conexao=pg_connect($str_conexao))){
        echo "Não foi possível estabelecer conexão com o banco de dados.";
        exit;
    }
?>