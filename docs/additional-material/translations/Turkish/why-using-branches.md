## Katkıda Bulunurken Neden Branch Kullanılır?

Git branch’leri, yazılım geliştirmede iş birliği için kritik bir araçtır. Birden fazla geliştiricinin, ana proje koduna müdahale etmeden aynı anda farklı özellikler veya hata düzeltmeleri üzerinde çalışmasına olanak tanır. Branch kullanarak özgürce denemeler yapabilir, yeni fikirleri test edebilir ve yalnızca en iyi değişiklikleri ana projeye dahil edebilirsiniz.

---

## Branch Nedir?

Git’te bir **branch (dal)**, aslında geliştirme sürecinin ayrı bir hattıdır. Projenin ana kod tabanını etkilemeden değişiklik yapabileceğiniz izole bir ortam oluşturmanızı sağlar. Hazır olduğunuzda, bu branch’i ana projeyle birleştirebilirsiniz.

### Branch’ler Nasıl Çalışır?

Her branch, proje geçmişindeki belirli bir commit’e işaret eden bir pointer’dır. Yeni bir branch oluşturduğunuzda, Git mevcut branch’in durumunu kopyalar ve bağımsız çalışmanıza olanak tanır. Yeni commit’ler bu branch’in geçmişine eklenir ve ana branch’i etkilemez.

- Branch’ler arasında geçiş yapmak için `git checkout` kullanılır.
- Bir branch’teki değişiklikleri diğerine aktarmak için `git merge` kullanılır.

---

## Neden Branch Kullanılır?

Branch’ler iş birliğini **daha düzenli ve verimli** hale getirir. Eğer branch kullanılmazsa, tüm değişiklikler doğrudan ana proje üzerinde yapılır ve bu da karmaşaya, hatalara ve çakışmalara yol açar.

---

## Örnek: Araba Boyama Analojisi 🚗

Bir araba üretim ekibinin yeni model için varsayılan renk seçtiğini düşünün. Başlangıçta araba **zeytin yeşili** olarak belirlenmiş olsun. Ancak bazı ekip üyeleri arabanın **kırmızı** halini görmek istiyor.

- Orijinal arabayı boyamak yerine, **kırmızı bir prototip** oluştururlar.
- Eğer kırmızı renk beğenilirse, ana modelin yerini alır (yani branch merge edilir).
- Eğer beğenilmezse, prototip atılır (yani branch silinir).

Git’te de aynı şekilde, branch’ler ana kodu bozmadan yeni özellikleri test etmenizi sağlar.

---

## Feature Branching (Özellik Bazlı Branch Kullanımı)

Her geliştirici için bir branch oluşturmak yerine, **her özellik için bir branch** oluşturmak daha iyi bir yaklaşımdır. Bu, düzeni korur ve gereksiz çakışmaları önler.

### Örnek: Alice ve Bob

- **Alice**, **Feature A** üzerinde çalışıyor ve birkaç commit yapıyor.
- Daha sonra **Feature C**’ye geçip commit’ler ekliyor.
- Bu sırada **Bob**, **Feature B**’yi bitirip **Feature A** üzerinde çalışmak istiyor.
- Bob, Alice’in branch’ini çekiyor ama içinde **Feature A, Feature B ve tamamlanmamış Feature C** de var.
- Merge etmeye çalıştığında, Feature C tamamlanmadığı için conflict (çakışma) yaşıyor.

Bunu önlemek için:

- Alice, **Feature A** ve **Feature C** için ayrı branch’ler açmalı.
- Bob da **Feature B** ve **Feature A** için ayrı branch’ler kullanmalı.

Bu sayede herkes birbirini etkilemeden çalışabilir.

---

## Branch Oluşturma ve Yönetme

### Yeni Branch Oluşturma

```sh
git branch my-new-branch
```

Bu komut, `my-new-branch` adında yeni bir branch oluşturur ancak o branch’e geçmez.

---

### Branch’e Geçiş

```sh
git checkout my-new-branch
```

Bu komut sizi `my-new-branch` branch’ine geçirir.

---

### Tek Komutla Oluştur ve Geç

```sh
git checkout -b my-new-branch
```

Bu komut hem branch oluşturur hem de o branch’e geçer.

---

### Branch Silme (Merge Edildiyse)

```sh
git branch -d my-new-branch
```

Bu komut, merge edilmiş branch’i siler.

---

### Zorla Branch Silme (Merge Edilmemiş Olsa Bile)

```sh
git branch -D my-new-branch
```

Dikkatli kullan! Merge edilmemiş değişiklikleri de siler.

---

## Ek Kaynaklar
- [Git Branching Rehberi (Atlassian)](https://www.atlassian.com/git/tutorials/using-branches)
- [Repository’den Branch Silme](https://github.com/jashnimje/first-contributions/blob/7dcae72208e4b42fcf834b4f189fa8ee78238077/additional-material/git_workflow_scenarios/removing-branch-from-your-repository.md)