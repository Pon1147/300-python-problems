# Bài 004: Phép toán chia

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 4

## Mô tả

Cho một số nguyên a, hãy tính B = a : 3 và in kết quả ra màn hình với hai chữ số thập phân.

## Yêu cầu

1. Đọc một số nguyên a từ bàn phím
2. Tính B = a / 3
3. In kết quả với 2 chữ số thập phân

## Input

- Một số nguyên a (|a| ≤ 10⁹).

## Output

- Một số thực duy nhất là kết quả của B, có hai chữ số thập phân.

## Ví dụ

**Input:**
```
10
```

**Output:**
```
3.33
```

## Gợi ý

- Sử dụng `/` để chia lấy số thực
- Sử dụng f-string: `f"{value:.2f}"` để định dạng 2 chữ số thập phân

## Kiến thức cần biết

- Toán tử chia: `/`
- Định dạng số thập phân: `f"{value:.2f}"`
