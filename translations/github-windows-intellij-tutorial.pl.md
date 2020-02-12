[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Pierwsze kontrybucje

| <img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width="40"> | IntelliJ IDEA |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |


To trudne. Za pierwszym razem zawsze jest ciężko. Zwłaszcza, gdy z kimś współpracujesz, popełnianie błędów nie jest rzeczą komfortową. Ale w open source chodzi o współpracę i wspólną pracę. Chcieliśmy uprościć sposób, w jaki nowi autorzy oprogramowania typu open source uczą się i pomagają po raz pierwszy.

Czytanie artykułów i oglądanie samouczków może pomóc, ale co jest lepsze niż faktyczne robienie rzeczy bez bałaganu? Ten projekt ma na celu zapewnienie wskazówek i uproszczenie sposobu, w jaki nowicjusze wnoszą swój pierwszy wkład. Pamiętaj, że im bardziej jesteś zrelaksowany, tym lepiej się uczysz. Jeśli szukasz pierwszego wkładu, po prostu wykonaj poniższe czynności. Obiecujemy, że będzie fajnie.

Jeśli nie posiadasz środowiska IntelliJ na swoim komputerze, [zainstaluj je](https://www.jetbrains.com/idea/download/#section=windows).

** Uwaga: ** Ten samouczek został wykonany przy użyciu IntelliJ IDEA (wersja 2019.3.2) na komputerze z systemem Windows 10. W dalszej części tego samouczka wykorzystamy niektóre skróty klawiaturowe. Mogą się one różnić w innych systemach operacyjnych (macOS / Linux).

## Rozgałęź to repozytorium

<img align="right" width="300" src="../assets/fork.png" alt="Rozgałęż to repozytorium" />

Rozgałęź to repozytorium klikając przycisk rozwidlenia w prawym górnym rogu tej strony. Spowoduje to utworzenie kopii tego repozytorium na Twoim koncie GitHub.

GitHub śledzi relacje między Twoim repozytorium a tym, z którego je rozgałęziłeś. Możesz myśleć o swoim repozytorium jak o kopii roboczej.

Większość repozytoriów GitHub najwyższego poziomu (tj. tych niepochodzących z innych repozytoriów) ma niewielki zespół ludzi, którzy mogą bezpośrednio zatwierdzać zmiany. Wszyscy pozostali współpracownicy muszą rozgałęzić repozytorium i wprowadzić zmiany w rozwidleniu, a następnie utworzyć żądanie ściągnięcia (pull request), aby poprosić o scalenie ich zmian w repozytorium najwyższego poziomu. Jeśli administrator repozytorium najwyższego poziomu zatwierdzi zmiany, zostaną one scalone, a Ty zyskasz natychmiastową sławę i fortunę! Więcej informacji o tym, jak to zrobić później.

## Sklonuj swoje repozytorium

<img align="right" width="300" src="../assets/clone.png" alt="Sklonuj to repozytorium" />

Następnym krokiem jest sklonowanie repozytorium do Twojego komputera, abyś mógł zacząć wprowadzać zmiany. IntelliJ IDEA potrzebuje adresu URL Twojego repozytorium, więc kliknij przycisk „klonuj”, a następnie kliknij ikonę „skopiuj do schowka”.

** OSTROŻNIE: ** Jednym z błędów, które często popełniają nowi autorzy, jest klonowanie repo, od którego dokonałeś rozgałęzienia zamiast klonowania swojego repozytorium. Sprawdź pasek adresu przeglądarki i upewnij się, że klonujesz swoje repozytorium.

Teraz otwórz IntelliJ IDEA.

IntelliJ IDEA umożliwia przełączenie się (w terminologi Git - sklonowanie) istniejącego repozytorium i utworzenie nowego projektu na podstawie pobranych danych.

Z menu głównego wybierz VCS | Uzyskaj z kontroli wersji lub, jeśli żaden projekt nie jest aktualnie otwarty, kliknij "Pobierz z kontroli wersji" na ekranie powitalnym.

W oknie dialogowym "Pobierz z kontroli" wersji określ adres URL zdalnego repozytorium, które chcesz sklonować (możesz kliknąć opcję Testuj, aby upewnić się, że można nawiązać połączenie z serwerem Github) lub wybrać jedną z usług hostingowych VCS po lewej stronie. Jeśli jesteś już zalogowany w wybranej usłudze hostingowej, akcja kończąca zasugeruje listę dostępnych repozytoriów, które możesz sklonować.

Kliknij Klonuj. Jeśli chcesz utworzyć projekt IntelliJ IDEA na podstawie sklonowanych źródeł, kliknij przycisk Tak w oknie dialogowym potwierdzenia. Mapowanie katalogu głównego Git zostanie automatycznie ustawione na katalog główny projektu.

Jeśli twój projekt zawiera submoduły, zostaną one również sklonowane i automatycznie zarejestrowane jako katalogi główne projektu.

** Ważne **: Upewnij się, że jest to rozwidlone repozytorium, a nie oryginalne, w przeciwnym razie nie będzie działać.

## Stwórz gałąź

W Git rozgałęzienie jest potężnym mechanizmem, który pozwala oddzielić się od głównej ścieżki programistycznej, na przykład, gdy trzeba pracować nad funkcją lub zamrozić określony stan bazy kodu dla wydania i tak dalej.

W IntelliJ IDEA wszystkie operacje na gałęziach są wykonywane w wyskakującym oknie Git Branches. Aby je wywołać, kliknij widżet Git na pasku stanu lub naciśnij Ctrl + Shift + `.

Nazwa gałęzi, na której się obecnie znajdujesz, jest wyświetlana w widżecie Git na pasku stanu.

W wyskakującym oknie Branches wybierz opcję New Branch.

W oknie dialogowym, które zostanie otwarte, określ nazwę gałęzi i upewnij się, że opcja Checkout jest zaznaczona, jeśli chcesz przejść do tej gałęzi.

Nowa gałąź rozpocznie się od pozycji wartości wskaźnika HEAD. Jeśli chcesz stworzyć gałąź z poprzedniego commit'u zamiast bieżącego wskaźnika HEAD gałęzi, wybierz ten commit na karcie Dziennik w oknie narzędzi kontroli wersji Alt + 9 i wybierz New Branch z menu kontekstowego.


## Dokonaj niezbędnych zmian

Otwórz `Contributors.md` i dopisz swoje imię i nazwisko gdziekolwiek w pliku. Ten plik zawiera GFM (GitHub Flavored Markdown), który jest zastrzeżonym formatem składni <a href="https://en.wikipedia.org/wiki/Markdown">markdown</a>.

Skopiuj jedną z linii kontrybutorów, zmodyfikuj go swoim nazwiskiem, aby upewnić się, że masz poprawną składnię - może być wybredna.

## Zatwierdź i wypchnij zmiany do GitHub'a

Wybierz pliki, które chcesz zatwierdzić, lub całą listę zmian na karcie Zmiany lokalne w oknie narzędzia Kontrola wersji Alt + 9 i naciśnij Ctrl + K lub kliknij przycisk Zatwierdź na pasku narzędzi.

Okno dialogowe Zatwierdź zmiany, które zawiera listę wszystkich plików, które zostały zmodyfikowane od ostatniego zatwierdzenia, a także wszystkich nowo dodanych niewersjonowanych plików.

Wprowadź sensowny komunikat zatwierdzenia.

Możesz kliknąć Zatwierdź historię wiadomości Ctrl + M, aby wybrać z listy ostatnich wiadomości zatwierdzenia.

Możesz także edytować komunikat zatwierdzenia później, zanim go wypchniesz.

Naciśnij Ctrl + Shift + K lub wybierz VCS | Git | Wypchnij z menu głównego. Zostanie otwarte okno dialogowe Zatwierdzenia, pokazujące wszystkie repozytoria Git (dla projektów z wieloma repozytoriami) i zawierające wykaz wszystkich zatwierdzeń dokonanych w bieżącej gałęzi w każdym repozytorium od ostatniego wypchnięcia zmian.

## Prześlij zmiany do sprawdzenia

W tym momencie dokonałeś zmiany, ale nadal znajduje się ona tylko w twoim repozytorium. W tym kroku pokażemy, jak przesłać żądanie do administratora repozytorium najwyższego poziomu w celu scalenia zmiany.

W repozytorium w serwisie GitHub zobaczysz przycisk „Porównaj i poproś o złączenie” (Compare & pull request) obok powiadomienia o nowej gałęzi. Kliknij ten przycisk.

<img src="../assets/compare-and-pull.png" alt="create a pull request" />

A teraz wyślij prośbę o złączenie.

<img src="../assets/submit-pull-request.png" alt="submit pull request" />

Wkrótce połączę wszystkie twoje zmiany w głównej gałęzi tego projektu. Po scaleniu zmian otrzymasz wiadomość e-mail z powiadomieniem.

## Co dalej?

Gratulacje! Właśnie ukończyłeś standardowy proces roboczy _rozgałęzienie -> klonowanie -> edycja -> PR_, w którym często będziesz pracować!

Świętuj swój wkład i podziel się nim z przyjaciółmi i obserwatorami, przechodząc do [strony](https://roshanjossey.github.io/first-contributions/#social-share).

Możesz dołączyć do naszego zespołu na Slack'u, jeśli potrzebujesz pomocy lub masz pytania.. [Dołącz do Slack'a](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Teraz zacznij od udziału w innych projektach. Zebraliśmy listę projektów z łatwymi problemami, od których możesz zacząć. Sprawdź [listę projektów.](https://roshanjossey.github.io/first-contributions/#project-list).

### [Materiały dodatkowe](additional-material/git_workflow_scenarios/additional-material.md)

[Powrót do strony głównej](README.md)

## Autopromocja

Jeśli podoba Ci się ten projekt, oznacz go gwiazdką [GitHub](https://github.com/Roshanjossey/first-contributions).
Jeśli czujesz szczególną hojność, zacznij obserwować [Roshan](https://roshanjossey.github.io/) na
[Twitterze](https://twitter.com/sudo__bangbang) and
[GitHubie](https://github.com/roshanjossey).

<a href="http://saasgrids.com"> <img alt="http://saasgrids.com" src="../assets/saasgrids-banner.png" width="500"></a>
