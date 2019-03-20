[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# პირველი წვლილი

ეს რთულია. რთულია როდესაც რაღაცას აკეთებ პირველად. ძალიან უსიამოვნოა შეცდომების დაშვება განსაკუთრებით მაშინ, როდესაც ვინმესთან ერთად მუშაობ. ჩვენ გვსურს დავეხმაროთ მათ, ვისაც აქვს სურვილი ისწავლოს და წვლილი შეიტანოს open source პროექტებში

სტატიებისა და სახელმძღვანელოების წაკითხვა ან ვიდეოების ყურება კარგია, მაგრამ რა შეიძლება იყოს პრაქტიკულ გამოცდილებაზე უკეთესი? პროექტის მიზანია დაეხმაროს და გაუმარტივოს გზა დამწყებებს მათი პირველი კონტრიბუციისაკენ. თუ გინდათ რომ საკუთარი წვლილი შეიტანოთ პროექტში, მაშინ მიყევით ქვემოთ მოცემულ ინსტრუქციებს.

#### *თუ თქვენ არ გქონიათ ტერმინალთან(command line) შეხება, [იხილეთ ინსტრუქცია რომელიც იყენებს გრაფიკულ ინტერფეისს.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

თუ თქვენ არ გაქვთ git დაყენებული თქვენს კომპიუტერზე, [დააყენეთ ის]( https://help.github.com/articles/set-up-git/).

## შექმენით რეპოზიტორიის განშტოება

გვერდის ზედა კუთხეში არსებულ `fork` ღილაკზე დაჭერით შექმენით რეპოზიტორიის ახალი განშტოება
ეს შექმნის რეპოზიტორიის განშტოებას თქვენს ანგარიშზე

## მოახდინეთ რეპოზიტორიის კლონირება

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

ახლა მოახდინეთ რეპოზიტორიის კლონირება თქვენს კომპიუტერზე. შედით თქვენს ანგარიშზე, ნახეთ ამ რეპოზიტორიის განშტოება, გახსენით ის და დააჭირეთ ჯერ `clone` ღილაკს, ხოლო შემდეგ *copy to clipboard*.

გახსენით ტერმინალი და გაუშვით ბრძანება:

```
git clone "url you just copied"
```
სადაც "url you just copied" (ბრჭყალების გარეშე) არის თქვენი რეპოზიტორიის მისამართი. მისამართის მისაღებად მიჰყევით წინა ნაბიჯს.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

მაგალითად:
```
git clone https://github.com/this-is-you/first-contributions.git
```
სადაც `this-is-you` არის თქვენი Github-ის მომხმარებლის სახელი. ასე თქვენ აკოპირებთ ამ რეპოზიტორიას თქვენს კომპიუტერზე

## შექმენით შტო

თქვენს კომპიუტერში გადადით რეპოზიტორიის საქაღალდეში (თუ უკვე იქ არ იმყოფებით):

```
cd first-contributions
```
ახლა შექმენით შტო `git checkout` ბრძანების დახმარებით

მაგალითად
```
git checkout -b add-alonzo-church
```
(არ არის აუცილებელი, რომ შტოს სახელი შეიცავდეს სიტყვა *add*-ს, მაგრამ ამ შემთხვევაში ეს გამართლებულია, რადგანაც ამ შტოს მიზანია დაამატოს თქვენი სახელი სიაში).

## გააკეთეთ სასურველი ცვლილებები და შექმენით commit-ი

გახსენით `Contributors.md` ფაილი ტექსტურ რედაქტორში და სიაში დაამატეთ თქვენი სახელი. ამის შემდეგ შეინახეთ ფაილი.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />


თუ გადახვალთ პროექტის დირექტორიაში და გაუშვებთ ბრძანებას - `git status`, თქვენ დაინახავთ ცვლილებებს.


`git add` ბრძანების დახმარებით განშტოებას დაამატეთ თქვენს მიერ განხორციელებული ცვლილებები:

```
git add Contributors.md
```

ახლა გაუშვით ბრძანება `git commit`, თქვენი ცვლილებების commit-`ისთვის:
```
git commit -m "Add <your-name> to Contributors list"
```
შეცვალეთ `<your-name>` თქვენი სახელით

## გაუშვით თქვენი ცვლილებები Github-ზე

თქვენი ცვლილებების Github-ზე გასაშვებად გამოიყენეთ ბრძანება `git push`:
```
git push origin <add-your-branch-name>
```
`<add-your-branch-name>` შეცვალეთ თქვენს მიერ შექმნილი შტოს სახელით

## დაამოწმეთ თქვენი ცვლილებები განხილვისათვის

თუ თქვენ ნახავთ თქვენს რეპოზიტორიას Github-ზე, დაინახავთ `Compare & pull request` ღილაკს. დააჭირეთ ამ ღილაკს

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

ახლა დაამოწმეთ თქვენი pull request

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

მალე მე განვახორციელებ თქვენი ცვლილებების შერწყმას პროექტის master შტოსთან. ამის შესახებ თქვენ მოგივათ შეტყობინება ელექტრონულ ფოსტაზე.

## რა გავაკეთოთ ამის შემდეგ? 

გილოცავთ! თქვენ განახორციელეთ სტანდარტული _fork -> clone -> edit -> PR_  ნაბიჯები, რომლებიც ხშირად შეგხვდებათ სხვებთან გუნდში მუშაობისას.

გაუზიარე ეს შენს მეგობრებს: [გაზიარება](https://firstcontributions.github.io/#social-share).

თუ გაქვს კითხვები ან გჭირდება დახმარება, [შემოგვირთდი Slack-ზე](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

ახლა შენ შეგიძლია შეიტანო შენი წვლილი სხვა პროექტებშიც. ჩვენ შევქმენით სია პროექტებისა, სადაც შეგიძლია ნახო დავალებები დამწყებთათვის [პროექტების სია](https://firstcontributions.github.io/#project-list).

### [დამატებითი მასალები](additional-material/git_workflow_scenarios/additional-material.md)

## ინსტრუქციები სხვა ინსტუმენტების გამოყენებით

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|
