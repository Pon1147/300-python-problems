# Bài 014: Tính tổng hàng đơn vị

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 14

## Mô tả

Nhập vào hai số nguyên a và b. Tính tổng hàng đơn vị của hai số nguyên a và b.

## Yêu cầu

1. Đọc hai số nguyên a và b
2. Lấy chữ số hàng đơn vị của a (a % 10)
3. Lấy chữ số hàng đơn vị của b (b % 10)
4. In tổng hai chữ số hàng đơn vị

## Input

- Hai số nguyên a, b (0 ≤ a, b ≤ 10⁹), hai số trên một dòng, cách nhau bởi dấu cách.

## Output

- Một số nguyên là kết quả của bài toán.

## Ví dụ

**Input:**
```
123 456
```

**Output:**
```
9
```

## Gợi ý

- Sử dụng `a % 10` để lấy hàng đơn vị
- Sử dụng `b % 10` để lấy hàng đơn vị
- In tổng: `print(a % 10 + b % 10)`

## Kiến thức cần biết

- Toán tử `%`: lấy phần dư
