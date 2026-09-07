# Bài 007: Nghịch đảo

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 7

## Mô tả

Cho một số thực a, hãy tính B = 1/a và in kết quả ra màn hình với năm chữ số thập phân.

## Yêu cầu

1. Đọc một số thực a từ bàn phím
2. Tính B = 1/a
3. In kết quả với 5 chữ số thập phân

## Input

- Một số thực a (|a| ≤ 10⁹, a ≠ 0).

## Output

- Một số thực là kết quả của B, hiển thị năm chữ số thập phân.

## Ví dụ

**Input:**
```
3
```

**Output:**
```
0.33333
```

## Gợi ý

- Sử dụng `1 / a` để tính nghịch đảo
- Định dạng 5 chữ số thập phân: `f"{value:.5f}"`

## Kiến thức cần biết

- Toán tử chia: `/`
- Định dạng số thập phân: `f"{value:.5f}"`
