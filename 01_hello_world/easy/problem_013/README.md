# Bài 013: Tính tổng chữ số

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 13

## Mô tả

Nhập vào một số nguyên a có 4 chữ số. Tính tổng các chữ số của a.

## Yêu cầu

1. Đọc một số nguyên a có 4 chữ số
2. Tách các chữ số hàng nghìn, trăm, chục, đơn vị
3. Tính tổng 4 chữ số
4. In kết quả

## Input

- Một số nguyên a (1000 ≤ a ≤ 9999).

## Output

- Một số nguyên là kết quả của bài toán.

## Ví dụ

**Input:**

```
1234
```

**Output:**

```
10
```

## Gợi ý

- Hàng nghìn: `a // 1000`
- Hàng trăm: `(a // 100) % 10`
- Hàng chục: `(a // 10) % 10`
- Hàng đơn vị: `a % 10`

## Kiến thức cần biết

- Toán tử `%`: lấy phần dư
- Toán tử `//`: chia lấy phần nguyên
