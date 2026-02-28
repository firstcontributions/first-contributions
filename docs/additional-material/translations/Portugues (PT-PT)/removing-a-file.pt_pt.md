# Remover um ficheiro do Git

Por vezes podes querer que o Git deixe de controlar um ficheiro, mas sem o apagar do teu computador. Podes fazer isso com:

``git rm <file> --cached``

## O que aconteceu?

O Git deixa de rastrear o ficheiro. Para o Git, parece que o ficheiro foi removido, embora ainda exista no teu sistema de ficheiros.

No exemplo acima, foi usado o sinalizador `--cached`. Se não usares esse sinalizador, o Git removerá o ficheiro tanto do repositório como do teu sistema de ficheiros.

Se confirmares a alteração com `git commit -m "Remove file1.js"` e empurrares para o remoto com `git push origin master`, o repositório remoto removerá o ficheiro.

## Notas adicionais

- Para remover mais de um ficheiro, inclui-os todos no mesmo comando:

    `git rm file1.js file2.js file3.js --cached`

- Podes usar curingas, por exemplo:

    `git rm *.txt --cached`
