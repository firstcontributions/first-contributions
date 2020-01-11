[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="../assets/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

*Người dịch: [Tran Ly Vu](https://github.com/tranlyvu) và [Nguyễn Huỳnh Lợi](https://github.com/loia5tqd001)*

# Tạo những đóng góp đầu tiên trên github

Cái gì cũng khó lần đầu tiên bạn làm nó cả! đặc biệt là làm chung với người khác, làm chung với người khác và để mắc sai lầm thì chả dễ chịu tí nào. Đó là lý do repository này được nào ra. Chúng tôi muốn giúp bạn học cách đóng góp vào mã nguồn mở, một cách đơn giản nhất, bằng cách thực hành tạo những đóng góp đầu tiên. 

Việc đọc các bài viết, xem những video hướng dẫn cũng có tác dụng, nhưng có gì tốt hơn là thực sự thực hành nó, đóng góp vào một môi trường luyện tập? Project này cung cấp các hướng dẫn và đơn giản hóa cách thức những người mới tham gia đóng góp. Nếu bạn mong muốn thực hiện việc đóng góp đầu tiên của mình, chỉ cần làm theo các bước đơn giản bên dưới.

#### *Nếu bạn không thích làm việc với dòng lệnh, [đây là những hướng dẫn sử dụng bằng giao diện (GUI).]( #Hướng-dẫn-sử-dụng-cho-các-công-cụ-khác )*

<img align="right" width="300" src="../assets/fork.png" alt="fork this repository" />

Nếu bạn chưa có git trên máy tính của bạn, [cài đặt ở đây](https://help.github.com/articles/set-up-git/)

## Bước đầu tiên: Fork

Copy kho mã nguồn này bằng cách nhấn vào nút `Fork` đầu trang này. Bản sao kho mã nguồn sẽ được tạo ra trong tài khoản github của bạn.

## Bước thứ hai: Clone

<img align="right" width="300" src="../assets/clone.png" alt="clone this repository" />

Bây giờ clone kho mã nguồn này về máy của bạn. Nhấn vào nút `clone` và sau đó nhấn vào biểu tượng *copy to clipboard* để sao chép url

Mở terminal và chạy lệnh git sau đây:

```
git clone "url bạn vừa sao chép" 
# Lưu ý dán url vừa sao chép bằng Shift+Insert hoặc Ctrl+Shift+V thay vì Ctrl+V như thường
```
Trong đó "url bạn vừa sao chép" (không có dấu ngoặc kép) là url dẫn vào kho mã nguồn này. Xem bước trước đó để có được url.

<img align="right" width="300" src="../assets/copy-to-clipboard.png" alt="copy URL to clipboard" />

Ví dụ:
```
git clone https://github.com/tên-bạn/first-contributions.git
```
Trong đó `tên-bạn` là tên người dùng github của bạn. Ở đây bạn đang sao chép nội dung của kho mã nguồn "first-contributions" trong github vào máy tính của bạn

## Bước thứ ba: Tạo nhánh (branch)

Di chuyển môi trường trên terminal tới repository của bạn trên máy tính.

```
cd first-contributions
```
Bây giờ tạo ra một nhánh sử dụng lệnh `git checkout`
```
git checkout -b <tên-chi-nhánh>
```
Ví dụ:
```
git checkout -b add-son-tung-mtp 
# add-son-tung-mtp là tên nhánh
```
(Trong trường hợp này, nhánh này được tạo ra sẽ được dùng để  thêm tên của bạn vào danh sách đóng góp, nên bạn sẽ đặt tên `add-tên-bạn` để thể hiện tính năng của nhánh.)

## Bước thứ tư: Thực hiện những thay đổi và commit những thay đổi đó

Bây giờ mở file `Contributors.md` lên và thêm tên của bạn vào đó. 
Đừng thêm vào đầu hoặc cuối tập tin. Thêm vào bất cứ nơi nào ở giữa. Thêm xong rồi thì lưu lại.

<img align="right" width="450" src="../assets/git-status.png" alt="git status" />

Nếu bạn vào thư mục hiện tại của project và thực hiện lệnh `git status`, bạn sẽ thấy những thay đổi đã thực hiện.

Thêm những thay đổi này vào nhánh bạn vừa tạo bằng lệnh `git add`:

```
git add Contributors.md
```

Giờ commit những thay đổi bằng cách sử dụng dòng lệnh `git commit` như dưới đây.
```
git commit -m "Add <ten-ban> to Contributors list"
              #Thêm tên bạn vào danh sách người đóng góp
```

Thay thế `<ten-ban>` với tên của bạn

## Bước thứ năm: Push thay đổi lên github

Push những thay đổi của bạn, những đóng góp mà bạn đã tạo ra bằng lệnh `git push`
```
git push origin <tên-chi-nhánh>
```
Thay thế `<tên-chi-nhánh>` với tên của chi nhánh bạn tạo ra trước đó *(`add-son-tung-mtp` trong ví dụ này)*

## Bước thứ sáu: Gửi những thay đổi của bạn để xem xét

Nếu bạn mở kho mã nguồn (repository) của bạn trên github, bạn sẽ thấy nút `Compare & pull request`. Nhấp vào nút đó.

<img style="float: right;" src="../assets/compare-and-pull.png" alt="create a pull request" />

Bây giờ gửi yêu cầu pull request.

<img style="float: right;" src="../assets/submit-pull-request.png" alt="submit pull request" />

Chúng tôi sẽ sớm hợp nhất các thay đổi của bạn vào nhánh chủ (master branch) của project này. Bạn sẽ nhận được email thông báo sau khi các thay đổi được hợp nhất.

## Tiếp theo

Chúc mừng! Bạn vừa hoàn thành quy trình tiêu chuẩn *fork -> clone -> chỉnh sửa -> pull request* mà bạn sẽ gặp thường xuyên khi đóng góp!

Hãy ăn mừng đóng góp của bạn và chia sẻ nó với bạn bè và những người theo dõi của bạn bằng cách truy cập [ứng dụng web này](https://firstcontributions.github.io/#social-share).

Bạn có thể tham gia slack của chúng tôi trong trường hợp bạn cần trợ giúp đỡ hoặc có câu hỏi nào. [Tham gia slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Để hỗ trợ bạn với việc đóng góp cho các project khác. Chúng tôi đã chuẩn bị danh sách các project đơn giản mà bạn có thể bắt đầu. Hãy kiểm tra [danh sách các project](https://roshanjossey.github.io/first-contributions/#project-list).

### [Tài liệu bổ sung](additional-material/git_workflow_scenarios/additional-material.md)

## Hướng dẫn sử dụng cho các công cụ khác

|<a href="github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a>|<a href="github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a>|<a href="gitkraken-tutorial.md"><img alt="GitKraken" src="../assets/gk-icon.png" width="100"></a>|<a href="github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a>|<a href="sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a>|
|---|---|---|---|---|
|[GitHub Desktop](../github-desktop-tutorial.md)|[Visual Studio 2017](../github-windows-vs2017-tutorial.md)|[GitKraken](../gitkraken-tutorial.md)|[Visual Studio Code](../github-windows-vs-code-tutorial.md)|[Atlassian Sourcetree](../sourcetree-macos-tutorial.md)|

