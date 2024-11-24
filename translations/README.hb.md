<div dir="rtl">
  <a href="https://www.codetriage.com/roshanjossey/first-contributions" rel="nofollow"><img src="https://camo.githubusercontent.com/8e53aecabdd0316ce198fe932798bb0f8754b30f/68747470733a2f2f7777772e636f64657472696167652e636f6d2f726f7368616e6a6f737365792f66697273742d636f6e747269627574696f6e732f6261646765732f75736572732e737667" alt="Open Source Helpers"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://camo.githubusercontent.com/76f0e887c183ccc31c1cb63c33d2dbf48cb2df51/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667" alt="License: MIT"></a>
  <a href="https://github.com/ellerbrock/open-source-badges/"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" alt="Open Source Love"></a>
  <a href="https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA"><img align="left" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png"></a>
</div>

<div dir="rtl">
<h1> תרומות ראשונות </h1>
</div>

<div dir="rtl">
מטרת פרויקט זה היא לפשט ולהדריך מתחילים בדרכם אל תרומתם הראשונה לקוד פתוח.
 אם אתם מחפשים דרך לבצע תרומה ראשונית, עקבו אחר ההוראות הבאות.
</div>

<div dir="rtl">
<h4> אם אינכם חשים בנוח להשתמש בשורת פקודה, ניתן להשתמש 
<a href="#הדרכות-בשימוש-כלים-אחרים">בכלים גרפיים</a>.</h4>
</div>

<div dir="rtl">
<h4>כמו כן, ניתן לקרוא את המאמר
<a href="">בשפות אחרות</a>.</h4>
</div>

<div dir="rtl">
<a href="https://help.github.com/articles/set-up-git/">אם אין לכם GIT ניתן להתקין GIT בקישור</a>
</div>

<div dir="rtl">
<a href="/Roshanjossey/first-contributions/blob/master/assets/fork.png"><img img style="float: left;" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository"></a>
</div>

<div dir="rtl">
<h2> בצעו FORK למאגר זה </h2>
</div>

<div dir="rtl">
כדי לבצע FORK למאגר זה, ניתן ללחוץ על כפתור ה – FORK בתחילת העמוד. פעולה זה תיצור עותק של מאגר זה בחשבון שלכם.
</div>


<div dir="rtl">
<h2> שכפול המאגר </h2>
</div>

<div dir="rtl">
  <img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />
</div>

<div dir="rtl">
  
כעת, שכפלו את המאגר הזה למחשב שלכם. לכו לדף ה-GitHub שלכם, לחצו על כפתור השכפול ואז לחצו על הצלמית `copy to clipboard`.

פתחו טרמינל והריצו את הפקודה הבאה:
</div>

```
git clone "url you just copied"
```
<div dir="rtl">
  
כאשר הביטוי `"url you just copied"` (ללא סימני הגרשיים) הוא הקישור למאגר זה שביצעתם עליו FORK קודם לכן. ראו את הצעדים הקודמים כדי להשיג את הקישור.
</div>

<img align="left" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

<div dir="rtl">
לדוגמא:
</div>

```
git clone https://github.com/this-is-you/first-contributions.git
```
<div dir="rtl">
  
כאשר `this-is-you` הוא שם המשתמש שלכם ב-GitHub. לכאן אתם מעתיקים את התוכן של מאגר first-contributions ב-GitHub לתוך המחשב שלכם.
</div>

<div dir="rtl">
<h2> יצירת ענף </h2>
</div>

<div dir="rtl">
החליפו לתיקיית המאגר בתוך המחשב שלכם (באם טרם נכנסתם לתיקייה זו):
</div>

```
cd first-contributions
```
<div dir="rtl">
  
כעת, צרו ענף (branch) בשימוש הפעולה `git checkout`:
</div>

```
git checkout -b your-new-branch-name
```
<div dir="rtl">
  לדוגמא:
</div>

```
git checkout -b add-alonzo-church
```

<div dir="rtl">
(שם הענף לא חייב להכיל את המילה add בתוכו, אבל זה הגיוני להוסיף אותה מכיוון שמטרת הענף היא להוסיף את שמכם לרשימה.)
</div>

<div dir="rtl">
<h2> ערכו שינויים הכרחיים ובצעו להם commit </h2>
</div>

<div dir="rtl">
  
כעת פתחו את הקובץ `Contributors.md` בתוכנת עריכת טקסט והוסיפו את השם שלכם אליו. אל תוסיפו את השם בתחילת הקובץ או בסופו. הוסיפו אותו באמצע. לאחר שסיימתם, שמרו את הקובץ.


אם תנווטו לתיקיית הפרויקט ותבצעו את הפעולה `git status`, תוכלו לראות את השינויים שביצעתם שם.
הוסיפו את השינויים האלו לענף שיצרתם תוך שימוש בפקודה `git add`:
</div>

```
git add Contributors.md
```
<div dir="rtl">
  
עכשיו, בצעו commit לשינויים הללו תוך שימוש בפקודת `git commit`:
</div>

```
git commit -m "Add <your-name> to Contributors list"
```
<div dir="rtl">
  
החליפו את הביטוי `<your-name>` עם השם שלכם.
</div>

<div dir="rtl">
<h2>לדחוף את השינויים ל-GitHub</h2>
</div>

<div dir="rtl">
  
דחפו את השינויים תוך שימוש בפקודה `git push`:
</div>

```
git push origin <add-your-branch-name>
```
<div dir="rtl">
  
החליפו את `<add-your-branch-name>` עם השם של הענף שיצרתם מוקדם יותר.
</div>

<div dir="rtl">
<h2> הגישו את השינויים שלכם לסקירה </h2>
</div>

<div dir="rtl">
  
אם תלכו למאגר שלכם ב-GitHub, תוכלו לראות כפתור עם הכיתוב `Compare & pull request`. לחצו על כפתור זה.

<img style="float: left;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

כעת, הגישו את בקשת הדחיפה (pull request):

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

בקרוב, אצרף את כל השינויים לתוך הענף הראשי של פרויקט זה. אתם תקבלו עדכון במייל ברגע שהשינויים ימוזגו.
</div>

<div dir="rtl">
<h2>מחקו את הענף שלכם אחרי שבקשת הדחיפה אושרה</h2>
</div>

<div dir="rtl">
<h2>מה לעשות מכאן?</h2>
</div>

<div dir="rtl">
כל הכבוד! כרגע סיימתם את מעגל הזרימה הסטנדרטי של Fork->Clone->Edit->PR שאתם תפגשו באופן שכיח כתורמים!
תחגגו את התרומתכם ושתפו אותה עם החברים והעוקבים שלכם בכך שתלכו ל-<a href="https://firstcontributions.github.io/#project-list">web app</a>.
  </br>
אתם יכולים להצטרף לצוות הסלאק שלנו אם אתם צריכים עזרה או אם יש לכם שאלות.
<a href="https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA">הצטרפו לקבוצת סלאק</a>.

עכשיו אפשר להתחיל לתרום לפרוייקטים אחרים. הכנו רשימה של פרוייקטים על נושאים קלים שאתם יכולים להתחיל לעבוד עליהם.

<a href="https://firstcontributions.github.io/#project-list">רשימה של פרוייקטים ב-web app</a>.
</div>

<div dir="rtl">
<h3><a href="../additional-material/git_workflow_scenarios/additional-material.md">חומר נוסף</a></h3>
</div>

<div dir="rtl">
<h2>הדרכות בשימוש כלים אחרים</h2>
</div>

<div dir="rtl">
  <table style="width:100%">
    <tr>
      <th><img alt="GitKraken" src="https://firstcontributions.github.io/assets/Readme/gk-icon.png" width="100"></th>
      <th><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></th>
      <th><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></th>
    </tr>
    <tr>
      <th><a href="../gui-tool-tutorials/gitkraken-tutorial.md">GitKraken</a></th>
      <th><a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md">Visual Studio 2017</a></th>
      <th><a href="../gui-tool-tutorials/github-desktop-tutorial.md">GitHub Desktop</a></th>
    </tr>
  </table>
</div>
