
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)


# Đóng góp đầu tiên

Nó khó. Lần đầu tiên bạn làm điều gì đó thật khó khăn. Đặc biệt khi bạn đang cộng tác, những sai lầm không phải là điều thoải mái. Nhưng mã nguồn mở là tất cả về sự hợp tác và làm việc cùng nhau. Chúng tôi muốn đơn giản hóa cách những người đóng góp lần đầu tiên mới học và đóng góp.

Đọc hướng dẫn có thể giúp, nhưng tốt nhất là thực sự đóng góp mà không làm rối tung bất cứ điều gì. Dự án này nhằm mục đích cung cấp hướng dẫn và đơn giản hóa cách thức những người tân binh tham gia đóng góp lần đầu tiên. Hãy nhớ rằng khi bạn cảm thấy thoải mái thì việc học sẽ trở nên dễ dàng hơn. Nếu bạn mong muốn thực hiện việc đóng góp đầu tiên của mình, bạn chỉ cần làm theo các bước đơn giản bên dưới. Chúng tôi hứa bạn sẽ có nhiều niềm vui.  

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Nếu bạn không thích làm việc với dòng lệnh, hãy thử hướng dẫn của chúng tôi dựa trên [GitKraken](../gitkraken-tutorial.md).

Nếu bạn không có git trên máy tính của bạn, [ cài đặt nó ]( https://help.github.com/articles/set-up-git/ )

## Fork kho mã nguồn này

Fork kho mã nguồn này bằng cách nhấn vào nút Fork đầu trang này. Bản sao kho mã nguồn mày sẽ được tạo ra trong tài khoản của bạn.

## Sao chép (clone) kho mã nguồn

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Bây giờ sao chép kho mã nguồn này vào máy của bạn. Nhấn vào nút clone và sau đó nhấn vào biểu tượng "copy to clipboard"

Mở một bộ xử lý terminal và chạy lệnh git sau đây:

```
git clone "url bạn vừa sao chép"
```
Trong đó "url bạn vừa sao chép" (không có dấu ngoặc kép) là url dẫn vào kho mã nguồn này. Xem các bước trước đó để có được url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Ví dụ:
```
git clone https://github.com/this-is-you/first-contributions.git
```
Trong đó 'this-is-you' là tên người dùng github của bạn. Ở đây bạn đang sao chép nội dung của kho mã nguồn "first-contributions" trong github vào máy tính của bạn

## Tạo một chi nhánh (branch)

Thay đổi môi trường làm việc bằng thư mục của kho mã nguồn trên máy tính của bạn.

```
cd first-contributions
```
Bây giờ tạo ra một chi nhánh sử dụng lệnh `git checkout`
```
git checkout -b <them-ten-ban>
```

Ví dụ:
```
git checkout -b them-Tran-Ly-Vu
```

## Thực hiện những thay đổi cần thiết và chấp nhận những thay đổi này

Bây giờ mở tập tin `Contributors.md` trong một trình soạn thảo văn bản và thêm tên của mình vào nó, sau đó lưu tập tin. Nếu bạn đi đến thư mục dự án và nhập lệnh `git status`, bạn sẽ thấy có những thay đổi. Thêm những thay đổi bằng cách nhập dòng lệnh dưới đây 'git add`.
```
git add Contributors.md
```

Bây giờ chấp nhận những thay đổi bằng cách sử dụng dòng lệnh 'git commit` dưới đây.
```
git commit -m "Them <ten-ban> vào danh sách Cộng tác viên"
```
thay thế `<ten-ban>` với tên của bạn

## Đẩy thay đổi lên github

Đẩy những thay đổi của bạn sử dụng `git push`
```
git push origin <them-ten-ban>
```
Thay thế `<them-ten-ban>` với tên của chi nhánh bạn tạo ra trước đó

## Gửi những thay đổi của bạn để được xem xét

Nếu bạn mở kho mã nguồn của bạn trên github, bạn sẽ thấy nút `Compare & pull request`.Nhấp vào nút đó.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Bây giờ gửi yêu cầu kéo.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Bây giờ tôi sẽ kết hợp tất cả các thay đổi của bạn vào chi nhánh chủ (master branch) của dự án này. Bạn sẽ nhận được một email thông báo khi những thay đổi đã được sáp nhập.

Chi nhánh chủ của fork của bạn sẽ không có những thay đổi. Để giữ cho khớp của bạn được đồng bộ với chi nhánh chủ của tôi, hãy làm theo các bước dưới đây.

## Giữ fork của bạn đồng bộ hóa với kho mã nguồn chủ

Đầu tiên, chuyển sang chi nhánh chủ.
 ```
 git checkout master
 ```

Sau đó, thêm url repo của tôi như sau `upstream remote url`.
```
 git remote add upstream https://github.com/multunus/first-contributions
```
Đây là một cách để nói với git rằng một phiên bản khác của dự án này đang tồn tại trong một url khác và chúng ta gọi đó là phiên bản chủ. Một khi các thay đổi được sáp nhập, kéo phiên bản mới này đang nằm trong kho mã nguồn của tôi.
```
git fetch upstream
```

Ở đây chúng ta lấy tất cả những thay đổi trong fork của tôi (upstream remote). Bây giờ, bạn cần phải hợp nhất các phiên bản mới của kho mã nguồn của tôi vào chi nhánh chủ (master) của bạn.
```
git rebase upstream/master
```
Ở đây bạn đang áp dụng tất cả những thay đổi bạn lấy để đưa vào chi nhánh chủ (master). Nếu bạn đẩy chi nhánh chủ bây giờ, bản sao của bạn cũng sẽ có những thay đổi
```
git push origin master
```
Chú ý ở đây bạn đang đẩy lên trên github với chi nhánh tên là origin.

## Hướng dẫn sử dụng các công cụ khác


|<a href="../github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="../github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="../gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|
|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|
