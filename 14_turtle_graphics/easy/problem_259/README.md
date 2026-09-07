# Bài 259: Vẽ hình vuông màu sắc

> **Chủ đề:** Vẽ hình với Turtle
> **Độ khó:** Easy
> **Số thứ tự:** 259

## Mô tả

Sử dụng thư viện Turtle để vẽ một hình vuông có cạnh 100 pixel, với viền màu đỏ và nền màu vàng nhạt.

## Yêu cầu

1. Tạo một con rùa (turtle)
2. Đặt màu viền là đỏ (`red`)
3. Đặt màu nền là vàng nhạt (`lightyellow`)
4. Vẽ hình vuông cạnh 100 pixel
5. Điền màu vào hình vuông
6. Đóng cửa sổ khi click chuột

## Ví dụ

Output sẽ là một cửa sổ hiển thị hình vuông:
- Viền: màu đỏ
- Nền: màu vàng nhạt
- Cạnh: 100 pixel

## Gợi ý

- Sử dụng `turtle.begin_fill()` và `turtle.end_fill()` để điền màu
- Dùng vòng lặp `for` với 4 lần lặp để vẽ 4 cạnh

## Kiến thức cần biết

- Thư viện `turtle`: thư viện vẽ hình có sẵn trong Python
- `turtle.forward()`: di chuyển tiến
- `turtle.right()`: quay phải
- `turtle.color()`: đặt màu
- `turtle.begin_fill()` / `turtle.end_fill()`: điền màu

## Thử thách thêm

1. Vẽ một hình tam giác màu xanh dương
2. Vẽ nhiều hình vuông xếp cạnh nhau tạo thành hàng
3. Tạo hoạt hình con rùa vẽ hình
