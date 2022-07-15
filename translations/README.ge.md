[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# პირველი კონტრიბუცია

ახალი რამის პირველად, დამოუკიდებლად, გაკეთება შეიძლება საკმაოდ რთული აღმოჩნდეს. მითუმეტეს, თუ უცხოებთან თანამშრომლობ და შეცდომების დაშვება არცთუ ისე კარგი გრძნობაა. ჩვენ გვინდოდა დამწყები ოფენ სორს კონტრიბუტორებისთვის გაგვემარტივებინა საქმე და გვესწავლებინა თუ როგორ უნდა შეიტანონ წვლილი სხვა პროექტებში.

კი, სტატიების წაკითხვა და ვიდეოების ყურება კარგია, მაგრამ, პრაქტიკას არც ერთი შეედრება. ეს პროექტიც ზუსტად იმისთვისაა, რომ გაგიმარტივოს გზა პირველ კონტრიბუციამდე, რომელსაც ქვემოთ ჩამოთვლილი რამდენიმე ნაბიჯი გაშორებს.

#### *თუ ტერმინალთან დიდად არ მეგობრობ, [აქ ნახავ რამდენიმე პროგრამას, რომელიც ტერმინალის გამოყენებას აგარიდებს თავიდან]( #ტუტორიალები-სხვა-პროგრამების-გამოყენებით )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

თუ კომპიუტერში გითი არ გაქვს ჩაწერილი, [მიჰყევი ლინკს]( https://help.github.com/articles/set-up-git/).

## დაფორკე ეს რეპოზიტორია

რეპოზიტორიის დაფორკვისთვის, ამ გვერდის მარჯვენა ზედა კუთხეში დააჭირე "Fork" ღილაკს, რომელიც მის ასლს შეგიქმნის.

## რეპოზიტორიის დაკლონვა

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

ახლა, დაფორკილი რეპოზიტორია შენს კომპიუტერზე უნდა გადმოიტანო. ამისთვის შედი შენს გითჰაბის პროფილზე, გახსენი რეპოზიტორია და დააჭირე "Clone or download"-ს, შემდეგ კი *"copy to clipboard"*-ის სურათს.

ახლა გახსენი ტერმინალი და გაუშვი შემდეგი ბრძანება:

```
git clone "url you just copied"
```
სადაც "url you just copied" (ბრჭყალების გარეშე) არის შენ მიერ დაკოპირებული რეპოზიტორიის ლინკი. (თუ ეს ლინკი არ გაქვს, წინა ნაბიჯი თავიდან გაიარე).

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

მაგალითად:
```
git clone https://github.com/this-is-you/first-contributions.git
```
სადაც `this-is-you` ნაწილი, შენი გითჰაბის სახელია. ამითი რეპოზიტორიის ყველა ფაილი შენს კომპიუტერში გადმოვა.

## შექმენი ბრენჩი

შენი კომპიუტერით შედი რეპოზიტორიის ფოლდერში (თუ უკვე იქ არ ხარ):

```
cd first-contributions
```
ახლა შექმენი ახალი ბრენჩი `git checkout` ბრძანების გამოყენებით:
```
git checkout -b <add-your-new-branch-name>
```

მაგალითად:
```
git checkout -b add-alonzo-church
```
(ბრენჩის სახელის დასაწყისში *add*-ის მიწერა სავალდებულო არაა, თუმცა მიზანშეწონილია, რადგანაც მისი მთავარი მიზანია თქვენი სახელი დაამატოს კონტრიბუტორთა სიაში.)

## საჭირო ფაილების შეცვლა და ატვირთვა

ახლა რომელიმე პროგრამით (სასურველია ტექსტ ედიტორით) გახსენი ფაილი, სახელად `Contributors.md` და დაამატე შენი სახელი. ოღონდ გაითვალისწინე, რომ ის სხვების სახელებს შორის უნდა ჩაწერო და არა ფაილის დასაწყისში, ან ბოლოში. შეინახე ცვლილებები.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />


თუ პროექტის ფოლდერში გადახვალ და გაუშვებ ბრძანება: `git status`. ტერმინალი გაჩვენებს რა ფაილებში მოხდა ცვლილებები.


`git add`-ით დაამატე ცვლილებები შენ მიერ შექმნილ ახალ ბრენჩს:

```
git add Contributors.md
```

ახლა შეინახე ისინი `git commit`-ის გამოყენებით:
```
git commit -m "Add <your-name> to Contributors list"
```
აქაც, `<your-name>` უნდა შეცვალო შენი პროფილის სახელით.

## ცვლილებების ატვირთვა გითჰაბზე

ატვირთე შენი ნამუშევარი `git push`-ის მეშვეობით:
```
git push origin <add-your-branch-name>
```
`<add-your-branch-name>` აქ შენ მიერ შექმნილი ბრენჩის სახელით უნდა ჩაანაცვლო.

## განხილვის მოთხოვნა

გითჰაბზე, შენს რეპოზიტორიაში როცა გადახვალ, დაინახავ `Compare & pull request` ღილაკს. დააჭირე.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

ახლა შენ მოითხოვ ცვლილებების განხილვას.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

და სულ მალე, შენი ნამუშევარი ამ პროექტის მთავარ ბრენჩზე გამოჩნდება. ამის შესახებ მეილსაც მიიღებ.

## აქედან საით?

გილოცავ! შენ შეასრულე სტანდარტული კონტრიბუციის პროცედურა, რომელსაც მომავალში ხშირად გამოიყენებ, როგორც კონტრიბუტორი!

აღნიშნე და გაუზიარე მეგობრებს შენი წარმატება [ამ ლინკზე გადასვლით](https://firstcontributions.github.io/#social-share).

[შემოგვიერთდი slack-ზე](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).

თუ კონტრიბუციების სხვაგან შეტანაც გინდა, ჩვენ შენთვის შედარებით მარტივად გასაგები პროექტები შევარჩიეთ,  [რომლებსაც აქ ნახავ](https://firstcontributions.github.io/#project-list).

### [დამატებითი მასალა](../additional-material/git_workflow_scenarios/additional-material.md)


## ტუტორიალები სხვა პროგრამების გამოყენებით

| <a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></a> | <a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [GitHub Desktop](../github-desktop-tutorial.md)              | [Visual Studio 2017](../github-windows-vs2017-tutorial.md)   | [GitKraken](../gitkraken-tutorial.md)                        | [Visual Studio Code](../github-windows-vs-code-tutorial.md)  | [Atlassian Sourcetree](../sourcetree-macos-tutorial.md)      | [IntelliJ IDEA](../github-windows-intellij-tutorial.md)      |