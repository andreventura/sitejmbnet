<?php
    include "conecta_postgresql.inc";
    $query_modulo = "SELECT nome_modulo,codigo_modulo_id FROM modulo";
    $result_modulo = pg_query($conexao,$query_modulo);
    
    if (!$result_modulo) {
      echo "Erro ao tentar selecionar a tabela modulo.\n";
      exit;
    }  
    
    $num_rows = pg_num_rows($result_modulo);

    for($i=0;$i<$num_rows;$i++){
        $r = pg_fetch_row($result_modulo, $i);
        // O estilo deverá ser controlado pelo login do usuario.
        switch($r[0]){
            case "Compras":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Financeiro":
                echo "<li><a style=\"color:#BFBFBF\" href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Vendas":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Estoque":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Custos":
                echo "<li><a style=\"color:#BFBFBF\" href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Contabil":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Fretes":
                echo "<li><a style=\"color:#BFBFBF\" href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Gerencial":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Configuração":
                echo "<li><a href=\"#\" >$r[0]</a></li>\n";
                break;
            case "Logout":
                echo "<li><a href=\"logout.php\" >$r[0]</a></li>\n";
                break;
        }
    }   
    pg_close($conexao);
?>