# Ek bilgi

Buraya gelmeden önce temel eğitimi tamamladığınızı varsayıyoruz. Bu belge size gelişmiş Git teknikleri hakkında bazı ek bilgiler verecektir.

### [Bir commit<sup>1</sup>'i değiştirme](../git_workflow_scenarios/amending-a-commit.md)

Bu belge, remote repo<sup>2</sup>'daki bir commit<sup>1</sup>'in nasıl değiştirileceği hakkında bilgi sağlar.

> Yaptığınız bir commit<sup>1</sup>'i ayarlamanız gerektiğinde bunu kullanın.

### [Git'in yapılandırılması](../git_workflow_scenarios/configuring-git.md)

Bu belge, Git'te kullanıcı ayrıntılarının ve diğer seçeneklerin nasıl yapılandırılacağı hakkında bilgi sağlar.

> Git yapılandırmalarınızı daha iyi kontrol etmek için bunu kullanın.

### [Fork<sup>3</sup>'unuzu depoyla senkronize tutma](../git_workflow_scenarios/keeping-your-fork-synced-with-this-repository.md)

Bu belge, fork<sup>3</sup> edilmiş deponuzu ana depoyla nasıl güncel tutacağınız hakkında bilgi sağlar. Bu, siz ve birçok kişinin bu projeye katkıda bulunacağını umut ettiğimizden dolayı önemlidir.

> Fork<sup>3</sup>'unuzun ana depoda herhangi bir değişikliği yoksa bu adımları izleyin.

### [Bir commit<sup>1</sup>'i farklı bir branch<sup>4</sup>'a taşıma](../git_workflow_scenarios/moving-a-commit-to-a-different-branch.md)

Bu belge, bir commit<sup>1</sup>'in başka bir branch<sup>4</sup>'a nasıl taşınacağı hakkında bilgi sağlar.

> Bir commit<sup>1</sup>'i başka bir branch<sup>4</sup>'a taşımak için bu adımları atın.

### [Bir dosyayı kaldırma](../git_workflow_scenarios/removing-a-file.md)

Bu belge, yerel deponuzdan bir dosyanın nasıl kaldırılacağı hakkında bilgi sağlar.

> Commit<sup>1</sup>'ten önce bir dosyanın nasıl kaldırılacağını öğrenmek için bu adımları izleyin.

### [Repo<sup>5</sup>'nuzdan bir branch<sup>4</sup>'i kaldırma](../git_workflow_scenarios/removing-branch-from-your-repository.md)

Bu belge, bir branch<sup>4</sup>'in repo<sup>3</sup>'nuzdan nasıl silineceği hakkında bilgi sağlar.

> Bu adımları yalnızca PR<sup>6</sup>'ınız birleştirildikten sonra yapın.

### [Merge conflict<sup>7</sup>'leri çözme](../git_workflow_scenarios/resolving-merge-conflicts.md)

Bu belge, merge conflict<sup>7</sup>'lerin nasıl çözüleceği hakkında bilgi sağlar.

> Can sıkıcı merge conflict<sup>7</sup>'leri çözmek için bu adımları uygulayın.

### [Bir commit<sup>1</sup>'i geri alma](../git_workflow_scenarios/reverting-a-commit.md)

Bu belge, remote repo<sup>2</sup>'daki bir commit<sup>1</sup>'in nasıl geri alınacağı hakkında bilgi sağlar. Github'a gönderilmiş bir commit<sup>1</sup>'i geri almanız gerektiğinde kullanışlı olacaktır.

> Bir commit<sup>1</sup>'i geri almak istiyorsanız bu adımları uygulayın.

### [Commit<sup>1</sup>'leri squash<sup>8</sup>'lama](../git_workflow_scenarios/squashing-commits.md)

Bu belge, interaktif bir rebase<sup>9</sup> ile commit<sup>1</sup>'lerin nasıl squash<sup>8</sup> edileceği hakkında bilgi sağlar.

> Açık kaynaklı bir projede bir PR<sup>6</sup> açmak istiyorsanız ve gözden geçiren kişi sizden bilgilendirici bir commit<sup>1</sup> mesajı ile bütün commit<sup>1</sup>'leri bir araya getirmenizi isterse bunu kullanın.

### [Yerel bir commit<sup>1</sup>'i geri alma](../git_workflow_scenarios/undoing-a-commit.md)

Bu belge, yerel deponuzdaki bir commit<sup>1</sup>'in nasıl geri alınacağı hakkında bilgi sağlar. Yerel deponuzu karıştırdığınızı hissettiğinizde ve yerel depoyu sıfırlamak istediğinizde yapmanız gereken budur.

> Yerel bir commit<sup>1</sup>'i geri almak/sıfırlamak istiyorsanız bu adımları uygulayın.

### [Faydalı bağlantılar](../git_workflow_scenarios/Useful-links-for-further-learning.md)

Bu belge, hayatımızı kolaylaştıran tüm ipuçları ve püf noktaları web sitelerine, blog gönderilerine ve yardımcı sitelere adanmıştır. İster yeni başlayan ister uzman olsun, tüm ihtiyaçlarımıza hizmet etmek için harika bir referanstır. Bu sayfa, açık kaynak alanında yeni olan herkese veya daha fazlasını öğrenmek isteyen herkese yardımcı olacak tüm bu faydalı bağlantıların bir dizini görevi görmelidir.

### [Bir .gitignore dosyası oluşturma](../git_workflow_scenarios/creating-a-gitignore-file.md)

Bu belge, bir .gitignore dosyasının ne yaptığını, neden kullanılacağını ve bir .gitignore dosyasının nasıl oluşturulacağını açıklar. Bu dosya hemen hemen tüm Git projelerinde kullanılır. Git'e yalnızca gerekli dosyaları kaydetmeye yardımcı olur.

## Mini Sözlük:

1. Commit, kelime anlamı olarak “işlemek” demektir. Git'e eklediğimiz dosyaları kalıcı olarak Git veri tabanına işlemeye commit denir. [Tanım kaynağı](https://medium.com/@mustafazahidefe/git-notlar%C4%B1-3-git-commit-96439510aef0)
2. Remote repository, en basit anlamda tüm ekibin erişimi olan dosya sunucusudur. Bu sayede, dosyalar yerelde sınırlı kalmaz, takım çalışması için İnternet'e açılır. [Tanım kaynağı](https://aliozgur.gitbooks.io/git101/content/remote_repositoryler/)
3. Fork, Github'daki herhangi bir projeyi kullanıcının Github hesabı altında çoğaltmaya yarar. Bu şekilde, Katkı yapmak istenilen projenin birebir kopyası oluşturulur. [Tanım kaynağı](https://cangelis.com/git-ile-acik-kaynakli-projelere-katkida-bulunmak/)
4. Branch, projelerin dallara ayrılmasını, akabinde ana programı bozmadan paralel değişiklikler yapılmasını sağlar. [Tanım kaynağı](https://medium.com/@mustafazahidefe/git-notlar%C4%B1-5-branch-kavram%C4%B1-d176626711a4)
5. Repo (repository), projelerin dosyalarının, GitHub'ın alanında veya yerelde depolandığı bir dizindir. [Tanım kaynağı](https://www.hostinger.web.tr/rehberler/github-nedir/)
6. PR, yapılan katkıların bir gelişime açık projeye sunulması tekniğidir. Bu proje sahibi/sahipleri, katkıda bulunanları kabul edebilir veya reddedebilir. [Tanım kaynağı](https://medium.com/@noteCe/git-source-tree-6-27a5143c8ee7)
7. Merge Conflict ya da çakışma, iki kişinin aynı dosyadaki aynı satırı değiştirmesinden kaynaklanan merge (birleştirme) hatasıdır. [Tanım kaynağı](https://www.mobilhanem.com/git-merge-conflict/)
8. Squash, herhangi bir branch'deki commit'lerin bir kısmını birleştirip tek bir commit olarak yeniden oluşturmak için yapılan işlemdir. [Tanım kaynağı](http://aliozgur.net/2020/05/28/git-squash/)
9. Rebase, bir branch üzerindeki commit'lerin commit mesajlarının değiştirilmesi, drop edilmesi, sırasının değiştirilmesi veya bütün commit'lerin tek bir commit haline getirilmesi gibi çeşitli aksiyonları yapmamızı sağlayan bir araçtır. [Tanım kaynağı](https://aliozgur.gitbooks.io/git101/content/alistirmalar/Gun_10.html)
