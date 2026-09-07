# Bài 010: Phép chia lấy phần nguyên và lấy phần dư

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 10

## Mô tả

Cho hai số nguyên a và b. Tính P là kết quả của a chia b lấy phần nguyên, và Q là kết quả của a chia b lấy phần dư.

## Yêu cầu

1. Đọc hai số nguyên a và b
2. Tính P = a // b (phần nguyên)
3. Tính Q = a % b (phần dư)
4. In P và Q cách nhau bởi dấu cách

## Input

- Hai số nguyên a, b (0 < a, b ≤ 10⁹), hai số trên một dòng, cách nhau bởi dấu cách.

## Output

- P và Q trên một dòng, cách nhau bởi dấu cách.

## Ví dụ

**Input:**
```
10 3
```

**Output:**
```
3 1
```

## Gợi ý

- Sử dụng `//` để chia lấy phần nguyên
- Sử dụng `%` để lấy phần dư

## Kiến thức cần biết

- Toán tử chia nguyên: `//`
- Toán tử lấy phần dư: `%`
- Quan hệ: a = (a // b) * b + (a % b)
