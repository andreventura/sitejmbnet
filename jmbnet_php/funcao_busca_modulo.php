<?php

/* function retorna_modulo_menu_lateral(){ */
    include "conecta_postgresql.inc";
    $query = "select nome_modulo from modulo";
    $result = pg_query($conexao,$query);
    pg_close($conexao);
    //criando a string com a versátil função php implode
    $string_array = implode(“|”, $result);
    echo $string_array;
    /*return $stryng_array;*/
/*}*/
?>