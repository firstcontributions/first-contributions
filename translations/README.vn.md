[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/Readme/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open Source Helpers](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# Những đóng góp đầu tiên

Lần đầu tiên bạn làm điều gì đó có thể gặp nhiều trở ngại. Đặc biệt khi bạn đang cộng tác, sai lầm là điều rất khó tránh khỏi. 

Việc đọc hướng dẫn có tác dụng, nhưng có gì tốt hơn là thực sự đóng góp trong môi trường thực tiễn? Dự án này là nhằm mục đích cung cấp sự hướng dẫn và đơn giản hóa cách thức những người mới tham gia đóng góp. Nếu bạn mong muốn thực hiện việc đóng góp đầu tiên của mình, chỉ cần làm theo các bước đơn giản bên dưới.

#### *Nếu bạn không thoải mái khi làm việc với dòng lệnh, [đây là các hướng dẫn sử dụng các công cụ có giao diện đồ họa (GUI).]( #Hướng-dẫn-sử-dụng-các-công-cụ-khác )*

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

Nếu bạn không có git trên máy tính của bạn, [cài đặt git](https://help.github.com/articles/set-up-git/).

## Sao chép kho lưu trữ (Fork)

Sao chép (copy) kho lưu trữ mã nguồn (repository) này bằng cách nhấn vào nút `Fork` (Tạo nhánh) đầu trang này. Một bản sao kho lưu trữ này sẽ được tạo ra trong tài khoản của bạn.

## Tạo bản lưu nội bộ của kho lưu trữ trên máy tính của bạn (clone)

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Bây giờ, hãy sao chép bản sao (clone) kho lưu trữ đã được sao chép (fork) này vào máy của bạn. Để thực hiện thao tác này, truy xuất vào tài khoản GitHub của bạn, mở kho lưu trữ đã tạo nhánh rồi nhấn vào nút `Code`, và sau đó nhấn vào biểu tượng *copy to clipboard*

Mở một cửa sổ terminal và chạy lệnh git sau đây:

```bash
git clone "url bạn vừa sao chép"
```
Trong đó `"url bạn vừa sao chép"` (không có dấu ngoặc kép) là url dẫn vào kho mã nguồn (mà bạn đã sao chép) này. Xem các bước trước đó để có được url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

Ví dụ:
```bash
git clone https://github.com/tên-bạn/first-contributions.git
```
Trong đó `tên-bạn` là tên người dùng (username) tài khoản GitHub của bạn. Ở đây bạn đang sao chép nội dung của kho mã nguồn "first-contributions" trên GitHub vào máy tính của bạn

## Tạo nhánh (branch)

Di chuyển đến thư mục chứa kho lưu trữ trên máy tính của bạn (nếu bạn chưa ở đó):

```bash
cd first-contributions
```
Bây giờ tạo ra một nhánh (branch) sử dụng lệnh `git switch`
```bash
git switch -c <tên-nhánh-mới-của-bạn>
```

Ví dụ:
```bash
git switch -c thêm-Tran-Ly-Vu
```
(Tên của nhánh mới không cần phải có từ *thêm* trong đó, nhưng nó được dùng vì mục đích của nhánh này là thêm tên của bạn vào danh sách.)

## Thực hiện những thay đổi cần thiết và chấp nhận (commit) những thay đổi này

Bây giờ mở tập tin `Contributors.md` trong một trình soạn thảo văn bản và thêm tên của bạn vào. Đừng thêm vào đầu hoặc cuối tập tin. Thêm vào bất cứ nơi nào ở giữa. Sau đó, lưu tập tin.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

Nếu bạn vào thư mục hiện tại của project và thực hiện lệnh `git status`, bạn sẽ thấy những thay đổi.

Thêm những thay đổi vào nhánh bạn vừa tạo bằng lệnh `git add`:

```bash
git add Contributors.md
```

Bây giờ chấp nhận những thay đổi bằng cách sử dụng dòng lệnh `git commit` dưới đây:
```bash
git commit -m "Them <ten-ban> vào danh sách Cộng tác viên"
```

thay thế `<ten-ban>` bằng tên của bạn.

## Đẩy (push) các thay đổi lên GitHub

Đẩy những thay đổi của bạn sử dụng `git push`:
```bash
git push origin <tên-nhánh-của-bạn>
```
thay thế `<tên-nhánh-của-bạn>` với tên của nhánh bạn tạo ra trước đó.

<details>
<summary> <strong>Nếu bạn gặp bất cứ lỗi gì trong lúc thực hiện thao tác push, nhấn vào đây:</strong> </summary>

- ### Lỗi xác thực (Authentication Error)
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Truy cập vào [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) về việc tạo cấu hình khóa SSH cho tài khoản của bạn.

</details>

## Gửi yêu cầu xem xét các thay đổi của bạn

Nếu bạn mở kho mã nguồn của bạn trên GitHub, bạn sẽ thấy nút `Compare & pull request`. Nhấn vào nút đó.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Bây giờ, hãy gửi yêu cầu xem xét thay đổi (pull request)

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Tôi sẽ sớm hợp nhất (merge) tất cả các thay đổi của bạn vào nhánh chính (master branch) của dự án này. Bạn sẽ nhận được email thông báo sau khi các thay đổi đã được gộp.

## Bước tiếp theo là gì?

Chúc mừng! Bạn vừa hoàn thành quy trình tiêu chuẩn copy (fork) -> Sao chép (clone) -> chỉnh sửa (edit) -> yêu cầu kéo (pull request) mà bạn sẽ thường gặp khi đóng góp vào những dự án!

Hãy ăn mừng đóng góp của bạn, và chia sẻ nó với bạn bè và những người theo dõi của bạn bằng cách truy cập [ứng dụng web](https://roshanjossey.github.io/first-contribution/#social-share).

Bạn có thể tham gia Slack của chúng tôi trong trường hợp bạn cần trợ giúp hoặc có câu hỏi nào. [Tham gia Slack](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA).

Để hỗ trợ bạn với việc đóng góp cho các dự án (project) khác, chúng tôi đã tổng hợp một danh sách các dự án có các vấn đề đơn giản mà bạn có thể bắt đầu. Hãy kiểm tra [danh sách dự án trong ứng dụng web](https://firstcontributions.github.io/#project-list).

### [Tài liệu bổ sung](../additional-material/git_workflow_scenarios/additional-material.md)

## Hướng dẫn sử dụng  các công cụ khác

| <a href="../gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs2017-tutorial.md"><img alt="Visual Studio 2017" src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Visual_Studio_2017_Logo.svg" width="100"></a> | <a href="../gui-tool-tutorials/gitkraken-tutorial.md"><img alt="GitKraken" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/gitkraken-tutorial/gk-icon.png" width="100"></a> | <a href="../gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Visual_Studio_Code_1.35_icon.png" width=100></a> | <a href="../gui-tool-tutorials/sourcetree-macos-tutorial.md"><img alt="Sourcetree App" src="https://wac-cdn.atlassian.com/dam/jcr:81b15cde-be2e-4f4a-8af7-9436f4a1b431/Sourcetree-icon-blue.svg" width=100></a> | <a href="../gui-tool-tutorials/github-windows-intellij-tutorial.md"><img alt="IntelliJ IDEA" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/512px-IntelliJ_IDEA_Icon.svg.png" width=100></a> |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](../gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](../gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](../gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](../gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](../gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](../gui-tool-tutorials/github-windows-intellij-tutorial.md) |
