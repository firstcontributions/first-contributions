# What is a merge conflict?
# O que é um conflito de mesclagem?

When you try to merge another branch into your current working branch, you are taking changes from another context and combining them with your current working files.
If two people have changed the same lines in the same file, or if one person decided to delete it while the other person decided to modify it, Git cannot identify which is the correct version. Git will then mark the file as having a conflict - which you'll have to resolve before you can continue your work.

Quando você tentar mesclar outra branch na sua branch de trabalho atual, você esta puxando as alterações de um outro contexto e combinando-as com os seus arquivos de trabalho atuais.
Se duas pessoas tiverem alterados as mesmas linhas em um mesmo arquivo, ou se uma pessoa ressolver deletar isso enquanto outra pessoa resolveu modifica-lo, o Git não será capaz de indentificar qual das duas é a versão correta. O Git irá então marcar que este arquivo como possuindo um conflito - o qual você precisará resolver antes de poder continuar o seu trabalho.

# How to resolve a merge conflict?
# Como resolver um conflito de mesclagem?

When faced with a merge conflict, git will mark the problematic area in the file by enclosing it in “<<<<<<<< HEAD” and “>>>>>>>>>>[other branch name]”

The contents after the first marker originate from your current working branch. After the angle brackets, Git tells us where (from which branch) the changes came from. A line with "=======" separates the two conflicting changes.
Our job is now to clean up these lines: when we're done, the file should look exactly as we want it to look. It is advisable to consult the teammate who wrote the conflicting changes to decide which version should be final. It could be either on of yours - or maybe a mixture between the two.

Quando se deparar com um conflito de mesclagem, git irá marcar o inicio e o final da area problemática do arquivo envolvendo ela com “<<<<<<<< HEAD” e “>>>>>>>>>>[other branch name]”
O conteudo após a primeira marcação vem da sua branch de trabalho atual. Depois dos sinais de "menor que", Git nos diz de onde (de qual branch) as mudanças vieram. Uma linha com "=======" separa as duas alterações conflitantes.
Nosso trabalho agora é limpar essas linhas: quando finalizado, o arquivo deverá estar da forma que desejamos. É aconselhável consultar o colega de equipe que escreveu as alterações conflitantes para decidir qual versão deve ser a final. Pode ser um dos seus - ou talvez uma mistura dos dois.

e.g. :
```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest

e.g. :
```
 <<<<<<< HEAD:mergetest
 Esta é minha terceira linha
 =======
Esta é a quarta linha que estou adicionando
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indicates the start of the lines that had a merge conflict. The first set of lines are the lines from the file that you were trying to merge the changes into.  
`=======`: Indicates the break point used for comparison. Breaks up changes that user has committed (above) to changes coming from merge (below) to visually see the differences.  
`>>>>>>>`: Indicates the end of the lines that had a merge conflict.  


`<<<<<<<`: Indica o inicio das linhas que possuem um conflito de mesclagem. O primeiro conjunto de linhas são as linhas do arquivo para o qual você esta tentando mesclar suas alterações.
`=======`: Indica o ponto de ruptura usado para comparação. Divide as alterações que o usuário comitou (acima) com as alterações provenientes da mesclagem (abaixo) para ver as diferenças visualmente.
`>>>>>>>`: Indica o fim das linhas que tiveram um conflito de mesclagem.

You resolve a conflict by editing the file and then manually merging the parts of the file that git had trouble merging. This may mean discarding either your changes or someone else's or going ahead with a mix of the two. You will also need to delete the '<<<<<<<', '=======', and '>>>>>>>' in the file.

Você resolve um conflito editando o arquivo e então mesclando manualmente as partes do arquivo que o git teve dificuldades para mesclar. Isso pode significar descartar suas alterações ou as de outra pessoa ou prosseguir com uma mistura das duas. Você também precisará deletar '<<<<<<<<', '=======' e '>>>>>>>>' no arquivo.


Once you have resolved the conflict do a `git add`. Do not forget to run the tests, as you have to make sure that you have resolved the conflict.

You can also download different plugins depending on the IDE you are using for an easier way to resolve merge conflicts.

Depois de resolver o conflito, faça um `git add`. Não se esqueça de fazer os testes, pois você deve se certificar de que resolveu o conflito.

Você também pode baixar plug-ins diferentes dependendo da IDE que está usando para resolver os conflitos de mesclagem de uma forma mais fácil.

# How to undo a merge?
If you want to undo a merge then you can do `git merge —abort`

# Como desfazer uma mesclagem?
Se você deseja desfazer uma fusão, você pode digitar `git merge —abort`