# Hal-hal yang dapat dilakukan oleh non Programmer
## Mulai mendengarkan

Semua yang ada di open source melibatkan orang lain.
Anda ingin bergabung dengan sebuah tim, dan itu berarti memahami komunitas dan cara kerjanya.
Datang ke sebuah proyek dan berkata “Hai, inilah yang saya pikir harus dilakukan oleh proyek ini” biasanya tidak dianggap sebagai hal yang baik.
Beberapa proyek mungkin akan menerima pendekatan semacam itu, tetapi jika proyek tersebut sudah berjalan cukup lama, kemungkinan sikap tersebut akan kecil.
**Mendengarkan adalah cara terbaik untuk mengetahui apa yang dibutuhkan oleh proyek.**.

1. **Bergabunglah dengan milis**: Untuk banyak proyek, milis adalah saluran utama komunikasi tentang perkembangan proyek.
Pada proyek-proyek besar, ada banyak milis yang dapat dipilih.
Sebagai contoh, proyek PostgreSQL memiliki tidak kurang dari 12 milis berorientasi pengguna dan enam milis pengembang pada halaman milisnya.
Saya sarankan Anda mengikuti milis berorientasi pengguna utama dan milis pengembang inti untuk mulai menyimak.

2. **Mengikuti sebuah blog: Blog yang dikelola oleh pengembang inti sering kali memberikan informasi tentang apa yang akan hadir di rilis mendatang,
dan apa yang diperlukan untuk mencapainya. Situs planet mengumpulkan berita dan entri blog dari banyak sumber yang terkait dengan proyek.
Jika ada situs planet, seperti planet.gnome.org atau planet.mysql.com, mulailah dari sana. Cari saja di Google dengan kata kunci “planet <nama proyek>.”

3. **Bergabunglah dengan saluran IRC**: Banyak proyek open source memiliki saluran khusus Internet relay chat (IRC) di mana para pengembang dan pengguna berkumpul untuk mendiskusikan 

**Bekerja dengan Tiket**  
Kode adalah jantung dari setiap proyek open source, tetapi jangan berpikir bahwa menulis kode adalah satu-satunya cara untuk berkontribusi.
Pemeliharaan kode dan sistem yang mengelilingi kode sering kali terabaikan karena terburu-buru untuk membuat fitur baru dan memperbaiki bug.
Lihatlah area-area ini sebagai cara mudah untuk masuk ke dalam sebuah proyek.
Sebagian besar proyek memiliki sistem tiket masalah yang dapat dilihat oleh publik, ditautkan dari halaman depan situs web proyek dan disertakan dalam dokumentasi.
Ini adalah saluran utama komunikasi antara pengguna dan pengembang. Menjaga agar tetap mutakhir adalah cara yang bagus untuk membantu proyek.
Anda mungkin perlu mendapatkan izin khusus dalam sistem tiket, yang sebagian besar pemimpin proyek akan dengan senang hati memberikannya kepada Anda ketika Anda mengatakan ingin membantu membersihkan tiket.

4. **Mendiagnosis bug**: Bug sering kali tidak dilaporkan dengan baik.
Mendiagnosis dan melakukan triase terhadap bug dapat membantu menghemat waktu pengembang untuk mencari tahu secara spesifik masalahnya.
Jika pengguna melaporkan, “Perangkat lunak tidak berfungsi ketika saya melakukan X,” luangkan waktu untuk mencari tahu secara spesifik apa yang menyebabkan masalah tersebut.
Apakah masalah tersebut dapat diulang? Dapatkah Anda membuat serangkaian langkah yang menyebabkan masalah berulang kali? Dapatkah Anda mempersempit masalahnya, misalnya hanya terjadi pada satu browser tetapi tidak pada browser lainnya, atau satu distro tetapi tidak pada distro lainnya?

Meskipun Anda tidak tahu apa yang menyebabkan masalah, upaya yang Anda lakukan untuk mempersempit masalah akan memudahkan orang lain untuk memperbaikinya.
Apa pun yang Anda temukan, tambahkan ke tiket di sistem bug agar semua orang dapat melihatnya.

5. **Tutup bug yang sudah diperbaiki**: Sering kali bug diperbaiki di basis kode tetapi tiket yang dilaporkan tidak diperbarui di sistem tiket.
Membersihkan kesalahan ini dapat memakan waktu, tetapi sangat berharga bagi keseluruhan proyek.

Mulailah dengan menanyakan sistem tiket untuk tiket yang lebih tua dari satu tahun dan lihat apakah bug masih ada.
Periksa log perubahan rilis proyek untuk melihat apakah bug telah diperbaiki dan dapat ditutup.
Jika diketahui sudah diperbaiki, catat nomor versi di tiket dan tutup.

Coba buat ulang bug dengan versi terbaru perangkat lunak.
Jika tidak dapat dibuat ulang dengan versi terbaru, catat dalam tiket dan tutup.
Jika masih ada, catat juga di tiket dan biarkan terbuka.

Bekerja dengan Kode
Programmer dari semua tingkat pengalaman dapat membantu dengan kode dalam proyek.
Jangan berpikir bahwa Anda harus menjadi seorang jenius pengkodean untuk memberikan kontribusi nyata pada proyek favorit Anda.

Jika pekerjaan Anda melibatkan modifikasi kode, selidiki metode yang digunakan proyek untuk mendapatkan kode dari kontributor.
Setiap proyek memiliki alur kerjanya sendiri, jadi tanyakan tentang cara melakukannya sebelum Anda mulai mengirimkan kode.

Sebagai contoh, proyek PostgreSQL sangat ketat dalam prosesnya: Modifikasi kode dikirim dalam bentuk tambalan ke milis di mana para pengembang inti meneliti setiap aspek perubahan. Di sisi lain adalah proyek seperti Parrot di mana mudah untuk mendapatkan hak komit ke basis kode. Jika proyek menggunakan GitHub, mungkin ada alur kerja yang menggunakan fitur pull request dari GitHub. Tidak ada dua proyek yang sama.

Setiap kali Anda memodifikasi kode, pastikan Anda bertindak sebagai anggota komunitas yang bertanggung jawab dan menjaga gaya kode Anda agar sesuai dengan basis kode lainnya. Kode yang Anda tambahkan atau modifikasi harus terlihat seperti yang lainnya. Anda mungkin tidak menyukai gaya bracing atau penanganan spasi untuk lekukan, tetapi tidak sopan untuk mengirimkan perubahan kode yang tidak sesuai dengan standar yang ada. Ini sama saja dengan mengatakan “Saya tidak suka gaya Anda, dan menurut saya gaya saya lebih baik, jadi Anda harus melakukannya dengan cara saya.”

6. **Menguji versi beta atau kandidat rilis**: Setiap proyek yang dirancang untuk berjalan di berbagai platform dapat memiliki berbagai macam masalah portabilitas.
Ketika sebuah rilis mendekati dan sebuah beta atau kandidat rilis diterbitkan, pemimpin proyek berharap bahwa hal itu akan diuji oleh banyak orang yang berbeda di berbagai platform.
Anda dapat menjadi salah satu dari orang-orang tersebut dan membantu memastikan bahwa paket tersebut bekerja pada platform Anda.

Biasanya Anda hanya perlu mengunduh, membangun, dan menguji perangkat lunak, tetapi nilainya bagi proyek bisa sangat besar jika Anda menggunakan distribusi atau perangkat keras yang tidak umum.
Hanya dengan melaporkan kembali bahwa pembuatan dan pengujian telah berhasil, akan membantu para pemimpin proyek untuk mengetahui bahwa rilis yang akan datang sudah solid.

7. **Memperbaiki bug**: Ini biasanya merupakan tempat kontributor yang ingin mulai mengerjakan kode.
Sederhana saja: Temukan bug yang terdengar menarik dalam sistem tiket dan coba perbaiki dalam kode.
Dokumentasikan perbaikannya dalam kode jika sesuai.
Sebaiknya tambahkan tes ke dalam test suite untuk menguji bagian kode yang telah Anda perbaiki; beberapa proyek memerlukan perbaikan bug untuk menyertakan tes. Buatlah catatan saat Anda mengutak-atik basis kode yang tidak Anda kenal. Bahkan jika Anda tidak dapat memperbaiki bug, dokumentasikan dalam tiket apa yang Anda temukan sebagai bagian dari upaya perbaikan. Apa yang Anda temukan akan membantu mereka yang datang setelah Anda.

8. **Menulis tes**: Sebagian besar proyek memiliki test suite yang menguji kode, tetapi sulit untuk membayangkan sebuah test suite yang tidak dapat menambahkan lebih banyak tes ke dalamnya.
Gunakan alat bantu cakupan pengujian seperti gcov untuk C, atau Devel::Cover untuk Perl untuk mengidentifikasi area dalam kode sumber yang tidak diuji oleh rangkaian pengujian.
Kemudian, tambahkan sebuah tes ke dalam rangkaian tes untuk menutupinya.

9. **Diamkan peringatan kompiler**: Proses build untuk banyak proyek berbasis C sering memuntahkan bendera peringatan kompiler yang aneh ke layar.
Peringatan ini biasanya bukan merupakan indikator dari sebuah masalah, tetapi bisa terlihat seperti itu.
Terlalu banyak peringatan dapat membuat kompiler terdengar seperti serigala yang menangis.
Periksa untuk melihat apakah kode tersebut benar-benar menyembunyikan bug. Jika tidak, memodifikasi sumbernya untuk tidak bersuara akan membantu menyembunyikan kesalahan positif ini.

10. **Tambahkan komentar**:
Ketika Anda menggali kode, Anda mungkin menemukan beberapa bagian yang membingungkan.
Kemungkinan besar jika Anda bingung, orang lain juga akan bingung. Dokumentasikan dalam kode dan kirimkan patch.
Bekerja dengan Dokumentasi
Dokumentasi biasanya merupakan bagian dari sebuah proyek yang mendapat waktu singkat.
Dokumentasi juga dapat mengalami kesulitan karena ditulis dari sudut pandang mereka yang sudah terbiasa dengan proyek tersebut, bukan dari sudut pandang seseorang yang baru saja masuk ke dalamnya.
Jika Anda pernah membaca dokumen untuk sebuah proyek di mana Anda berpikir, “Sepertinya manual ini mengharapkan bahwa saya sudah tahu cara menggunakan paket ini,” Anda tahu apa yang saya bicarakan.
Seringkali, satu set mata yang segar dapat menunjukkan kekurangan dalam dokumentasi yang tidak disadari oleh mereka yang dekat dengan proyek.

11. **Buatlah sebuah contoh**: Tidak ada proyek yang memiliki terlalu banyak contoh cara.
Entah itu API web, pustaka rutinitas, aplikasi GUI seperti Gimp, atau alat baris perintah,
contoh penggunaan yang baik dapat menjelaskan penggunaan perangkat lunak dengan lebih jelas dan cepat daripada halaman-halaman dokumentasi.
Untuk API atau pustaka, buatlah contoh program yang menggunakan alat tersebut. Ini bahkan dapat diekstrak dari kode yang telah Anda tulis, dipangkas hingga ke hal-hal yang diperlukan.
Untuk sebuah alat, tunjukkan contoh dunia nyata tentang bagaimana Anda menggunakannya dalam kehidupan sehari-hari. Jika Anda berorientasi pada visual,
pertimbangkan untuk membuat tangkapan layar dari proses penting, seperti cara menginstal aplikasi.

Bekerja dengan Komunitas
Open source hanya sebagian dari kode. Komunitaslah yang membuat open source bekerja. Berikut adalah cara-cara yang dapat Anda lakukan untuk membantu membangunnya.

12. **Menjawab pertanyaan**: Cara terbaik untuk membantu membangun komunitas adalah dengan membantu orang lain.
Menjawab pertanyaan, terutama dari seseorang yang baru saja memulai, sangat penting untuk membantu proyek tumbuh dan berkembang.
Waktu yang Anda luangkan untuk membantu seorang pemula, bahkan jika mereka mengajukan pertanyaan di mana Anda dapat dengan mudah menjawab “RTFM” dengan cepat, akan terbayar di kemudian hari dengan mendapatkan anggota aktif lainnya di dalam komunitas.
Semua orang memulai dari suatu tempat, dan proyek membutuhkan arus masuk orang yang konstan jika ingin tetap hidup.

13. **Tulislah sebuah postingan blog:
Jika Anda memiliki sebuah blog, tulislah tentang pengalaman Anda dengan proyek yang Anda gunakan.
Ceritakan tentang masalah yang Anda hadapi dengan menggunakan perangkat lunak dan apa yang Anda lakukan untuk menyelesaikannya.
Anda akan membantu dengan dua cara, yaitu dengan membantu menjaga proyek tetap berada di benak orang lain di sekitar Anda,
dan dengan membuat catatan untuk orang lain yang memiliki masalah yang sama dengan Anda di masa depan dan mencari jawabannya di web.
(Sebuah blog tentang petualangan teknis Anda juga merupakan cara yang sangat baik untuk menunjukkan pengalaman dunia nyata dengan perangkat lunak yang bersangkutan saat Anda mencari pekerjaan dengan menggunakan perangkat lunak tersebut).

14. **Memperbaiki situs web**:
Jika Anda memiliki keahlian dalam desain web dan dapat membantu meningkatkan situs web, dan dengan demikian citra proyek yang dihadapi publik, itu adalah waktu yang dihabiskan dengan baik.
Mungkin proyek tersebut dapat menggunakan perbaikan grafis, atau logo untuk mengidentifikasi proyek.
Hal ini mungkin merupakan keterampilan yang kurang dimiliki oleh komunitas. Saya tahu saya akan sangat senang jika saya bisa mendapatkan bantuan desain grafis di situs web proyek saya.
  
15. **Menulis dokumentasi teknis**
Jika Anda dapat menulis tentang bagaimana sebuah aplikasi atau perangkat lunak bekerja, Anda dapat menulis dokumentasi teknis tentangnya. Terutama proyek-proyek open source yang ingin memperbarui, mengubah, memperluas, atau membuat dokumen teknis untuk dibaca oleh masyarakat umum. Semakin banyak Anda menulis dalam bahasa Inggris, semakin baik. Bagian terbaiknya, Anda tidak harus menjadi seorang programmer untuk menulis dokumen teknis.

Yang terpenting, dengarkan apa yang orang-orang di sekitar Anda diskusikan. Lihat apakah Anda dapat mengenali kebutuhan yang mendesak. Sebagai contoh, baru-baru ini di milis pengembang Parrot, diputuskan untuk menggunakan GitHub sebagai sistem tiket masalah, meninggalkan instalasi Trac lama yang mereka miliki. Beberapa orang menentang langkah tersebut karena tidak ada cara untuk mengubah tiket ke sistem GitHub. Setelah seharian berdebat, saya akhirnya berkata, “Bagaimana jika saya menulis konverter?” Orang-orang sangat senang dengan ide tersebut. Saya menghabiskan waktu untuk menulis program konversi untuk 450+ tiket, jadi kami tidak kehilangan riwayat tiket kami. Itu adalah sebuah kesuksesan besar.  Saya bisa ikut serta, dan para pengembang inti tetap fokus pada bisnis pengerjaan Parrot.

16. **Mengajar dan Membantu orang lain**:
Cara terbaik untuk mempelajari lebih lanjut tentang suatu topik adalah dengan mencoba mengajarkannya.
Guru terbaik adalah guru yang dapat menjelaskan hal-hal yang rumit dengan contoh-contoh sederhana. Jadi, Anda perlu mencoba menjadi guru terbaik untuk menjadi pelajar terbaik dan yang terbaik di dunia pemrograman Anda. Mengajar orang lain akan membuat Anda merasa lebih baik tentang diri Anda sendiri dan akan membantu Anda mendapatkan keterampilan dan pengetahuan yang lebih baik dalam profesi Anda. Ketika Anda mendapatkan bantuan dari seseorang, jangan menyimpannya sendiri, tetapi bagikanlah dengan orang lain. Jadikan dunia tempat yang lebih baik untuk ditinggali.