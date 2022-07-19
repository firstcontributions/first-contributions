# Una na Paghatag

Kini nga proyekto gitumong aron yano ug magiyahan ang paagi sa mga nagsugod sa paghimo sa ilang una nga natampo. Kung nagtinguha ka nga makahatag sa imong una nga kontribusyon, sunda ang mga lakang sa ubus.

_Kung dili ka komportable sa linya sa pagsugo, [ania ang mga panudlo nga naggamit mga gamit sa GUI.](#tutorials-using-other-tools)_

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

#### Kung wala kay git sa imohang makina, [i-install kini](https://help.github.com/articles/set-up-git/).

## Pag Fork sa tipiganan

Sa pag fork sa tipiganan pinaagi sa pag-klik sa fork button sa taas sa kini nga panid.
Maghimo kini usa ka kopya sa kini nga tipiganan sa imong account.

## I-clone ang tipiganan

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Karon i-clone ang imong tipiganan sa imong makina. Pag-adto sa imong GitHub account, ablihi ang forked repository, pag-klik sa code button ug pagkahuman i-klik ang _copy to clipboard_ icon.

Pag-abli sa usa ka terminal ug pagdagan ang mosunud nga git command:

```
git clone "url nga imong gi-kopya"
```

diin ang `kini-ikaw` mao ang imong GitHub username. Dinhi gikopya nimo ang mga sulud sa repository nga una nga natampo sa GitHub sa imong kompyuter.


For example:

```
git clone https://github.com/this-is-you/first-contributions.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

diin ang `kini-ikaw` mao ang imong GitHub username. Dinhi gikopya nimo ang mga sulud sa repository nga una nga natampo sa GitHub sa imong kompyuter.

## Paghimo usa ka Sanga(Branch)

Pagbag-o sa direktoryo sa repository sa imong computer (kung wala ka didto):

```
cd first-contributions
```

Paghimo karon usa ka sanga gamit ang mando nga `git checkout`:

```
git checkout -b imong-bag-o-nga-branch-name
```

For example:

```
git checkout -b add-alonzo-cruz
```

(Ang ngalan sa sanga dili kinahanglan nga adunay pulong nga _add_ niini, apan kini usa ka makatarunganon nga butang nga iupod tungod kay ang katuyoan niini nga sanga aron madugang ang imong ngalan sa usa ka lista.)

## Paghimo mga kinahanglan nga pagbag-o ug himua ang mga pagbag-o

Karon i-open ang `Contributors.md` file sa usa ka text editor, idugang ang imong ngalan niini. Ayaw kini idugang sa sinugdanan o katapusan sa file. Ibutang kini bisan diin taliwala. Karon, i-save ang file.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />

Kung moadto ka sa direktoryo sa proyekto ug ipatuman ang mando `git status`, makita nimo nga adunay mga pagbag-o.

Idugang kana nga mga pagbag-o sa sanga nga bag-o lang nimong gihimo gamit ang mandong `git add`:

```
git add Contributors.md
```

Karon himua ang kana nga mga pagbag-o gamit ang mando nga `git commit`:

```
git commit -m "Add <imong-ngalan> to Contributors list"
```

ilisan `<imong-ngalan>` sa imong ngalan.

## Iduso ang mga pagbag-o sa GitHub

Iduso ang imong mga pagbag-o gamit ang mando `git push`:

```
git push origin <i-add-imong-branch-name>
```

ilisdan ang `<i-add-imong-branch-name>` sa ngalan sa sanga nga una nimong gihimo.

## Isumite ang imong mga pagbag-o alang sa pagsusi

Kung moadto ka sa imong tipiganan sa GitHub, makita nimo ang usa ka butones nga `Compare & pull request`. Pag-klik sa kana nga butones.


<img style="float: right;" src="assets/compare-and-pull.png" alt="create a pull request" />

Karon isumite ang imong pull request.

<img style="float: right;" src="assets/submit-pull-request.png" alt="submit pull request" />

Sa dili madugay akong paghiusa ang tanan nimo nga mga pagbag-o sa master branch sa kini nga proyekto. Makakuha ka usa ka email sa pagpahibalo sa higayon nga ang mga pagbag-o nahiusa.

## Asa man gikan dinhi?

Congrats! Nahuman ra nimo ang naandan nga _fork -> clone -> pag-edit -> pull request_ workflow sa trabaho nga kanunay nimong masugatan ingon usa ka magtampo!

Gisaulog ang imong kontribusyon ug ipaambit kini sa imong mga higala ug sumusunod pinaagi sa pag-adto [web app](https://firstcontributions.github.io/#social-share).

Mahimo ka nga moapil sa among slack team kung kinahanglan nimo ang bisan unsang tabang o adunay mga pangutana. [Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-hfcq788y-QaXzXT5clBBWukXQyBhH4w).

Karon magsugod kita sa pagtampo sa uban pang mga proyekto. Naghiusa kami usa ka lista sa mga proyekto nga adunay dali nga mga isyu nga mahimo nimong masugdan. Pagsusi niini [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### [Additional material](additional-material/git_workflow_scenarios/additional-material.md)

## Mga Panudlo nga Naggamit Uban nga Mga Gamit

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |
