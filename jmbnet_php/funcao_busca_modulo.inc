<?php
    include "conecta_postgresql.inc";
    $query = "SELECT nome_modulo FROM modulo";
    $result = pg_query($conexao,$query);
    pg_close($conexao);
    
    if (!$result) {
      echo "An error occured.\n";
      exit;
    }  
    while ($row = pg_fetch_row($result)) {
        // echo "<br />\n";
        //$array[] = $row[0];
        echo "<li><a href=\"#\">$row[0]</a></li>\n";
    }  
?>