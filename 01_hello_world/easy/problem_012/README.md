# Bài 012: Tìm chữ số

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 12

## Mô tả

Nhập vào một số nguyên a có 2 chữ số. Tìm chữ số hàng đơn vị và chữ số hàng chục của số nguyên a.

## Yêu cầu

1. Đọc một số nguyên a có 2 chữ số
2. Tìm chữ số hàng đơn vị (a % 10)
3. Tìm chữ số hàng chục (a // 10)
4. In hàng đơn vị trước, hàng chục sau, cách nhau bởi dấu cách

## Input

- Một số nguyên a (10 ≤ a ≤ 99).

## Output

- Chữ số hàng đơn vị và chữ số hàng chục trên một dòng, cách nhau bởi dấu cách.

## Ví dụ

**Input:**

```
35
```

**Output:**

```
5 3
```

## Gợi ý

- Sử dụng `% 10` để lấy chữ số hàng đơn vị
- Sử dụng `// 10` để lấy chữ số hàng chục

## Kiến thức cần biết

- Toán tử `%`: lấy phần dư
- Toán tử `//`: chia lấy phần nguyên
