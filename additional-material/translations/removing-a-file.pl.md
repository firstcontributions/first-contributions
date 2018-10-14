# Usuwanie plików z Git'a.

Czasami możesz chcieć usunąć plik z Git'a, ale nie z Twojego komputera. Możesz to uczynić za pomocą następującej komendy:

``git rm <file> --cached``

## Co się stało?

Git nie będzie dłużej śledził zmian w kasowanym pliku. Na tyle, na ile Git wie, to tak samo jakbyś usunął plik. Gdybyś umieścił ów plik w swym systemie, zauważyłbyś go nadal tam będącego.

Zauważ, że w przykładzie powyżej użyty jest flag --cached. Gdybyśmy tego nie dodali, Git usunąłby plik zarówno z repozytorium, jak i z twego urządzenia.

Jeśli dokonasz zmiany tak, aby Git wykonał -m "Remove file1.js" i wyślesz do zdalnego repozytorium używając git push origin master, zdalne repozytorium usunie ów plik.

## Dodatki

    Jeśli chcesz wykasować więcej niż jeden plik, możesz umieścić je wszystkie w jednej komendzie:

    `git rm file1.js file2.js file3.js --cached`

    Możesz użyć dzikiej karty (*) aby wykasować podobne pliki. Na przykład, jeśli chcesz usunąć wszystkie pliki .txt z twego lokalnego repozytorium wykonaj:

    `git rm *.txt --cached`
