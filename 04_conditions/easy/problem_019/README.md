# Bài 019: Kiểm tra số dương hay âm

> **Chủ đề:** Điều kiện (if/elif/else)
> **Độ khó:** Easy
> **Số thứ tự:** 19

## Mô tả

Bạn hãy viết chương trình nhận vào một số nguyên và thông báo số đó là số dương, số âm hay bằng 0.

## Yêu cầu

1. Nhận vào 1 số nguyên từ người dùng
2. Nếu số > 0: in ra `So duong`
3. Nếu số < 0: in ra `So am`
4. Nếu số = 0: in ra `So 0`

## Ví dụ

**Ví dụ 1:**

Input:
```
5
```

Output:
```
So duong
```

**Ví dụ 2:**

Input:
```
-3
```

Output:
```
So am
```

**Ví dụ 3:**

Input:
```
0
```

Output:
```
So 0
```

## Gợi ý

- Sử dụng `if/elif/else` để kiểm tra điều kiện
- So sánh số với 0 bằng toán tử `>`, `<`, `==`

## Kiến thức cần biết

- Câu lệnh điều kiện `if/elif/else`
- Toán tử so sánh: `>`, `<`, `==`
- Hàm `int()` để chuyển chuỗi thành số

## Thử thách thêm

Mở rộng chương trình: nếu số dương, in thêm "La so le" hoặc "La so chan" tùy vào tính chẵn lẻ của số đó.
