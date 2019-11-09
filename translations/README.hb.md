<div dir="rtl">
  <a href="https://www.codetriage.com/roshanjossey/first-contributions" rel="nofollow"><img src="https://camo.githubusercontent.com/8e53aecabdd0316ce198fe932798bb0f8754b30f/68747470733a2f2f7777772e636f64657472696167652e636f6d2f726f7368616e6a6f737365792f66697273742d636f6e747269627574696f6e732f6261646765732f75736572732e737667" alt="Open Source Helpers"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://camo.githubusercontent.com/76f0e887c183ccc31c1cb63c33d2dbf48cb2df51/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e2e737667" alt="License: MIT"></a>
  <a href="https://github.com/ellerbrock/open-source-badges/"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" alt="Open Source Love"></a>
  <a href="https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM"><img align="left" width="150" src="../assets/join-slack-team.png"></a>
</div>

<div dir="rtl">
<h1> תרומות ראשונות </h1>
</div>

<div dir="rtl">
זה קשה. זה תמיד קשה כשעושים משהו בפעם הראשונה. במיוחד כאשר משתפים פעולה, לעשות טעויות זה לא משהו נוח. רצינו להקל על הדרך שבה תורמים בפעם הראשונה לומדים ותורמים בפעם הראשונה.
קריאת כתבות וצפייה בסרטוני הדרכה יכולים לעזור, אבל מה יותר טוב מאשר לבצע את הדברים בסביבת למידה? המטרה של הפרויקט הזה היא לתת הכוונה ולפשט את הדרך שבה מתחילים מבצעים את התרומה הראשונה שלהם. אם אתם מחפשים לבצע את התרומה הראשונה שלכם, עקבו אחרי הצעדים למטה.
</div>

<div dir="rtl">
<h4> אם לא מתאים לכם להשתמש בטרמינל, כאן יש קישור תוך שימוש בכלים גרפיים
<a href="#הדרכות-בשימוש-כלים-אחרים">קישור לכלים גרפיים</a>.</h4>
</div>

<div dir="rtl">
<h4>ניתן לקרוא את המאמר
<a href="">בשפות אחרות</a>.</h4>
</div>

<div dir="rtl">
<a href="https://help.github.com/articles/set-up-git/">אם אין לכם GIT ניתן להתקין GIT בקישור</a>
</div>

<div dir="rtl">
<a href="/Roshanjossey/first-contributions/blob/master/assets/fork.png"><img img style="float: left;" width="300" src="../assets/fork.png" alt="fork this repository"></a>
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
  <img align="left" width="300" src="../assets/clone.png" alt="clone this repository" />
</div>

<div dir="rtl">
  
כעת, שכפלו את המאגר הזה למחשב שלכם. לכו לדף ה-GitHub שלכם, לחצו על כפתור השכפול ואז לחצו על הצלמית `העתק ללוח`
פתחו טרמינל והריצו את הפקודה הבאה:
</div>

```
git clone "url you just copied"
```
<div dir="rtl">
  
כאשר הביטוי `"url you just copied"` (ללא סימני הגרשיים) הוא הקישור למאגר שביצעתם עליו FORK מקודם. ראו את הצעדים הקודמים כדי להשיג את הקישור.
</div>

<img align="left" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

<div dir="rtl">
לדוגמא:
</div>

```
git clone https://github.com/this-is-you/first-contributions.git
```
<div dir="rtl">
  
כאשר `this-is-you` הוא שם המשתמש שלכם ב-GitHub. כאן, אתם מעתיקים את התוכן של מאגר first-contributions ב-GitHub לתוך המחשב שלכם.
</div>

<div dir="rtl">
<h2> יצירת ענף </h2>
</div>

<div dir="rtl">
תחליפו לתיקיית המאגר בתוך המחשב שלכם (אם אתם כבר לא נמצאים שם):
</div>

```
cd first-contributions
```
<div dir="rtl">
  
כעת, תצרו ענף בשימוש הפעולה `git checkout`:
</div>

```
git checkout -b <add-your-new-branch-name>
```
<div dir="rtl">
  לדוגמא:
</div>

```
git checkout -b add-alonzo-church
```

<div dir="rtl">
(שם הענף לא חייב להכיל את המילה add בתוכו, אבל זה הגיוני להוסיף אותה מכיוון שהמטרה של הענף היא להוסיף את השם שלכם לרשימה)
</div>

<div dir="rtl">
<h2> ערכו שינויים הכרחיים ובצעו להם commit </h2>
</div>

<div dir="rtl">
  
כעת תפתחו את הקובץ, `Contributors.md` בתוכנת עריכת טקסט והוסיפו את השם שלכם אליו. אל תוסיפו את השם בתחילת הקובץ או בסופו. הוסיפו אותו באמצע. לאחר שסיימתם, שמרו את הקובץ.


אם תנווטו לתיקיית הפרויקט ותבצעו את הפעולה `git status`, תוכלו לראות את השינויים שביצעתם שם.
הוסיפו את השינויים האלו לענף שיצרתם תוך שימוש בפקודה `git add`:
</div>

```
git add Contributors.md
```
<div dir="rtl">
  
עכשיו, בצעו(commit) את שינויים הללו תוך שימוש בפקודת `git commit`:
</div>

```
git commit -m "Add <your-name> to Contributors list"
```
<div dir="rtl">
  
החליפו את הביטוי `<your-name>` .עם השם שלכם
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
  
החליפו את `<add-your-branch-name>` .עם השם של הענף שיצרתם מוקדם יותר
</div>

<div dir="rtl">
<h2> הגישו את השינויים שלכם לסקירה </h2>
</div>

<div dir="rtl">
  
אם תלכו למאגר שלכם ב-GitHub, אתם תראו כפתור עם הכיתוב `Compare & pull request`. לחצו על כפתור זה.

<img style="float: left;" src="../assets/compare-and-pull.png" alt="create a pull request" />

כעת, הגישו את בקשת הדחיפה (pull request):

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

בקרוב, אני אצרף את כל השינויים לתוך הענף הראשי של פרויקט זה. אתם תקבלו עדכון במייל ברגע שהשינויים ימוזגו.
</div>

<div dir="rtl">
<h2>מחקו את הענף שלכם אחרי שבקשת הדחיפה אושרה</h2>
</div>

<div dir="rtl">
<h2>מה לעשות מכאן?</h2>
</div>

<div dir="rtl">
כל הכבוד! כרגע סיימתם את מעגל הזרימה הסטנדרטי של Fork->Clone->Edit->PR שאתם תפגשו באופן שכיח כתורמים!
חגגו את התרומה שלכם ושתפו אותה עם חברים שלכם ועוקבים שלכם בכך שתלכו ל-<a href="https://firstcontributions.github.io/#project-list">web app</a>.
אתם יכולים להצטרף לצוות הסלאק שלנו אם אתם צריכים עזרה או אם יש לכם שאלות.
<a href="https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY">הצטרפו לקבוצת סלאק</a>.

עכשיו אפשר להתחיל לתרום לפרוייקטים אחרים. הכנו רשימה של פרוייקטים על נושאים קלים שאתם יכולים להתחיל לעבוד עליהם.

<a href="https://roshanjossey.github.io/first-contributions/#project-list">רשימה של פרוייקטים ב-web app</a>.
</div>

<div dir="rtl">
<h3><a href="additional-material/git_workflow_scenarios/additional-material.md">חומר נוסף</a></h3>
</div>

<div dir="rtl">
<h2>הדרכות בשימוש כלים אחרים</h2>
</div>

<div dir="rtl">
  <table style="width:100%">
    <tr>
      <th><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></th>
      <th><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></th>
      <th><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></th>
    </tr>
    <tr>
      <th><a href="gitkraken-tutorial.md">GitKraken</a></th>
      <th><a href="github-windows-vs2017-tutorial.md">Visual Studio 2017</a></th>
      <th><a href="github-desktop-tutorial.md">GitHub Desktop</a></th>
    </tr>
  </table>
</div>
