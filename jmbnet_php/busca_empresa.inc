<?php
    include "conecta_postgresql.inc";
    $query = "SELECT nome_modulo,codigo_modulo_id FROM modulo";
    $query = "SELECT nome_modulo,codigo_modulo_id FROM empresa";
    $result = pg_query($conexao,$query);
          
    if (!$result_modulo) {
      echo "An error occured.\n";
      exit;
    }  
    
    while ($row = pg_fetch_row($result)) {
        // echo "<br />\n";
        //$array[] = $row[0];
        echo "<option value=";
        <option >Volvo</option>
                    <option>Saab</option>
                    <option>Mercedes</option>
             <option>Audi</option>
        
        if ($row_modulo[1] == 10)
        {
            echo "<li><a href=\"index.html\" >$row_modulo[0]</a></li>\n";
        }
        else
        {
            echo "<li><a href=\"#\" >$row_modulo[0]</a></li>\n";
            // Busca opcoes para cada modulo
            // $query_opcao_menu = "SELECT om.nome_opcao,om.codigo_opcao_menu_id FROM opcao_menu om WHERE om.codigo_modulo_id =$row_modulo[1]";
            // $result_opcao_menu = pg_query($conexao,$query_opcao_menu);
            // while ($row_opcao_menu = pg_fetch_row($result_opcao_menu)) {
            //       echo "<ol><a href=\"#\">$row_opcao_menu[0]</a></ol>\n";
            //}
        }        
    }  
    pg_close($conexao);
?>