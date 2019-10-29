# PORQUE USAR RAMAS(branch) MIENTRAS SE ESTÁ CONTRIBUYENDO

Las ramas(branch) son simplemente punteros a un commit.

Cuando se ramifica, git esencialmente crea un nuevo estado de su código actual, en el que puede trabajar, sin afectar el importante estado principal del código (que está en la rama maestra).

Cuando esté satisfecho con sus experimentos y desee fusionar sus experimentos en el código principal, ejecute git merge
<branch name> master.

Esto le dirá a git, que agregue todos los cambios de tu rama en la que esta experimentando dentro de la rama master.

De esta manera, mientras se trabaja en un proyecto de código abierto con una gran cantidad de contribuyentes, este se hará mas facil al momento de combinar el código de la forma más adecuada sin alterar el código principal o la rama master.
