<?php
// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtém os dados do formulário
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $endereco = $_POST['endereco'];
    $telefone = $_POST['telefone'];

    // Identifica o IP do usuário
    $ip = $_SERVER['REMOTE_ADDR'];

    // Redireciona para a página de mensagem com o IP
    header("Location: mensagem.php?ip=$ip");
    exit();
}
?>
