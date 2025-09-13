# O que é um conflito de merge?

Quando você tenta fazer o merge de outra branch na sua branch atual de trabalho, está pegando alterações de outro contexto e combinando com os arquivos em que está trabalhando.
Se duas pessoas modificaram as mesmas linhas no mesmo arquivo, ou se uma pessoa decidiu deletá-lo enquanto a outra fez modificações, o Git não consegue identificar qual é a versão correta. O Git então marcará o arquivo como estando em conflito – e você precisará resolver esse conflito antes de continuar seu trabalho.

# Como resolver um conflito de merge?

Quando você se depara com um conflito de merge, o Git marcará a área problemática no arquivo delimitando-a com “<<<<<<< HEAD” e “>>>>>>> [nome da outra branch]”.
O conteúdo após o primeiro marcador vem da sua branch atual de trabalho. Depois dos colchetes angulares, o Git informa de qual branch vieram as outras alterações. Uma linha com “=======” separa as duas mudanças em conflito.
Nosso trabalho agora é limpar essas linhas: quando terminarmos, o arquivo deve estar exatamente como queremos que fique. É recomendável consultar o colega de equipe que escreveu as alterações conflitantes para decidir qual versão deve ser a final. Pode ser a sua, a dele — ou até uma combinação das duas.

e.g. :
```
 <<<<<<< HEAD:mergetest
 Essa é minha terceira linha
 =======
 Essa é a quarta linha, eu estou adicionando
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indica o início das linhas que tiveram um conflito de merge. O primeiro conjunto de linhas corresponde às linhas do arquivo no qual você estava tentando mesclar as alterações.  
`=======`: Indica o ponto de separação usado para comparação. Separa as alterações que o usuário realizou (acima) das alterações vindas da mesclagem (abaixo), permitindo visualizar claramente as diferenças. 
`>>>>>>>`: Indica o final das linhas que tiveram um conflito de merge.

Você resolve um conflito editando o arquivo e mesclando manualmente as partes que o Git teve dificuldade em unir. Isso pode significar descartar suas alterações, as de outra pessoa ou seguir com uma combinação das duas. Você também precisará remover os marcadores '<<<<<<<', '=======', e '>>>>>>>' do arquivo.


Depois de resolver o conflito, execute um git add. Não se esqueça de rodar os testes, pois é importante garantir que o conflito foi resolvido corretamente.

Você também pode baixar diferentes plugins, dependendo da IDE que estiver usando, para facilitar a resolução de conflitos de merge.


# Como desfazer um merge?
Se você quiser desfazer um merge, pode usar o comando `git merge —abort`
