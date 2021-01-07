
#

# pahala yogadaan

is pariyojana ka uddeshy shuruaatee logon ko apana pahala yogadaan dene ke tareeke ko saral aur nirdeshit karana hai. yadi aap apana pahala yogadaan dena chaahate hain, to neeche die gae charanon ka paalan karen.

yadi aap kamaand lain ke saath sahaj nahin hain, [to yahaan gui tool ka upayog karake tyootoriyal hain.](#tutorials-using-other-tools)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### yadi aapake paas apanee masheen par git nahin hai, to [ise sthaapit karen] (https://hailp.github.chom/artichlais/sait-up-git/)

## Fork this repository

is prshth ke sheersh par sthit phork batan par klik karake is ripojitaree ko phork karen.
yah aapake khaate mein is bhandaar kee ek prati banaega.

## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

ab kaante vaale bhandaar ko apanee masheen par klon karen. apane github khaate mein jaen, kaanta hua ripojitaree kholen, kod batan par klik karen aur phir klipabord_ aaikan par _chopy klik karen.

ek tarminal kholen aur nimnalikhit git kamaand chalaen:

```
git clone "url you just copied"
```
jahaan "url aapane abhee kopee kiya hai" (uddharan chihnon ke bina) is ripojitaree (is projekt ka aapaka kaanta) ke lie url hai. url praapt karane ke lie pichhale charan dekhen.

## Create a branch

apane kampyootar par ripojitaree daayarektaree mein badalen (yadi aap pahale se nahin hain):

```
cd first-contributions
```

ab `git checkout` kamaand ka upayog karake ek shaakha banaen:

```
git checkout -b your-new-branch-name
```

udaaharan ke lie:

```
git checkout -b add-alonzo-church
```

(shaakha ke naam ko isamen _add_ shabd rakhane kee aavashyakata nahin hai, lekin ise shaamil karana ek uchit baat hai kyonki is shaakha ka uddeshy aapaka naam soochee mein jodana hai.)

## apne parivartan karain or phir un parivartanon ko commit karain

ab ek tekst editar mein `Contributors.md` phail kholen, isamen apana naam joden. ise fail ke aarambh ya ant mein na joden. ise beech mein kaheen bhee rakh den. ab, fail ko sahejen.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

yadi aap projekt daayarektaree mein jaate hain aur kamaand `git status` nishpaadit karate hain, to aap dekhenge ki parivartan hain.

shaakha mein un badalaavon ko joden jinhen aapane `git add` kamaand ka upayog karake banaaya tha:

```
git add Contributors.md
```
ab `git commit` kamaand ka upayog karake un parivartanon ko karen:

```
git commit -m "Add <your-name> to Contributors list"
```

replacing `<your-name>` with your name.

## Push changes to GitHub

`git push` kamaand ka upayog karake apane parivartan push karen:

```
git push origin <add-your-branch-name>
```

aapake dvaara pahale banaee gaee shaakha ke naam ke saath `<add-your-branch-name>` badlain.

## Submit your changes for review

yadi aap github par apane repository mein jaate hain, to aapako ek `Compare & pull request` batan dikhaee dega. us batan par klik karen.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

ab pull request sabamit karen.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

jald hee main is pariyojana ke maastar braanch mein aapake sabhee parivartanon ka vilay karoonga. ek baar badalaav ke vilay ke baad aapako ek soochana eemel milega.

## yahaan se kahaan jaen?

badhaee! aapane abhee-abhee maanak_fork -> clone -> edit -> pull request_ varkaflo ko poora kiya hai jisaka aap aksar ek yogadaanakarta ke roop mein saamana karenge!

apane yogadaan ka jashn manaen aur ise apane doston aur anuyaayiyon ke saath saajha karen [web app](https://firstcontributions.github.io/#social-share).

yadi aapako kisee sahaayata kee aavashyakata hai ya koee prashn hai, to aap hamaaree sust teem mein shaamil ho sakate hain. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-iywfifau-_aMtdwTjBoMzQqzW8~YUUA).

ab aapako any pariyojanaon mein yogadaan dene ke saath shuroo karate hain. hamane un aasaan muddon vaalee pariyojanaon kee ek soochee taiyaar kee hai jin par aap shuruaat kar sakate hain. chek aaut [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)

## Tutorials Using Other Tools


| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
