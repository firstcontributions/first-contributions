# Dalınızı Ana Depo ile Senkronize Etme

Öncelikle, tam senkronizasyon için akışı anlamak önemlidir. Bu senaryoda 3 farklı depo bulunur: Github'daki açık depom github.com/firstcontributions/first-contributions.git, GitHub'daki çatal deponuz github.com/Your-Name/first-contributions/ ve üzerinde çalıştığınız yerel makinenizdeki depo. Bu tür bir işbirliği, açık kaynak projeler için tipiktir ve Triangle Workflows olarak adlandırılır.

<img style="float;" src="https://firstcontributions.github.io/assets/additional-material/triangle_workflow.png" alt="triangle workflow" />

Deponuzu benim açık depomla güncel tutmak için önce ana depoyu yerel deponuzla birleştirmeliyiz.
İkinci adımımız, yerel deponuzu GitHub'daki çatal deponuza itmektir. Daha önce gördüğünüz gibi, yalnızca "çatal depo" ile bir "pull request" isteyebilirsiniz. Bu nedenle, GitHub'daki çatal depo, güncellenmesi gereken son depodur.

Şimdi bunu nasıl yapacağımıza bir göz atalım:

Senkronizasyon Adımları

1. Ana Dal (master) Üzerine Geçin

Öncelikle ana dalda olduğunuzdan emin olun. Hangi dalda olduğunuzu öğrenmek için şu komutu çalıştırın:

* git status

Eğer ana dalda (master) değilseniz, ana dala geçin:

* git checkout master

2. Ana Depoyu upstream Olarak Ekleyin

Yerel deponuzu ana depo ile senkronize etmek için önce ana depoyu upstream olarak ekleyin:

* git remote add upstream https://github.com/firstcontributions/first-contributions.git

Bu komut, Git'e belirttiğiniz adreste bu projenin başka bir versiyonunun bulunduğunu ve bunu upstream olarak adlandırdığımızı söyler.

3. upstream'den Son Değişiklikleri Alın

Ardından, ana depodan en son değişiklikleri alın:

* git fetch upstream

Bu komut, upstream (ana depo) üzerindeki tüm son değişiklikleri yerel deponuza indirir.

4. upstream/master ile Birleştirin

Şimdi, ana depodaki değişiklikleri yerel ana dalınızla birleştirin:

git rebase upstream/master
Bu komut, ana depodaki değişiklikleri yerel ana dalınızla birleştirir. Yerel ana dalınız artık günceldir.

5. Yerel Depoyu GitHub Çatal Deponuza İtin

Son olarak, yerel ana dalınızı GitHub'daki çatal deponuza itin:

* git push origin master

Bu komut, yerel deponuzdaki değişiklikleri GitHub'daki çatal deponuza gönderir. Artık tüm depolarınız günceldir!
