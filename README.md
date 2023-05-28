# Gerador-de-Senha
Este foi o meu primeiro projeto em Python.
Vou dar uma explicação simples de como meu código está funcionando:

A função gerar_senha recebe o comprimento e os caracteres permitidos como parâmetros. Ela cria uma string vazia e itera comprimento vezes. Em cada iteração, adiciona um caractere aleatório escolhido dos caracteres permitidos à senha. Por fim, retorna a senha gerada.

A função main é onde o programa é iniciado. Ela solicita ao usuário o comprimento da senha desejada e define os caracteres permitidos usando as constantes string.ascii_letters (letras maiúsculas e minúsculas), string.digits (dígitos) e eu também poderia ter adicionado  a contante string.punctuation (caracteres de pontuação) mas optei por manter as senhas apenas com letras e dígitos.

Em seguida, chama a função gerar_senha passando o comprimento e os caracteres permitidos como argumentos. A senha gerada é armazenada na variável senha e, por fim, é exibida na tela.

Quando executado, o usuário será solicitado a digitar o comprimento da senha desejada. Em seguida, o programa irá gerar uma senha aleatória e exibi-la na tela.
