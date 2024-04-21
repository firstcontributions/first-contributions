# Removendo um arquivo do Git

Às vezes, você pode querer remover um arquivo do Git, mas não excluí-lo do seu computador. Você pode fazer isso usando o seguinte comando:

``git rm <file> --cached``

## Então o que aconteceu?

O Git não irá mais controlar as mudanças no arquivo removido. Pelo que Git sabe, é como se você tivesse excluído o arquivo. Se você localizar o arquivo em seu sistema de arquivos, notará que ele ainda está lá.

Observe que no exemplo acima, o sinalizador `--cached` é utilizado. Se não adicionarmos esse sinalizador, o Git removerá o arquivo não apenas do repositório, mas também do seu sistema de arquivos.

Se você confirmar a mudança com `git commit -m" Remove file1.js "` e enviar para o repositório remoto usando `git push origin master`, o repositório remoto removerá o arquivo.


## Características adicionais

- Se você deseja remover mais de um arquivo, pode incluí-los todos no mesmo comando:

    `git rm file1.js file2.js file3.js --cached`

- Você pode utilizar o caractere coringa (*) para remover todos os arquivos semelhantes.  Por exemplo se você deseja remover todos os .txt do seu repositório local:

    `git rm *.txt --cached`
