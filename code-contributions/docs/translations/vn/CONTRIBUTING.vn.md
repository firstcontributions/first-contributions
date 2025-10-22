# Các bước để đóng góp

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />

## Fork (Sao chép) kho lưu trữ này bằng cách nhấp vào nút fork

## Clone fork của bạn (Kéo về về máy tính)

Trong fork của bạn của kho lưu trữ này, nhấp vào nút "Code". Chọn tab SSH và sau đó nhấp vào nút `copy to clipboard`.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Mở một terminal và chạy lệnh `git clone`

```bash
git clone "url bạn đã copy"
```

> [!IMPORTANT]
> Trong các bước sau, khi bạn thấy `<your-github-id>`, bạn nên thay thế bằng ID GitHub của bạn.  
> Ví dụ, nếu ID GitHub của bạn là `aaronsw`,  
> `git switch -c add-<your-github-id>` sẽ trở thành `git switch -c add-aaronsw`  
> `contributors/<your-github-id>.html` sẽ trở thành `contributors/aaronsw.html`

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## Tạo một nhánh (branch)

Chuyển đến thư mục kho lưu trữ nếu bạn chưa ở đó

```bash
cd code-contributions
```

Tạo một branch với lệnh `git switch`

```bash
git switch -c add-<your-github-id>
```

## Tạo card của bạn

Bạn có thể thêm card của mình dưới dạng file HTML trong thư mục `contributors`. Tạo một file với username của bạn trong thư mục `contributors`. Bạn có thể copy mẫu sau để bắt đầu.

`contributors/<your-github-id>.html`
```html
<article>
  <h3>Username của bạn</h3>
  <p>Một đoạn mô tả ngắn về bạn (tùy chọn)</p>
  <h4>Ngôn ngữ lập trình tôi sử dụng</h4>
  <section class="container">
    <div class="badge" style="background-color: #3874a4; color: white">
      Python
    </div>
    <div class="badge" style="background-color: #f7df1e; color: black;">
      JavaScript
    </div>
  </section>

  <h4>Công cụ tôi sử dụng</h4>
  <section class="container">
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bash/bash-original.svg"
    />
    <img
      class="icon"
      src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg"
    />
  </section>
</article>
<style>
  body {
    font-family: sans-serif;
  }
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .badge {
    padding: 0.5rem;
    border-radius: 0.25rem;
  }
  .icon {
    width: 2rem;
  }
</style>
```

## Thêm card của bạn vào danh sách contributors

Thêm tên file bạn đã tạo vào file `scripts/contributors.js`.

`scripts/contributors.js`
```js
const contributorFiles = [
  "<your-github-id>.html", // thêm tên file của bạn ở đây
  "roshanjossey.html",
  "gokultp.html",
];
```

## Xem thay đổi của bạn trong trình duyệt web

Bạn có thể xem thay đổi bằng cách mở `index.html` trong trình duyệt web. Bạn nên có thể thấy card mới bạn đã thêm ở các bước trước.

Bạn có thể tiếp tục thực hiện thay đổi cho card của bạn và làm mới tab trình duyệt để xem những thay đổi đó.

## Commit thay đổi của bạn

Đầu tiên, stage thay đổi của bạn với lệnh `git add`

```bash
git add contributors/<your-github-id>.html
```

Bây giờ, commit thay đổi của bạn với lệnh `git commit`

```bash
git commit -m "add <your-github-id>"
```

## Đẩy (Push) thay đổi của bạn lên GitHub

```bash
git push -u origin add-<your-github-id>
```

## Gửi đi (Submit) thay đổi của bạn để được review

Nếu bạn đến kho lưu trữ của mình trên GitHub, bạn sẽ thấy nút `Compare & pull request`. Nhấp vào nút đó.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Bây giờ, gửi yêu cầu đóng góp mã (submit pull request).

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Bạn sẽ nhận được email thông báo khi thay đổi đã được hợp nhất (merge).