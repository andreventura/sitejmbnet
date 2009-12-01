<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <title>JMBNet</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
    <link rel="stylesheet" type="text/css" href="jmbnet002.css" />
	 <link rel="stylesheet" type="text/css" href="css/multi/tree.css">
    <script type="text/javascript" src="build/yahoo.js" ></script>
    <script type="text/javascript" src="build/event.js"></script>
    <script type="text/javascript" src="build/treeview.js" ></script>
    <script type="text/javascript" src="build/jktreeview.js" ></script>
</head>

<body>
<div id="geral"> 
    <div id="cabecalho">
        <!-- <h1>Cabecalho</h1> -->
        <h1><?php include "teste.inc"; ?>teste2</h1>
    </div>
    <div id="bloco_central">
        <div id="menu_lateral"> 
            <spam id="tree2"></spam>
        </div>
        <script type="text/javascript">
            <!-- variáveis -->
            var i, array_modulos, string_array;
            <!-- //recebe a string com elementos separados, vindos do PHP -->
            <!-- string_array = “<?php echo $string_array; ?>“; -->
            <!-- transforma esta string em um array próprio do Javascript -->
            <!-- array_modulos = string_array.split(“|”); -->

            <!-- varre o array só pra mostrar que tá tudo ok -->
            for (i in array_modulos)
                alert(array_modulos[i]);
        
            <!-- TreeView Demo 2 //-->
            var oaktree=new jktreeview("tree2")
            
            var branch2=oaktree.addItem("CSS Library", "") //A TREE BRANCH
                oaktree.addItem("Horizontal Menus", branch2, "http://dynamicdrive.com/style/csslibrary/category/C1/") //Add this item to branch2
                oaktree.addItem("Horizontal Menus", branch2, "http://dynamicdrive.com/style/csslibrary/category/C1/") //Add this item to branch2
                
            var branch2=oaktree.addItem("CSS Library", "") //A TREE BRANCH
	             oaktree.addItem("Horizontal Menus", branch2, "http://dynamicdrive.com/style/csslibrary/category/C1/") //Add this item to branch2
	             oaktree.addItem("Vertical Menus", branch2, "http://dynamicdrive.com/style/csslibrary/category/C2/") //Add this item to branch2
	                 var branch2_4=oaktree.addItem("CSS Layouts", branch2, "http://www.dynamicdrive.com/style/layouts/") //A TREE BRANCH WITH URL FOR ITSELF!
		                  oaktree.addItem("Two Columns", branch2_4, "http://www.dynamicdrive.com/style/layouts/category/C9/") //Add this item to branch2_4
		                  oaktree.addItem("Tree Columns", branch2_4, "http://www.dynamicdrive.com/style/layouts/category/C10/") //Add this item to branch2_4
		                  
            oaktree.addItem("Webmaster Tools", "", "http://tools.dynamicdrive.com")
            oaktree.addItem("Help Forums", "", "http://dynamicdrive.com/forums/")
            
            oaktree.treetop.draw(); //REQUIRED LINE: Initalize tree
        </script>
                
        <div id="conteudo">
            <h1>Conteudo</h1>
            <p>Atividades Exercidas: Atendimento receptivo e ativo aos clientes do Banco,
            orientação referente a conta corrente , pagamentos através da conta , abertura
            de reclamações, sugestões e elogios, transferências para outros setores do
            Banco.
            </p>
        </div>
    </div>
    <div id="rodape">
        <h1>Rodape</h1>
    </div>
</div>
</body>
</html>