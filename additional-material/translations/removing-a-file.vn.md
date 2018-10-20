# Xóa tệp khỏi Git

Đôi khi, bạn có thể muốn xóa tệp khỏi Git nhưng không xóa tệp khỏi máy tính của mình. Bạn có thể đạt được điều này bằng cách sử dụng lệnh sau:

``git rm <file> --cached``

## Vậy chuyện gì đã xảy ra?

Git sẽ không theo dõi sự thay đổi của các tập tin đã bị xoá. Tất cả những gì Git biết là bạn đã xoá tệp rồi. Nếu bạn tìm tệp trong hệ thống tệp của mình, bạn sẽ thấy rằng nó vẫn còn ở đó.

Lưu ý rằng trong ví dụ trên, cờ `--cached` được sử dụng. Nếu chúng ta không add thêm cờ này, Git không chỉ xoá tệp repo, mà còn xoá khỏi hệ thống tệp của bạn.

Nếu bạn commit sự thay đổi bằng lệnh `git commit -m "Remove file1.js"` và push nó vào kho lưu trữ từ xa sử dụng  `git push origin master`, kho lưu trữ từ xa sẽ xoá tệp đó.

## Các tính năng bổ sung

-   Nếu bạn muốn xoá nhiều hơn một tệp, bạn có thể thêm tất cả các tệp trong cùng một lệnh:

    `git rm file1.js file2.js file3.js --cached`

-   Bạn có thể sử dụng ký tự đại diện (*) để xóa các tệp tương tự. Ví dụ: nếu bạn muốn xóa tất cả các tệp .txt khỏi kho lưu trữ cục bộ của mình:

    `git rm *.txt --cached`
