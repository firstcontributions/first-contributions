# Bir başka dala bir işlem taşıma
Eğer bir işlem yaparsan ve yanlış kolu değiştirdiğinizi fark ettiysen?
Bu hatayı nasıl düzeltebilirim? Bu soruya bu soru cevaplanmaktadır.

## Son işlemleri mevcut dala taşı
Bu hareketi yapmak için şunu yazın:

```git reset HEAD~ --soft``` - Son işlemi iptal eder, ancak yapılan değişiklikleri kaydeder.

```git stash``` - Dizinin durumunu kaydeder.

```git checkout <имя правильной ветки>``` - Başka bir şubeye geçer.

```git stash pop```- Son kaydedilen durumu döndürür.

```git add .```- Tek tek dosyalar ekler.

```git commit -m "ваш комментарий"``` - Değişiklikleri kaydeder ve kaydeder.

Şimdi değişiklikleriniz doğru dalda.


### Son işlemleri yeni dala taşı

Bu hareketi yapmak için şunu yazın:
```git branch newbranch``` - Tüm işleri kaydederek yeni bir şube oluşturur.
```git reset --hard HEAD~[n]``` - Ana dalı işlemlere geri döndürür. Bu işlemlerde yer alan değişikliklerin ana daldan tamamen kaldırılacağını unutmayın.
```git checkout newbranch``` - Oluşturduğunuz şubeye geçer. Bu dal şu anda tüm işlemleri içermektedir.

Unutmayın: İşlemde yer almayan değişiklikler tamamen KAYIP olacaktır.
