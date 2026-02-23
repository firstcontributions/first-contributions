[1mdiff --git a/README.md b/README.md[m
[1mindex 69e2b7d0..09026b8b 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -1,246 +1,249 @@[m
[31m-[![Open Source Love](https://firstcontributions.github.io/open-source-badges/badges/open-source-v1/open-source.svg)](https://github.com/firstcontributions/open-source-badges)[m
[31m-[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)[m
[31m-[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)[m
[31m-[m
[31m-#### _Read this in [other languages](docs/translations/Translations.md)._[m
[31m-<kbd>[<img title="Shqip" alt="Shqip" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/al.svg" width="22">](docs/translations/README.al.md)</kbd>[m
[31m-<kbd>[<img title="Armenian" alt="Armenian" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/am.svg" width="22">](docs/translations/README.arm.md)</kbd>[m
[31m-<kbd>[<img title="Uzbek" alt="Uzbek language" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/uz.svg" width="22">](docs/translations/README.uz.md)</kbd>[m
[31m-<kbd>[<img title="Azərbaycan dili" alt="Azərbaycan dili" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/az.svg" width="22">](docs/translations/README.aze.md)</kbd>[m
[31m-<kbd>[<img title="বাংলা" alt="বাংলা" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/bd.svg" width="22">](docs/translations/README.bn.md)</kbd>[m
[31m-<kbd>[<img title="Bulgarian" alt="Bulgarian" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/bg.svg" width="22">](docs/translations/README.bg.md)</kbd>[m
[31m-<kbd>[<img title="Português (Brasil)" alt="Português (Brasil)" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/br.svg" width="22">](docs/translations/README.pt_br.md)</kbd>[m
[31m-<kbd>[<img title="Català" alt="Català" src="https://firstcontributions.github.io/assets/Readme/catalan1.png" width="22">](docs/translations/README.ca.md)</kbd>[m
[31m-<kbd>[<img title="中文 (Simplified)" alt="中文 (Simplified)" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/cn.svg" width="22">](docs/translations/README.zh-cn.md)</kbd>[m
[31m-<kbd>[<img title="Czech" alt="Czech" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/cz.svg" width="22">](docs/translations/README.cs.md)</kbd>[m
[31m-<kbd>[<img title="Deutsch" alt="Deutsch" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/de.svg" width="22">](docs/translations/README.de.md)</kbd>[m
[31m-<kbd>[<img title="Dansk" alt="Dansk" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/dk.svg" width="22">](docs/translations/README.da.md)</kbd>[m
[31m-<kbd>[<img title="المصرية" alt="المصرية" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/eg.svg" width="22">](docs/translations/README.eg.md)</kbd>[m
[31m-<kbd>[<img title="Dezéiriya" alt="Dezéiriya" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/dz.svg" width="22">](docs/translations/README.dz.md)</kbd>[m
[31m-<kbd>[<img title="Español de España" alt="Español de España" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/es.svg" width="22">](docs/translations/README.es.md)</kbd>[m
[31m-<kbd>[<img title="Française" alt="Française" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/fr.svg" width="22">](docs/translations/README.fr.md)</kbd>[m
[31m-<kbd>[<img title="Gaeilge" alt="Gaeilge" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/ie.svg" width="22">](docs/translations/README.ga.md)</kbd>[m
[31m-<kbd>[<img title="Galego" alt="Galego" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Galicia.svg/1200px-Flag_of_Galicia.svg.png" width="22">](docs/translations/README.gl.md)</kbd>[m
[31m-<kbd>[<img title="Ελληνικά" alt="Ελληνικά" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/gr.svg" width="22">](docs/translations/README.gr.md)</kbd>[m
[31m-<kbd>[<img title="ქართული" alt="ქართული" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/ge.svg" width="22">](docs/translations/README.ge.md)</kbd>[m
[31m-<kbd>[<img title="Magyar" alt="Magyar" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/hu.svg" width="22">](docs/translations/README.hu.md)</kbd>[m
[31m-<kbd>[<img title="Bahasa Indonesia" alt="Bahasa Indonesia" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/id.svg" width="22">](docs/translations/README.id.md)</kbd>[m
[31m-<kbd>[<img title="עִברִית" alt="עִברִית" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/il.svg" width="22">](docs/translations/README.hb.md)</kbd>[m
[31m-<kbd>[<img title="ગુજરાતી / हिन्दी / मराठी / മലയാളം / ಕನ್ನಡ / తెలుగు / ଓଡିଆ / छत्तीसगढ़ी / ਪੰਜਾਬੀ" alt="ગુજરાતી / हिन्दी / मराठी / മലയാളം / ಕನ್ನಡ / తెలుగు / ଓଡିଆ / छत्तीसगढ़ी / ਪੰਜਾਬੀ" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/in.svg" width="22">](docs/translations/Translations.md)</kbd>[m
[31m-<kbd>[<img title="தமிழ்" alt="தமிழ்" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/lk.svg" width="22">](docs/translations/README.ta.md)</kbd>[m
[31m-<kbd>[<img title="فارسی" alt="فارسی" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Iran_before_1979_Revolution.svg" width="22">](docs/translations/README.fa.md)</kbd>[m
[31m-<kbd>[<img title="Italiano" alt="Italiano" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/it.svg" width="22">](docs/translations/README.it.md)</kbd>[m
[31m-<kbd>[<img title="日本語" alt="日本語" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/jp.svg" width="22">](docs/translations/README.ja.md)</kbd>[m
[31m-<kbd>[<img title="සිංහල" alt="සිංහල" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/lk.svg" width="22">](docs/translations/README.si.md)</kbd>[m
[31m-<kbd>[<img title="Kiswahili (Kenya)" alt="Kiswahili (Kenya)" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/ke.svg" width="22">](docs/translations/README.kws.md)</kbd>[m
[31m-<kbd>[<img title="한국어" alt="한국어" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/kr.svg" width="22">](docs/translations/README.ko.md)</kbd>[m
[31m-<kbd>[<img title="Lietuvių kalba" alt="Lietuvių kalba" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/lt.svg" width="22">](docs/translations/README.lt.md)</kbd>[m
[31m-<kbd>[<img title="Limba Română" alt="Limba Română" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/md.svg" width="22"> <img title="Limba Română" alt="Limba Română" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/ro.svg" width="22">](docs/translations/README.ro.md)</kbd>[m
[31m-<kbd>[<img title="မြန်မာ" alt="မြန်မာ" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/mm.svg" width="22">](docs/translations/README.mm_unicode.md)</kbd>[m
[31m-<kbd>[<img title="Македонски" alt="Македонски" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/mk.svg" width="22">](docs/translations/README.mk.md)</kbd>[m
[31m-<kbd>[<img title="Español de México" alt="Español de México" src="https://cdn.jsdelivr.net/gh/hampusborgos/country-flags@main/svg/mx.svg" width="22">](docs/translations/README.mx.md)</kbd>[m
[31m-<kbd>[<img title="Bahasa Melayu / بهاس ملايو‎ / Malay" alt="Bahasa Melayu / بهاس ملايو�