# O que é um conflito de mesclagem?

Quando você tentar mesclar outra branch na sua branch de trabalho atual, você esta puxando as alterações de um outro contexto e combinando-as com os seus arquivos de trabalho atuais.
Se duas pessoas tiverem alterados as mesmas linhas em um mesmo arquivo, ou se uma pessoa resolver deletar isso enquanto outra pessoa resolveu modificá-lo, o Git não será capaz de identificar qual das duas é a versão correta. O Git irá então marcar que este arquivo como possuindo um conflito - o qual você precisará resolver antes de poder continuar o seu trabalho.

# Como resolver um conflito de mesclagem?

Quando se deparar com um conflito de mesclagem, git irá marcar o inicio e o final da área problemática do arquivo envolvendo ela com “<<<<<<<< HEAD” e “>>>>>>>>>>[other branch name]”

O conteúdo após a primeira marcação vem da sua branch de trabalho atual. Depois dos sinais de "menor que", Git nos diz de onde (de qual branch) as mudanças vieram. Uma linha com "=======" separa as duas alterações conflitantes.
Nosso trabalho agora é limpar essas linhas: quando finalizado, o arquivo deverá estar da forma que desejamos. É aconselhável consultar o colega de equipe que escreveu as alterações conflitantes para decidir qual versão deve ser a final. Pode ser um dos seus - ou talvez uma mistura dos dois.

e.g. :
```
 <<<<<<< HEAD:mergetest
 Esta é minha terceira linha
 =======
Esta é a quarta linha que estou adicionando
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indica o inicio das linhas que possuem um conflito de mesclagem. O primeiro conjunto de linhas são as linhas do arquivo para o qual você esta tentando mesclar suas alterações.
`=======`: Indica o ponto de ruptura usado para comparação. Divide as alterações que o usuário comitou (acima) com as alterações provenientes da mesclagem (abaixo) para ver as diferenças visualmente.
`>>>>>>>`: Indica o fim das linhas que tiveram um conflito de mesclagem.

Você resolve um conflito editando o arquivo e então mesclando manualmente as partes do arquivo que o git teve dificuldades para mesclar. Isso pode significar descartar suas alterações ou as de outra pessoa ou prosseguir com uma mistura das duas. Você também precisará deletar '<<<<<<<<', '=======' e '>>>>>>>>' no arquivo.

Depois de resolver o conflito, faça um `git add`. Não se esqueça de fazer os testes, pois você deve se certificar de que resolveu o conflito.

Você também pode baixar plugins diferentes dependendo da IDE que está usando para resolver os conflitos de mesclagem de uma forma mais fácil.

# Como desfazer uma mesclagem?
Se você deseja desfazer uma fusão, você pode digitar `git merge —abort`