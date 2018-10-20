# Giữ fork của bạn đồng bộ với kho lưu trữ này

Trước tiên, việc quan trọng nhất là nên hiểu một luồng đồng bộ đầy đủ. Trong lược đồ này, có 3 kho lưu trữ khác nhau: kho lưu trữ công khai của tôi trên Github `github.com/Roshanjossey/first-contributions/`, kho lưu trữ fork của bạn trên GitHub `github.com/Your-Name/first-contributions/` và kho lưu trữ trên máy làm việc của bạn. Loại hợp tác này điển hình cho các dự án mã nguồn mở và được gọi là `Quy trình làm việc tam giác`.

<img style="float;" src="../../assets/triangle_workflow.png" alt="triangle workflow" />

Để giữ cho 2 kho lưu trữ của bạn đồng bộ với kho lưu trữ công khai của tôi, vì vậy đầu tiên chúng ta phải lấy và hợp nhất kho lưu trữ công khai với kho lưu trữ ở máy của bạn.
Bước thứ 2 của chúng ta là đẩy kho lưu trữ địa phương của bạn tới fork của bạn trên GitHub. Như bạn đã thấy trước đó, chỉ từ fork của bạn bạn có thể yêu cầu một "pull request". Vì vậy, fork của bạn trên GitHub là kho lưu trữ cuối cùng được cập nhật.

Bây giờ, hãy xem cách thực hiện:

Trước tiên, bạn phải ở trên nhánh chính của bạn. Để biết bạn đang ở nhánh nào, hãy kiểm tra dòng đầu tiên của:
```
git status
```
nếu bạn chưa sẵn sàng trên nhánh chính:
```
git checkout master
```

Sau đó bạn nên thêm kho lưu trữ công khai của tôi vào git của bạn với `add upstream remote-url`:
```
git remote add upstream https://github.com/Roshanjossey/first-contributions
```
Đây là một cách để nói với git rằng một phiên bản của dự án này tồn tại trong url được chỉ định và chúng ta đang gọi nó là `upstream`. Khi git của bạn có 1 cái tên hãy tìm nạp phiên bản mới nhất của kho lưu trữ công khai:
```
git fetch upstream
```

Bạn mới tìm nạp phiên bản mới nhất từ fork của tôi (`upstream` remote). Bây giờ, bạn cần hợp nhất kho lưu trữ công khai vào nhánh chính của bạn.
```
git rebase upstream/master
```
Ở đây bạn đang hợp nhất kho lưu trữ công khai với nhánh chính của bạn. Nhánh chính trên máy của bạn đã được cập nhật. Cuối cùng, nếu bạn đẩy nhánh chính của bạn lên fork của bạn, fork của bạn trên Github cũng sẽ có những thay đổi:
```
git push origin master
```
Lưu ý ở đây bạn đang đẩy tới remote có tên là `origin`.

Vì vậy, bây giờ hoặc tại thời điểm này, tất cả các kho lưu trữ của bạn đều được cập nhật. Làm tốt! Bạn nên làm điều này, mỗi lần kho lưu trữ trên GitHub của bạn cho bạn biết rằng bạn là một vài commits phía sau.
