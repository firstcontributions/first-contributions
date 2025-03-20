# Git Konfigürasyonu

İlk kez bir commit yapmaya çalıştığınızda aşağıdaki mesajı görmüş olabilirsiniz:

```
$ git commit
*** Lütfen kim olduğunuzu söyleyin.

Hesabınızın varsayılan kimliğini ayarlamak için şu komutu çalıştırın:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

Sadece bu depoda kimliği ayarlamak için --global seçeneğini kullanmayın.
Bir commit oluşturmak için Git, kimin tarafından yapıldığını bilmelidir. Ekip çalışmalarında, projenin belirli kısımlarının kim tarafından ve ne zaman değiştirildiğini bilmek önemlidir. Bu nedenle Git, her commit'in bir kullanıcı adı ve e-posta adresiyle ilişkilendirilmesini gerektirir.

Bu bilgiyi Git ile ilişkilendirmenin birkaç yolu vardır ve burada bazılarını listeleyeceğiz.

Global Konfigürasyon

Global konfigürasyonda kaydedilen bilgiler, tüm sistem için geçerlidir, yani çalıştığınız tüm depoları kapsar. Bu, çoğu kullanım durumu için tercih edilen yöntemdir.

Global konfigürasyona bir şey kaydetmek için config komutunu aşağıdaki şekilde kullanırsınız:


$ git config --global <değişken adı> <değer>
Kullanıcı bilgileri için bu komutları şu şekilde çalıştırabilirsiniz:

$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
Depo Konfigürasyonu

Adından da anlaşılacağı gibi, bu konfigürasyonlar yalnızca mevcut depo için geçerlidir. Örneğin, işle ilgili bir projede şirket e-posta adresinizi kullanmak istiyorsanız bu yöntemi kullanabilirsiniz.

Depo düzeyinde konfigürasyon yapmak için config komutunda --global anahtarını kullanmazsınız:

$ git config <değişken adı> <değer>
Kullanıcı bilgileri için bu şu şekilde görünür:

$ git config user.email "you@alternate.com"
$ git config user.name "Your Name"
Komut Satırı Konfigürasyonu

Bu konfigürasyon yöntemi yalnızca belirli bir komut için geçerlidir. Tüm Git komutları, komuttan önce -c anahtarını kullanarak geçici konfigürasyon parametreleri ayarlamanıza izin verir.

Konfigürasyon parametrelerini yalnızca belirli bir komut için geçici olarak değiştirmek için Git komutlarını aşağıdaki formatta kullanın:

$ git -c <değişken-1>=<değer> -c <değişken-2>=<değer> <komut>
Commit komutu için bu şu şekilde olacaktır:

git -c user.name='Your Name' -c user.email='you@example.com' commit -m "Commit mesajınız"
Öncelik Sırası Hakkında Not

Üç konfigürasyon türü arasındaki öncelik sırası şu şekildedir: komut satırı > depo > global. Bu, bir değişken hem global hem de komut satırında tanımlanmışsa, komut satırında atanan değerin kullanılacağı anlamına gelir.

Sadece Kullanıcı Bilgisi Değil

Şimdiye kadar Git konfigürasyonunu yalnızca kullanıcı bilgisi bağlamında ele aldık. Ancak Git, başka parametreleri de yapılandırmanıza izin verir. İşte bunlardan bazıları:

core.editor - Commit mesajlarını düzenlemek için kullanılacak metin düzenleyicisini belirtir.
commit.template - Commit mesajları için bir şablon dosyası belirtir.
color.ui - Git mesajlarında renkli çıktı kullanılıp kullanılmayacağını belirten mantıksal bir değişkendir.
Basitlik adına bazı detayları atladık. Daha fazla bilgi için git-scm.com adresine başvurabilirsiniz.

Bu şekilde tüm içerik **tek bir Markdown** dosyasında birleştirilmiş ve Türkçe olarak sunulmuştur.