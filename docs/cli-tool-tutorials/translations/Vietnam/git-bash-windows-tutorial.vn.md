[![opensoure](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[<img align="right" width="150" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-old-version-tutorial/join-slack-team.png">](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![badges](https://www.codetriage.com/roshanjossey/first-contributions/badges/users.svg)](https://www.codetriage.com/roshanjossey/first-contributions)

# First Contributions (Đóng góp đầu tiên)

| <img alt="Git Bash" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/git_scm_logo_icon_170096.png" width="200"> | Phiên bản Git Bash |
| ------------------------------------------------------------------------------------------------------------------ | ---------------- |

Lần đầu tiên làm một điều gì đó luôn khó khăn, đặc biệt khi phải cộng tác với người khác. Việc mắc lỗi thường khiến chúng ta không thoải mái. Nhưng mã nguồn mở chính là về sự hợp tác và cùng nhau phát triển. Chúng tôi muốn đơn giản hóa quá trình để người mới có thể dễ dàng học và tham gia đóng góp open source lần đầu tiên.

Đọc bài viết và xem hướng dẫn rất hữu ích, nhưng không gì hiệu quả bằng việc “tự tay thực hành mà không sợ làm hỏng thứ gì”. Dự án này được tạo ra nhằm hướng dẫn người mới và giúp quá trình đóng góp đầu tiên trở nên đơn giản hơn. Hãy nhớ rằng: càng thoải mái, bạn càng học nhanh hơn. Nếu bạn đang muốn thực hiện đóng góp đầu tiên của mình, chỉ cần làm theo các bước đơn giản bên dưới. Chúng tôi đảm bảo điều đó sẽ rất thú vị!

Nếu bạn chưa cài Git Bash trên Windows, hãy [nhấn vào đây để cài đặt](https://git-scm.com/download/win)。

<img align="right" width="300" src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/fork.png" alt="fork this repository" />

## Fork repository này

Nhấn vào nút Fork ở góc trên bên phải của trang này để Fork repository.

Thao tác này sẽ tạo một bản sao repository trong tài khoản GitHub của bạn.

## Clone repository

Bây giờ hãy clone repository này về máy tính của bạn.

**Quan trọng: Đừng clone repository gốc. Hãy clone từ repository fork của chính bạn.**

Nhấn vào nút "Code", sau đó copy đường dẫn hiển thị bên dưới.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-1.png" alt="copy string" />

Mở ứng dụng Git Bash mà bạn vừa cài đặt. Trên Windows, giao diện của nó sẽ giống như hình bên dưới.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-1.png" alt="open git bash terminal" />

Sử dụng lệnh sau để di chuyển đến thư mục mà bạn muốn lưu project:

```bash
cd <folder>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-2.png" alt="cd into a folder" />

Sử dụng đường dẫn bạn vừa copy để chạy lệnh clone repository:

```bash
git clone <repo-url>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-clone-2.png" alt="clone the repository" />

Di chuyển vào thư mục project và mở nó bằng VS Code để chỉnh sửa.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-terminal-3.png" alt="cd into the newly cloned repo" />

## Tạo branch

Sử dụng lệnh sau để tạo branch mới và chuyển sang branch đó:

```bash
git checkout -b <branch-name>
```

Thay `<add-your-name>` bằng định dạng ví dụ như `"add-james-smith"`.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-branch.png" alt="create a branch" />

## Chỉnh sửa cần thiết và commit thay đổi

Mở file `Contributors.md` bằng trình soạn thảo văn bản, kéo xuống cuối file, thêm tên của bạn rồi lưu lại.

Ví dụ, nếu bạn tên là James Smith, hãy thêm:

\[James Smith](https://github.com/jamessmith)

Bạn có thể kiểm tra các file đã thay đổi bằng lệnh:

```bash
git status
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-status.png" alt="check the status" />

Bây giờ hãy commit thay đổi của bạn:

Đầu tiên, thêm thay đổi vào vùng staging:

```bash
git add file-name
```

Sau đó commit bằng lệnh:

```bash
git commit -m "Add your-name to Contributors list"
```

Hãy thay `<your-name>` bằng tên của bạn.

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-commit.png" alt="commit changes" />

Bạn có thể sử dụng lệnh `git log --oneline` để kiểm tra lịch sử commit.

## Push thay đổi lên GitHub

Sau khi hoàn thành các bước trên, sử dụng lệnh sau để push thay đổi lên GitHub:

```bash
git push origin <branch-name>
```

<img src="https://firstcontributions.github.io/assets/cli-tool-tutorials/git-bash-windows-tutorial/gb-push.png" alt="push changes" />

## Gửi thay đổi để review

Truy cập repository GitHub của bạn, bạn sẽ thấy nút `Compare & pull request`. Hãy nhấn vào đó.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/compare-and-pull.png" alt="create a pull request" />

Sau đó nhấn submit pull request.

<img src="https://firstcontributions.github.io/assets/gui-tool-tutorials/github-desktop-tutorial/submit-pull-request.png" alt="submit pull request" />

Một thời gian ngắn sau, thay đổi của bạn sẽ được merge vào branch chính. Khi được merge, bạn sẽ nhận email thông báo.

## Tiếp theo nên làm gì?

Chúc mừng! Bạn vừa hoàn thành quy trình chuẩn của open source:

fork -> clone -> edit -> PR

Đây là workflow mà bạn sẽ thường xuyên sử dụng khi tham gia các dự án mã nguồn mở trong tương lai!

Bạn cũng có thể chia sẻ đóng góp của mình với bạn bè thông qua [web app](https://firstcontributions.github.io#social-share)。

Nếu bạn có bất kỳ câu hỏi hoặc cần hỗ trợ, hãy tham gia Slack của chúng tôi:
[Join slack team](https://join.slack.com/t/firstcontributors/shared_invite/zt-1hg51qkgm-Xc7HxhsiPYNN3ofX2_I8FA)。

### [Tài liệu bổ sung](../additional-material/git_workflow_scenarios/additional-material.md)

## Hướng dẫn sử dụng các công cụ khác

[Quay lại trang chính](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools)
