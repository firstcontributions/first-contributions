# Removendo o arquivo

Às vezes você quer remover um arquivo do Git, mas não quer removê-lo do seu computador. Você pode fazer isso usando o seguinte comando:

`` git rm <arquivo> --cached``

## O que aconteceu?

O Git não seguirá mais as alterações no arquivo removido. No que diz respeito ao Git, esse arquivo não existe mais. Se você procurar um arquivo no seu disco, verá que ele ainda existe.

No exemplo acima, usamos o parâmetro `--cached`. Se não fosse usado, o Git removeria o arquivo do nosso disco.

Se agora fizermos um commit com `git commit -m "Remover file1.js"` e enviá-lo para um repositório remoto com o comando `git push origin master`, o arquivo também será removido do repositório remoto.

## Opções adicionais

- Se você quiser remover vários arquivos, poderá incluir todos em um único comando:

  ``git rm file1.js file2.js file3.js --cached``

- Você pode usar o asterístico (*) para remover arquivos semelhantes. Por exemplo, se você quiser remover todos os arquivos com a extensão .txt do seu repositório, use o comando:

  ``git rm *.txt --cached``
