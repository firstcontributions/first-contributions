# GIT kontrolünden dosya silmek

Bazen dosyayı GIT versiyon kontrolünden kaldırmak, ancak bilgisayara kaydetmek gerekebilir. 
Bu durum aşağıdaki komutla sağlanabilir:

``git rm <dosya> --cached``

## Ne oldu?

GIT artık uzak bir dosyadaki değişiklikleri kontrol etmiyor. 
GIT bakış açısından, bu dosya eksik, ancak bu dosyayı dosya sisteminde yerelleştirmeye çalışırsanız, hala yerinde olduğunu göreceksiniz.

Yukarıdaki komutta `--cached` argümanının kullanıldığını unutmayın. Bu argümanı eklememiş olsaydık, GIT dosyayı yalnızca depodan değil, aynı zamanda dosya sisteminden de siler.

Eğer file1.js dosyasını  silerseniz, `git commit -m "file1.js silindi"  komutunu çalıştırıp ekleyiniz ve `git push origin master` komutu ile uzak depoya işledikten sonra dosya uzak depodan da silinecektir.

## Ek bilgi

- Birden fazla dosyayı silmek istiyorsanız, tüm dosyaları tek bir komutta listeleyerek yapabilirsiniz:

  `git rm file1.js file2.js file3.js --cached`

- Benzer uzantıya sahip dosyaları silmek için (*) şablonunu kullanabilirsiniz; örneğin, tüm .txt dosyalarını yerel depodan silmek istiyorsanız, şunu yazın:

  `git rm *.txt --cached`
