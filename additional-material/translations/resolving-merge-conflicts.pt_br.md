# Qual é o conflito de fusão?

Quando você tenta mesclar outro ramo no ramo em que você está trabalhando atualmente, você pega as alterações de outro contexto e as combina com os arquivos em que está trabalhando atualmente.
Se duas pessoas alterarem a linha no mesmo arquivo, ou se uma pessoa decidir excluir o arquivo enquanto a outra decidir mudar, o Git não saberá o que é certo. O Git marcará o arquivo como uma disputa. A disputa que você deve resolver antes de continuar trabalhando.

# Como resolver uma disputa de fusão?

Quando o Git detecta um conflito de fusão, ele marcará o local do problema em um arquivo, excluindo-o com:
“<<<<<<<< HEAD” and “>>>>>>>>>>[nome do outro branch]”

O conteúdo da primeira tag virá da sua ramificação atual. Em seguida, segue a linha com "=======", seguido por conteúdo do ramo que está na linha com o seu. Isso é seguido pelos caracteres ">>>>>" e pelo nome desse outro ramo.
Nossa tarefa é editar essas linhas. Quando terminar, o arquivo deve ficar exatamente do jeito que parece. Pode ser necessário consultar um colega que tenha escrito conteúdo que esteja em conflito com o nosso, para que possamos decidir qual código está correto. Talvez seja seu, talvez dele - ou uma mistura de ambos.

Exemplo:
```
 <<<<<<< HEAD:mergetest
 Esta é minha terceira linha
 =======
 Esta é a quarta linha que estou adicionando
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

`<<<<<<<`: Indica o começo das linhas onde está o conflito. Essas linhas são do seu arquivo que você tentou combinar.
`=======`: indica um ponto de interrupção para comparação. Compartilhe as alterações do seu commit (acima) e mude outra pessoa (abaixo) para facilitar.
`>>>>>>>`: indica o final da linha onde está o conflito.

Você resolve a disputa editando o arquivo e combinando manualmente partes do arquivo em que o Git encontrou o problema. Isso pode significar que você precisa descartar suas alterações, alterar outra pessoa ou criar uma mistura de ambas. Também é necessário excluir '<<<<<<<', '=======', in '>>>>>>>'.

Uma vez que a disputa foi resolvida, use o comando `git add`. Não se esqueça de realizar testes para garantir que a disputa foi resolvida adequadamente.

Você também pode instalar plugins diferentes que dependem do seu IDE para ajudar a resolver conflitos.

# Como desfazer o mesclagem (merge)?
Para desfazer a fusão, use o comando `git merge -abort`.
