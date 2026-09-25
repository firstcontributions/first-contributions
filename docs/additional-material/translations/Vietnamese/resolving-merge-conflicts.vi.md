# Mâu Thuẫn Khi Tích Hợp là gì?

Khi bạn cố gắng tích hợp một nhánh khác vào nhánh làm việc hiện tại của bạn, bạn đang thực hiện các thay đổi từ bối cảnh khác và kết hợp chúng với các tệp tin hiện tại bạn đang làm việc.
Nếu hai người đã thay đổi cùng một dòng trong cùng một tệp hoặc nếu một người quyết định xóa nó trong khi người kia quyết định sửa đổi nó, Git không thể xác định đâu là phiên bản chính xác. Git sau đó sẽ đánh dấu tệp là có xung đột - điều mà bạn sẽ phải giải quyết trước khi bạn có thể tiếp tục công việc của mình.

# Làm thế nào để giải quyết xung đột khi tích hợp?

Khi đối mặt với việc xảy ra xung đột khi tích hợp, Git sẽ đánh dấu khu vực có vấn đề trong tệp bằng cách đặt nó vào trong các nhãn bắt đầu và tên nhánh khác.

Các nội dung sau điểm đánh dấu đầu tiên bắt nguồn từ nhánh làm việc hiện tại của bạn. Sau nhãn bắt đầu, Git cho chúng ta biết những thay đổi đến từ đâu (từ nhánh nào). Dòng phân tách cho thấy sự chia tách giữa hai phiên bản đang xung đột. Công việc của chúng tôi bây giờ là giải quyết những dòng này: khi chúng ta hoàn thành, tệp sẽ trông chính xác như chúng ta muốn. Nên tham khảo ý kiến của người đồng đội đã viết những thay đổi mâu thuẫn để quyết định phiên bản nào sẽ là bản cuối cùng. Nó có thể là của bạn - hoặc có thể là hỗn hợp giữa hai người.

Ví dụ:
```
# Nội dung từ nhánh hiện tại
This is my third line

# Nội dung từ nhánh khác
This is a fourth line I am adding
```

`HEAD`: Cho biết nơi bắt đầu của các dòng có xung đột khi tích hợp. Những dòng đầu tiên là các dòng từ tệp tin mà bạn đang thử tích hợp các thay đổi vào.
Dòng phân tách: Cho biết điểm phân chia được sử dụng để so sánh các thay đổi. Phân chia các thay đổi mà người dùng đã cam kết (ở trên) đối với các thay đổi đến từ nhánh tích hợp (bên dưới) để thấy rõ sự khác biệt.
`branch-name`: Cho biết kết thúc của các dòng có xung đột khi tích hợp.

Bạn giải quyết xung đột bằng cách chỉnh sửa tệp và sau đó tích hợp thủ công các phần của tệp mà git gặp sự cố khi tích hợp. Điều này có thể có nghĩa là loại bỏ các thay đổi của bạn hoặc của người khác hoặc đi tới việc kết hợp thay đổi của cả hai. Bạn cũng sẽ cần xóa các dòng đánh dấu xung đột trong tệp.

Một khi bạn đã giải quyết xung đột, chạy lệnh `git add`. Đừng quên chạy thử nghiệm, vì bạn phải chắc chắn rằng bạn đã giải quyết được xung đột.

Bạn cũng có thể tải xuống các plugin khác nhau tùy thuộc vào IDE bạn đang sử dụng để có cách dễ dàng hơn để giải quyết xung đột hợp nhất.

# Làm thế nào để hoàn tác lại tích hợp?

Nếu bạn muốn hoàn tác lại tích hợp thì bạn có thể thực hiện `git merge —abort`
