[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

*Người dịch: [Tran Ly Vu](https://github.com/tranlyvu)*
*Người chỉnh sửa: [Tran Nguyen Thuong Truong](https://github.com/thuongtruong1009)* 

# Đóng góp đầu tiên

Lần đầu tiên bạn làm điều gì đó thật khó khăn. Đặc biệt khi bạn đang cộng tác với ai đó, thì sai lầm là điều rất khó chịu. Vì thế, chúng tôi muốn đơn giản hóa quy trình học và đóng góp vào những dự án mã nguồn mở. 

Việc đọc hướng dẫn có tác động rất tốt để tiếp thu kiến thức, nhưng chúng còn tốt hơn là khi bạn thực sự đóng góp trong môi trường thực tiễn? project này nhằm mục đích cung cấp hướng dẫn và đơn giản hóa cách thức những người mới tham gia đóng góp. Nếu bạn mong muốn thực hiện việc đóng góp đầu tiên của mình vào dự án mã nguồn mở, chỉ cần làm theo các bước đơn giản bên dưới.

#### *Nếu bạn không quen làm việc với dòng lệnh, [đây là hướng dẫn sử dụng GUI.]( #Hướng-dẫn-sử-dụng-các-công-cụ-khác )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Nếu bạn không có git trên máy tính của bạn, tham khảo tại [cài đặt](https://help.github.com/articles/set-up-git/)

## Cộng tác kho mã nguồn (Fork)

Cộng tác kho mã nguồn này bằng cách nhấn vào nút `Fork` ở đầu phía trên bên phải trang này. Sau đó bản sao kho mã nguồn này sẽ được tạo ra trong tài khoản của bạn.

## Sao lưu kho mã nguồn (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Bây giờ để sao lưu kho mã nguồn này vào máy của bạn. Hãy nhấn vào nút `clone` và sau đó nhấn vào biểu tượng *copy to clipboard* để lưu vào bộ nhớ đệm.

Mở một bộ xử lý dòng lệnh và chạy lệnh git sau đây:

```
git clone "đường dẫn mà bạn vừa sao chép"
```
Trong đó "đường dẫn mà bạn vừa sao chép" (không có dấu ngoặc kép) là đường dẫn vào kho mã nguồn này. Xem các bước trước đó để có được đường dẫn.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

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
(Tên của chi nhánh không cần phải có từ *add* trong đó, nhưng nó được dùng vì mục đích của chi nhánh này là thêm tên của bạn vào danh sách.)

## Thực hiện những thay đổi cần thiết và chấp thuận những thay đổi này

Bây giờ hãy mở tập tin `Contributors.md` trong một trình soạn thảo mã lệnh và thêm tên của bạn vào nó. 
Đừng thêm vào đầu hoặc cuối tập tin, mà hãy thêm chúng vào bất cứ nơi nào ở giữa. Sau đó, lưu tập tin.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Nếu bạn vào thư mục hiện tại của dự án và thực hiện lệnh `git status`, bạn sẽ thấy một cách chi tiết tình trạng kho mã nguồn.

Thêm những thay đổi vào chi nhánh bạn vừa tạo bằng lệnh `git add`:

```
git add Contributors.md
```

Bây giờ, để cam kết tất cả những thay đổi trên bằng cách sử dụng dòng lệnh `git commit` dưới đây.
```
git commit -m "Them <ten-ban> vào danh sách Cộng tác viên"
```

Thay thế `<ten-ban>` với tên của bạn

## Đẩy thay đổi lên github

Đẩy lên những thay đổi của bạn bằng cách gõ lệnh `git push`
```
git push origin <tên-chi-nhánh>
```
Thay thế `<tên-chi-nhánh>` với tên của chi nhánh bạn tạo ra trước đó

## Gửi những thay đổi của bạn để được xem xét

Nếu bạn mở kho mã nguồn của bạn trên github, bạn sẽ thấy nút `Compare & pull request`. Nhấp vào nút đó.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Bây giờ gửi yêu cầu kéo.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tôi sẽ sớm hợp nhất tất cả các thay đổi của bạn vào nhánh chủ (master branch) của dự án này. Bạn sẽ nhận được thư thông báo sau khi các thay đổi đã được hợp nhất.

## Cuối cùng

Xin chúc mừng! Bạn vừa hoàn thành quy trình tiêu chuẩn cộng tác (fork) -> sao lưu (clone) -> chỉnh sửa (edit) -> yêu cầu kéo (pull request) mà bạn sẽ gặp thường xuyên khi đóng góp vào những dự án mã nguồn mở tiếp theo!

Chúc mừng những đóng góp của bạn và chia sẻ chúng với bạn bè và những người theo dõi của bạn bằng cách truy cập tại [ứng dụng web](https://roshanjossey.github.io/first-contribution/#social-share).

Bạn có thể tham gia cộng đồng Slack của chúng tôi trong trường hợp bạn cần trợ giúp hoặc có bất kì câu hỏi nào. [Tham gia slack](https://join.slack.com/t/firstcontributors/shared_invite/enQtMzE1MTYwNzI3ODQ0LTZiMDA2OGI2NTYyNjM1MTFiNTc4YTRhZTg4OWZjMzA0ZWZmY2UxYzVkMzI1ZmVmOWI4ODdkZWQwNTM2NDVmNjY).

Để hỗ trợ bạn với việc đóng góp cho các dự án khác. Chúng tôi đã chuẩn bị danh sách các dự án đơn giản mà bạn có thể bắt đầu. Hãy kiểm tra tại đây[danh sách các project](https://roshanjossey.github.io/first-contributions/#project-list).

### [Tài liệu bổ sung](../additional-material/git_workflow_scenarios/additional-material.md)

## Hướng dẫn sử dụng các công cụ khác

| <a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="./assets/gk-icon.png" width="100"></a> | <a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> | <a href="gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/IntelliJ_IDEA_Logo.svg" width=100></a> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Desktop](gui-tool-tutorials/github-desktop-tutorial.md)                                                                                             | [Visual Studio 2017](gui-tool-tutorials/github-windows-vs2017-tutorial.md)                                                                                                                          | [GitKraken](gui-tool-tutorials/gitkraken-tutorial.md)                                                               | [Visual Studio Code](gui-tool-tutorials/github-windows-vs-code-tutorial.md)                                                                                                                  | [Atlassian Sourcetree](gui-tool-tutorials/sourcetree-macos-tutorial.md)                                                                                                                                      | [IntelliJ IDEA](gui-tool-tutorials/github-windows-intellij-tutorial.md)                                                                                                                   |

