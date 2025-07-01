# Depodan bir dalı kaldırma

Eğer şimdiye kadar eğitimi takip ettiyseniz, `<add-your-name>` dalımız amacına ulaşmıştır, onu yerel makinenizin deposundan kaldırmanın zamanı geldi. Bu gerekli değil, ancak bu endüstrinin ismi onun oldukça özel bir amacını gösteriyor. Ömrü de buna paralel olarak kısa olabilir.

Öncelikle `<add-your-name>`'inizi master'ınızla birleştirerek kendi dalınıza taşıyalım:
```
git ödeme ustası
```

`<add-your-name>`'i ana dosyaya birleştir:
```
git merge <adınızı-ekleyin> master
```

`<add-your-name>`'i yerel makinenizin depolarından kaldırın:
```
git branch -d <isminizi-ekleyin>
```

Artık yerel makine dalını `<add-your-name>` sildiniz ve her şey düzgün ve düzenli görünüyor.
Ancak bu noktada GitHub bölümünüzde hala `<add-your-name>` adlı bir dal olması gerekir. Ancak bunu silmeden önce, bu uzak daldan depolarıma bir "Çekme isteği" gönderdiğinizi unutmayın. Yani eğer bunu daha önce birleştirdiysem, bu dalı silmeyin.

Ancak, eğer sizin dalınızı birleştirdiysem ve siz uzak dalı silmek istiyorsanız, şunu kullanın:
```
git push origin --delete <isminizi-ekleyin>
```

Artık dallarınızı nasıl toparlayacağınızı biliyorsunuz.
Zamanla, kamuya açık arşivime birçok komisyon eklenecek. Hem yerel makinenizin ana dalları hem de GitHub çatalınız güncelliğini yitirecektir. Dolayısıyla, depolarınızı benimkilerle senkronize tutmak için şu adımları izleyin.

#### [Çatalınızı bu depoyla senkronize tutma](keeping-your-fork-synced-with-this-repository.md)