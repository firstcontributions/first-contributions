[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions

| <img alt="GitHub Desktop" src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" width="200"> | GitHub Command Line Interface (CLI) |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |

Zor gelir. Herhangi bir işi ilk kez yapmak daima zor gelir. Özellikle başkalarıyla ortak çalışıyorsanız, hata yapmak içinize sinmez. Ancak "Açık Kaynağın" temelinde işbirliği ve birlikte çalışma yatmakta. Biz, açık kaynak projelere ilk kez katkıda bulunacak kişilerin bu süreci öğrenmesini ve ilk katkılarını sunmalarını kolaylaştırmayı istiyoruz.

Makale okumak ve eğitim videoları izlemek yardımcı olabilir, fakat bir işi gerçekten yapmanın yerini ne tutabilir ki? Bu proje yeni başlayanların veya ilk defa katkıda bulunacakların işini kolaylaştırmak ve onlara rehberlik etmek amacındadır. Unutmayın ki ne kadar rahat olursanız o kadar rahat öğrenirsiniz. Eğer bir GitHub projesine ilk defa katkıda bulunacaksanız, aşağıda gösterilen basit adımları takip etmeniz yeterli olacaktır. Söz veriyoruz, eğlenceli olacak.

Bu rehber, terminalde her şeyi yapmak isteyen terminal meraklıları içindir ve [GitHub CLI](https://cli.github.com/) sayesinde bunu başarabiliriz. İlk katkınızın eğlenceli, tatmin edici ve devam etmek için motive edici olması gerektiğini unutmayın!

Bu rehber, hiç grafik arayüz kullanmadığımız için biraz daha zorlayıcıdır, ama yine de oldukça keyiflidir ve kesinlikle takip edebilirsiniz!

Öncelikle şunlara ihtiyacınız var:

- Git kurulu olmalı (nasıl kurulacağı için [git](https://git-scm.com/downloads))
- GitHub hesabı

Şimdi [resmi dokümantasyonu](https://github.com/cli/cli#installation) takip ederek sistemimize `github-cli` aracını kurmamız gerekiyor.

Ardından CLI üzerinden oturum açmamız gerekiyor, şu komutu girin:

```bash
gh auth login
```

Yönergeleri takip edin ve hazırız!

# Projeyi "forklama"

Bu komutu çalıştırmanız yeterli:

```bash
gh repo fork firstcontributions/first-contributions
```

**Önemli: Klonlamak isteyip istemediğinizi soracaktır, "yes" (evet) seçeneğini seçin.**

# Dal (Branch) oluşturma

Bu adımı git ile yapacağız; komuttaki ismi kendi isminizle değiştirin. Örneğin:

```bash
git switch -c ahmet-yilmaz-eklendi
```

# Gerekli değişiklikleri yapma ve değişiklikleri onaylama

Şimdi `Contributors.md` dosyasını bir metin düzenleyicide açın ve isminizi ekleyin. Dosyanın başı ile sonu arasındaki herhangi bir yere ekleyebilirsiniz, ardından dosyayı kaydedin.

Proje dizininde `git status` komutunu çalıştırın; değişiklikleri göreceksiniz.
<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status çıktısı" />

Biraz önce oluşturduğunuz dala bu değişiklikleri `git add` komutuyla ekleyin:
`git add Contributors.md`

Şimdi `git commit` komutunu kullanarak bu değişiklikleri onaylayın:
`git commit -m "Add <isminiz> to Contributors list"`
`<isminiz>` yerine kendi isminizi yazın.

# Değişiklikleri GitHub'a gönderme

Değişikliklerinizi `git push` komutuyla gönderin:

```
git push origin -u isminiz-eklendi
```

`isminiz-eklendi` yerine daha önce oluşturduğunuz dalın ismini yazın.

<details>
<summary> <strong>If you get any errors while pushing, click here: (Gönderme sırasında hata alırsanız buraya tıklayın)</strong> </summary>

- ### Authentication Error (Kimlik doğrulama hatası)
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Hesabınıza SSH anahtarı oluşturup yapılandırmak için [GitHub tutorial (GitHub öğreticisi)](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) bağlantısına gidin.

</details>

# Değişikliklerinizi inceleme için gönderme

Depo dizininde şu komutu çalıştırarak inceleme için bir pull request (çekme isteği) oluşturabilirsiniz:

```bash
gh pr create --repo firstcontributions/first-contributions
```

Ardından pull request'i (çekme isteğini) gönderin.

`gh status` komutunu kullanarak gönderdiğiniz pull request'i (çekme isteğini) görebilirsiniz.

## Bundan sonra ne yapabilirim?

Tebrikler! Katkıda bulunan biri olarak sıkça karşılaşacağınız standart _fork -> clone -> edit -> PR_ iş akışını tamamladınız!

Katkınızı kutlayın ve [web uygulamasına](https://firstcontributions.github.io/#social-share) giderek bunu arkadaşlarınız ve takipçilerinizle paylaşın.

Daha fazla pratik yapmak isterseniz [code contributions](https://github.com/roshanjossey/code-contributions) deposuna göz atabilirsiniz.

Artık diğer projelere katkı sunmaya hazırsınız. Çözmeye başlayabileceğiniz giriş seviyesindeki konulara (issue) sahip projeleri [web uygulamasındaki proje listesinden](https://firstcontributions.github.io/#project-list) inceleyebilirsiniz.

### [Ek bilgi](https://github.com/firstcontributions/first-contributions/blob/main/docs/additional-material/git_workflow_scenarios/additional-material.md)

## Diğer araçlarla ilgili eğitimler

| <a href="../../../gui-tool-tutorials/translations/Turkish/github-desktop-tutorial.tr.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../../../gui-tool-tutorials/translations/Turkish/github-windows-vs2017-tutorial.tr.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../../../gui-tool-tutorials/translations/Turkish/gitkraken-tutorial.tr.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../../../gui-tool-tutorials/translations/Turkish/github-windows-vs-code-tutorial.tr.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../../../gui-tool-tutorials/translations/Turkish/sourcetree-macos-tutorial.tr.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../../../gui-tool-tutorials/translations/Turkish/github-windows-intellij-tutorial.tr.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](../../../gui-tool-tutorials/translations/Turkish/github-desktop-tutorial.tr.md)                                                               | [Visual Studio 2017](../../../gui-tool-tutorials/translations/Turkish/github-windows-vs2017-tutorial.tr.md)                                                                                            | [GitKraken](../../../gui-tool-tutorials/translations/Turkish/gitkraken-tutorial.tr.md)                                                                                                         | [Visual Studio Code](../../../gui-tool-tutorials/translations/Turkish/github-windows-vs-code-tutorial.tr.md)                                                                                    | [Atlassian Sourcetree](../../../gui-tool-tutorials/translations/Turkish/sourcetree-macos-tutorial.tr.md)                                                                                                      | [IntelliJ IDEA](../../../gui-tool-tutorials/translations/Turkish/github-windows-intellij-tutorial.tr.md)                                                                                                    |

[Ana sayfaya dön](../../../translations/README.tr.md#diğer-araçlarla-ilgili-eğitimler)
