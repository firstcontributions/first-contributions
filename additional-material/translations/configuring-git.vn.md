# Cấu hình cho git

Nếu bạn đang chuẩn bị commit lần đầu tiên bằng git, bạn có thể nhìn thấy một dòng như thế này: 

```bash
$ git commit
*** Please tell me who you are.

Run

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```

Git cần biết được bạn là ai khi bạn tạo một commit. Khi làm việc tập thể, bạn cần phải có khả năng kiểm tra xem ai đã sửa đổi một phần nào đó của dự án, và vì thế, git đã được thiết kế để gắn các commit với một cái tên và một email.

Có nhiều cách để cung cấp cho lệnh `git commit` email và tên của bạn, và chúng tôi sẽ trình bày một số chúng dưới đây.

### Cấu hình hệ thống.

Khi bạn lưu một thông tin bất kỳ trong cấu hình của hệ thống, tất cả các repository của bạn đều có thể truy cập được nó. Đây là cách được ưa chuộng và hoạt động trong hầu hết trường hợp.

Để lưu một thông tin trong cấu hình hệ thống, chạy câu lệnh `config` như sau đây:

`$ git config --global <tên thông tin> <giá trị>`

Ví dụ, với thông tin người dùng, ta chạy:

```
$ git config --global user.email "Email của bạn"
$ git config --global user.name "Tên của bạn"
```

### Cấu hình cho repository

Giống như cái tên, cách cấu hình này chỉ có tác dụng trong repository hiện tại của bạn. Nếu bạn muốn commit trong một repository nào đó - ví dụ: một dự án liên quan đến công việc - bằng email của công ty bạn, thì bạn có thể sử dụng phương pháp này.

Để lưu một thông tin trong cấu hình repository, sử dụng dụng câu lệnh `config` và bỏ đi flag `--global` như sau:

`$ git config <tên thông tin> <giá trị>`

Ví dụ, với thông tin người dùng, ta chạy:

```
$ git config user.email "Email công ty của bạn"
$ git config user.name "Tên của bạn"
```

### Cấu hình riêng cho dòng lệnh 

Cách cấu hình này chỉ có hiệu lực đối với câu lệnh hiện tại. Tất cả các câu lệnh git sử dụng flag `-c` đặt trước hành động sẽ đặt các cấu hình được ghi kèm một cách tạm thời.

Để lưu thông tin trong cấu hình dòng lệnh, chạy câu lệnh sau đây:

`$ git -c <thông tin 1>=<giá trị> -c <thông tin 2>=<giá trị> <câu lệnh>` 

Trong ví dụ của chúng ta, ta sẽ chạy lệnh commit như sau

`git -c user.name='Tên của bạn' -c user.email='Email của bạn' commit -m "Nội dung commit"`

### Ghi chú về sự ưu tiên

Trong ba phương pháp kể trên, thứ tự ưu tiên là `dòng lệnh > repository > hệ thống`. Điều này nghĩa là, nếu một thông tin được cấu hình ở cả trong câu lệnh lẫn ở hệ thống, thì giá trị được đặt ở câu lệnh sẽ được sử dụng.

## Những thông tin khác có ích

Hiện giờ chúng ta chỉ đang quan tâm đến thông tin người dùng khi cấu hình git. Tuy nhiên còn một số loại thông tin khác cũng có thể điều chỉnh được, ví dụ như:

1.  `core.editor` - để đặt phần mềm chỉnh sửa văn bản mong muốn cho những tác vụ như viết nội dung commit, ...
2   `commit.template` - đặt một file làm mẫu cho commit đầu tiên
3.  `color.ui` - một giá trị kiểu boolean (true-false) để xác định xem có sử dụng màu trong output của git không.

Chúng tôi đã cắt bớt một số chi tiết để bài viết được dễ hiểu. Để tìm hiểu kỹ hơn, truy cập trang [git-scm.com](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).