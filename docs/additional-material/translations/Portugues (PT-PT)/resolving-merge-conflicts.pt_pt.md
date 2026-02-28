# Resolver conflitos de merge

Conflitos surgem quando o Git não consegue reconciliar automaticamente alterações em linhas semelhantes de ficheiros.

Fluxo básico:

1. Após um merge/rebase com conflitos, edita os ficheiros marcados pelo Git e resolve os blocos conflituosos.
2. Marca os ficheiros como resolvidos com `git add <file>`.
3. Continua o rebase com `git rebase --continue` ou conclui o merge com `git commit`.
