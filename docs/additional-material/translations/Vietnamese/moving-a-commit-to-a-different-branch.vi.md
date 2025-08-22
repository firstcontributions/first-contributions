# Di chuyển một commit tới một nhánh khác
Điều gì sẽ xảy ra nếu bạn thực hiện một cam kết và sau đó nhận ra mình đã thay đổi sai nhánh?
Làm thế nào để khắc phục lỗi này? Hướng dẫn này trả lời câu hỏi này.

## Di chuyển các cam kết mới nhất đến một nhánh hiện có
Để di chuyển theo cách này, gõ:

```git reset HEAD~ --soft``` - Hoàn nguyên lần xác nhận cuối cùng, nhưng giữ nguyên các thay đổi đã thực hiện.
```git stash``` - Lưu trạng thái của một thư mục.

```git kiểm tra <tên của nhánh chính xác>``` - Chuyển sang nhánh khác.
```git stash pop``` - Trả về trạng thái đã lưu cuối cùng.
```git add .``` - Thêm các tệp riêng lẻ.
```git commit -m "your comment"``` - Lưu và xác nhận các thay đổi.

Những thay đổi của bạn hiện đang ở đúng nhánh.


### Di chuyển các cam kết gần đây sang một nhánh mới
Để di chuyển theo cách này, gõ:
```git Branch newbranch``` - Tạo một nhánh mới, giữ nguyên tất cả các cam kết.
```git reset --hard HEAD~[n]``` - Đặt lại nhánh chính trở lại n lần xác nhận. Hãy nhớ rằng những thay đổi có trong các cam kết này sẽ bị xóa hoàn toàn khỏi nhánh chính.
```gitcheck newbranch``` - Chuyển sang nhánh bạn đã tạo. Nhánh này hiện chứa tất cả các cam kết.

Hãy nhớ rằng: Mọi thay đổi không có trong cam kết sẽ bị MẤT hoàn toàn.
