[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# İlk töhfələr

Bu layihə yeni başlayanlar üçün ilk töhfələrini vermə yollarını sadələşdirmək və yol göstərmək məqsədi daşıyır. İlk töhfənizi vermək istəyirsinizsə, aşağıdakı adımları tekrar edin.

_Əgər komut istemi (Command Prompt) ilə razı deyilsinizsə, [burada GUI alətlərindən istifadə edən təlimatlar tapa biləriniz.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Kompüterinizdə GIT yoxdursa, [buradan quraşdıra bilərsiniz ](https://help.github.com/articles/set-up-git/).

## layihəni "çatallama"

Səhifənin yuxarı hissəsindəki "Fork" düyməsini vuraraq bu layihəni çəngəlləyin.
Bu hesabınızda bu layihənin bir kopyasını yaradacaqdır.

## Depoyu (Repository) klonlama

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

İndi çəngəlli depoyu kompüterinizə klonlayın. GitHub hesabınıza daxil olun, çəngəlli depoyu açın, kod düyməsini vurun və sonra _copy to clipboard_ klikləyin.

Daha sonra komut istemini açın aşağıdaki git komutunu daxil edin:

```
git clone "kopyaladığınız-url"
```
"kopyaladığınız-url" (dırnaq işarəsi olmadan) yerine bu deponun GitHub səhifəsindən aldığınız linki kopyalayın.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Misal üçün:
```
git clone https://github.com/kullanıcı-adi/first-contributions.git
```
`istifadəçi-adı` sizin GitHub istifadəçi adınız. Burada GitHub-dakı ilk töhfələr deposunun içindəkiləri kompüterinizə kopyalayırsınız.

## Budağı (Branch) yaratmaq

Kompüterinizdəki anbar qovluğuna keçin (əgər orada deyilsinizsə):

```
cd first-contributions
```
`git checkout` əmrini istifadə edərək bir Budağ (Branch) yaradın:
```
git checkout -b <sizin-yeni-budağ-adınız>
```

Misal üçün:
```
git checkout -b add-alonzo-church
```
(Budağ adının içinde *add* sözünün olması məcbur deyil, ancaq bu bölmənin məqsədi adınızı siyahıya əlavə etmək olduğu üçün daxil etmək məqbul bir şeydir.)

## Lazımi dəyişiklikləri edin və bu dəyişiklikləri həyata keçirin

İndi `Contributors.md` faylını mətn redaktorunda açın, adınızı əlavə edin. Faylın əvvəlinə və ya sonuna əlavə etməyin. Arada bir yerə qoyun. İndi faylı saxlayın.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Layihə qovluğuna gedib `git status` əmrini icra etsəniz, dəyişikliklərin olduğunu görəcəksiniz.

Bu dəyişiklikləri `git add` əmrindən istifadə edərək yaratdığınız Budağa əlavə edin:

```
git add Contributors.md
```

İndi `git commit` əmrindən istifadə edərək bu dəyişiklikləri edin:

adınızla `<your-name>` ilə əvəz olunsun.

## Dəyişiklikləri GitHub'a itələyin (push)

Dəyişikliklərinizi "git push" əmrindən istifadə edərək itələyin:


```
git push origin <add-your-branch-name>
```

`<add-your-branch-name>` yerine öz istifadəçi adınızı daxil edin.

## Dəyişikliklərinizi nəzərdən keçirmək üçün göndərin

GitHub-dakı anbarınıza daxil olsanız, bir `Compare & pull request` düyməsini görəcəksən. Bu düyməni vurun.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

İndi çəkmə tələbini (pull request) göndərin.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tezliklə bütün dəyişikliklərinizi bu layihənin master filialına birləşdirəcəyəm. Dəyişikliklər birləşdirildikdən sonra bildiriş e-poçtu alacaqsınız.

## Bundan sonra nə edə bilərəm?

Təbriklər! Töhfə olaraq tez-tez qarşılaşacağınız standart _fork -> clone -> edit -> pull request_ tamamlamısınız!

Töhfənizi qeyd edin və [veb tətbiqetmə](https://firstcontributions.github.io/#social-share) girərək dostlarınız və izləyicilərinizlə bölüşün.

Hər hansı bir köməyə ehtiyacınız varsa və ya suallarınız varsa, [Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-iywfifau-_aMtdwTjBoMzQqzW8~YUUA) komandamıza qoşula bilərsiniz.

İndi başqa layihələrə töhfə verməyə başlayaq. Başlaya biləcəyiniz asan məsələləri olan layihələrin siyahısını hazırladıq, [Siyahıya baxın](https://firstcontributions.github.io/#project-list).

### [Əlavə Məlumat](additional-material/git_workflow_scenarios/additional-material.md)

## Digər texnologiyalar haqqında təlim

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
