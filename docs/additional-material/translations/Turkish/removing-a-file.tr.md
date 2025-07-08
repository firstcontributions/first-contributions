# GIT kontrolünden bir dosyayı kaldırma

Bazen bir dosyayı GIT kontrolünden kaldırmanız gerekebilir, ancak onu bilgisayarınızda tutmanız gerekebilir. Bu, aşağıdaki komut kullanılarak gerçekleştirilebilir:

``git rm <dosya> --cached``

## Ne oldu?

GIT artık uzak dosyadaki değişiklikleri izlemiyor. GIT perspektifinden bakıldığında bu dosya eksiktir, ancak bu dosyayı dosya sisteminde bulmaya çalışırsanız, hala orada olduğunu göreceksiniz.

Yukarıdaki örnekte `--cached` bayrağının kullanıldığına dikkat edin. Eğer bu bayrağı eklemezsek Git dosyayı sadece depodan değil aynı zamanda dosya sisteminizden de silecektir.

`git commit -m "Remove file1.js"` ile bir değişikliği onaylayıp `git push origin master` ile uzak depoya gönderirseniz, uzak depo dosyayı silecektir.

## Ek Bilgiler

- Birden fazla dosyayı silmek istiyorsanız, tüm dosyaları tek bir komutta listeleyerek bunu yapabilirsiniz:

 `git rm dosya1.js dosya2.js dosya3.js --cached`

- Benzer adlara sahip dosyaları silmek için joker karakteri (*) kullanabilirsiniz; örneğin, yerel depoda bulunan tüm .txt dosyalarını silmek istiyorsanız şunu yazın:

 `git rm *.txt --cached`