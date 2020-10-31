# Removing a file from Git

Sometimes, you may want to remove a file from Git but not delete it from your computer. You can achieve this by using the following command:

# Removendo um arquivo do Git

Às vezes, você pode querer remover um arquivo do Git, mas não excluí-lo do seu computador. Você pode fazer isso usando o seguinte comando:

``git rm <file> --cached``

## So what happened?

Git will no longer keep track of changes in the removed file. As far as Git knows, it's as if you had deleted the file. If you were to locate the file in your file system, you will notice that it's still there.

Notice that in the example above, the flag `--cached` is used. If we didn't add this flag, Git will remove the file from not just the repo, but from your file system too.

If you commit the change with `git commit -m "Remove file1.js"` and pushed it to the remote repository using `git push origin master`, the remote repository will remove the file.

## Então o que aconteceu?

O Git não irá mais controlar as mudanças no arquivo removido. Pelo que Git sabe, é como se você tivesse excluído o arquivo. Se você localizar o arquivo em seu sistema de arquivos, notará que ele ainda está lá.

Observe que no exemplo acima, o sinalizador `--cached` é utilizado. Se não adicionarmos esse sinalizador, o Git removerá o arquivo não apenas do repositório, mas também do seu sistema de arquivos.

Se você confirmar a mudança com `git commit -m" Remove file1.js "` e enviar para o repositório remoto usando `git push origin master`, o repositório remoto removerá o arquivo.

## Additional features

-   If you want to remove more than one file, you can include them all in the same command:

## Características adicionais

- Se você deseja remover mais de um arquivo, pode incluí-los todos no mesmo comando:

    `git rm file1.js file2.js file3.js --cached`

-   You can use a wildcard (*) to remove similar files. For example, if you would like to remove all .txt files from your local repository:


- Você pode utilizar o caractere coringa (*) para remover todos os arquivos semelhantes.  Por exemplom se você deseja remover todos os .txt do seu repositório local:

    `git rm *.txt --cached`
