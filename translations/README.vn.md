[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

*Người dịch: [Tran Ly Vu](https://github.com/tranlyvu)*

# Đóng góp đầu tiên

Lần đầu tiên bạn làm điều gì đó thật khó khăn. Đặc biệt khi bạn đang cộng tác, sai lầm là điều rất khó chịu. Chúng tôi muốn đơn giản hóa quy trình học và đóng góp vào những dự án (project) mã nguồn mở. 

Việc đọc hướng dẫn có tác dụng, nhưng có gì tốt hơn là thực sự đóng góp trong môi trường thực tiễn? project này nhằm mục đích cung cấp hướng dẫn và đơn giản hóa cách thức những người mới tham gia đóng góp. Nếu bạn mong muốn thực hiện việc đóng góp đầu tiên của mình, chỉ cần làm theo các bước đơn giản bên dưới.

#### *Nếu bạn không thích làm việc với dòng lệnh, [đây là hướng dẫn sử dụng GUI.]( #tutorials-using-other-tools )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Nếu bạn không có git trên máy tính của bạn, [cài đặt](https://help.github.com/articles/set-up-git/)

## Copy kho mã nguồn (Fork)

Copy kho mã nguồn này bằng cách nhấn vào nút `Fork` đầu trang này. Bản sao kho mã nguồn mày sẽ được tạo ra trong tài khoản của bạn.

## Sao chép kho mã nguồn (clone)

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Bây giờ sao chép kho mã nguồn này vào máy của bạn. Nhấn vào nút `clone` và sau đó nhấn vào biểu tượng *copy to clipboard*

Mở một bộ xử lý terminal và chạy lệnh git sau đây:

```
git clone "url bạn vừa sao chép"
```
Trong đó "url bạn vừa sao chép" (không có dấu ngoặc kép) là url dẫn vào kho mã nguồn này. Xem các bước trước đó để có được url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Ví dụ:
```
git clone https://github.com/tên-bạn/first-contributions.git
```
Trong đó `tên-bạn` là tên người dùng github của bạn. Ở đây bạn đang sao chép nội dung của kho mã nguồn "first-contributions" trong github vào máy tính của bạn

## Tạo chi nhánh (branch)

Thay đổi môi trường làm việc bằng thư mục của kho mã nguồn trên máy tính của bạn.

```
cd first-contributions
```
Bây giờ tạo ra một chi nhánh sử dụng lệnh `git checkout`
```
git checkout -b <tên-chi-nhánh>
```

Ví dụ:
```
git checkout -b thêm-Tran-Ly-Vu
```
(Tên của chi nhánh không cần phải có từ *thêm* trong đó, nhưng nó được dùng vì mục đích của chi nhánh này là thêm tên của bạn vào danh sách.)

## Thực hiện những thay đổi cần thiết và chấp nhận những thay đổi này

Bây giờ mở tập tin `Contributors.md` trong một trình soạn thảo văn bản và thêm tên của mình vào nó. 
Đừng thêm vào đầu hoặc cuối tập tin. Thêm vào bất cứ nơi nào ở giữa. Bây giờ, lưu tập tin.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Nếu bạn vào thư mục hiện tại của project và thực hiện lệnh `git status`, bạn sẽ thấy những thay đổi.

Thêm những thay đổi vào chi nhánh bạn vừa tạo bằng lệnh `git add`:

```
git add Contributors.md
```

Bây giờ chấp nhận những thay đổi bằng cách sử dụng dòng lệnh `git commit` dưới đây.
```
git commit -m "Them <ten-ban> vào danh sách Cộng tác viên"
```

Thay thế `<ten-ban>` với tên của bạn

## Đẩy thay đổi lên github

Đẩy những thay đổi của bạn sử dụng `git push`
```
git push origin <tên-chi-nhánh>
```
Thay thế `<tên-chi-nhánh>` với tên của chi nhánh bạn tạo ra trước đó

## Gửi những thay đổi của bạn để xem xét

Nếu bạn mở kho mã nguồn của bạn trên github, bạn sẽ thấy nút `Compare & pull request`. Nhấp vào nút đó.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Bây giờ gửi yêu cầu kéo.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Tôi sẽ sớm hợp nhất tất cả các thay đổi của bạn vào nhánh chủ (master branch) của project này. Bạn sẽ nhận được email thông báo sau khi các thay đổi đã được hợp nhất.

## Tiếp theo

Chúc mừng! Bạn vừa hoàn thành quy trình tiêu chuẩn copy (fork) -> Sao chép (clone) -> chỉnh sửa (edit) -> yêu cầu kéo (pull request) mà bạn sẽ gặp thường xuyên khi đóng góp!

Hãy ăn mừng đóng góp của bạn và chia sẻ nó với bạn bè và những người theo dõi của bạn bằng cách truy cập [ứng dụng web](https://roshanjossey.github.io/first-contribution/#social-share).

Bạn có thể tham gia slack của chúng tôi trong trường hợp bạn cần trợ giúp hoặc có câu hỏi nào. [Tham gia slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Để hỗ trợ bạn với việc đóng góp cho các project khác. Chúng tôi đã chuẩn bị danh sách các project đơn giản mà bạn có thể bắt đầu. Hãy kiểm tra [danh sách các project](https://roshanjossey.github.io/first-contributions/#project-list).

### [Tài liệu bổ sung](additional-material/git_workflow_scenarios/additional-material.md)

## Hướng dẫn sử dụng các công cụ khác

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://www.visualstudio.com/wp-content/uploads/2017/11/microsoft-visual-studio.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="/assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|
|---|---|---|---|
|[GitHub Desktop](github-desktop-tutorial.md)|[Visual Studio 2017](github-windows-vs2017-tutorial.md)|[GitKraken](gitkraken-tutorial.md)|[Visual Studio Code](github-windows-vs-code-tutorial.md)|

