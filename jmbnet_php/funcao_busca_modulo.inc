<?php
    include "conecta_postgresql.inc";
    $query_modulo = "SELECT nome_modulo,codigo_modulo_id FROM modulo";
    $result_modulo = pg_query($conexao,$query_modulo);
          
    if (!$result_modulo) {
      echo "An error occured.\n";
      exit;
    }  
    
    while ($row_modulo = pg_fetch_row($result_modulo)) {
        // echo "<br />\n";
        //$array[] = $row[0];
        echo "<li><a href=\"#\" >$row_modulo[0]</a></li>\n";
        // Busca opcoes para cada modulo
        // $query_opcao_menu = "SELECT om.nome_opcao,om.codigo_opcao_menu_id FROM opcao_menu om WHERE om.codigo_modulo_id =$row_modulo[1]";
        // $result_opcao_menu = pg_query($conexao,$query_opcao_menu);
        // while ($row_opcao_menu = pg_fetch_row($result_opcao_menu)) {
        //       echo "<ol><a href=\"#\">$row_opcao_menu[0]</a></ol>\n";
        //}        
    }  
    pg_close($conexao);
?>