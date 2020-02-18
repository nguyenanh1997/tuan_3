# tuan_3
Demo secure flag trong cookie
Run:  python3 Test.py
truy cập https://0.0.0.0:5000/ để set cookie
sau đó truy cập https://0.0.0.0:5000/test để chuyển hướng tới một trang khác có sử dụng https
(nếu trang được chuyển hướng tới sử dụng https thì cookie có secure flag là true sẽ được gửi. Nếu chỉ là giao thức http thì cookie đó sẽ không được gửi đi kèm) 
