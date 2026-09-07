# Bài 006: Căn bậc 2

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 6

## Mô tả

Cho một số thực không âm a, hãy tính B = √a và in kết quả ra màn hình với hai chữ số thập phân.

## Yêu cầu

1. Đọc một số thực a từ bàn phím
2. Tính B = √a
3. In kết quả với 2 chữ số thập phân

## Input

- Một số thực a (0 ≤ a ≤ 10⁹).

## Output

- Một số thực là kết quả của B, có hai chữ số thập phân.

## Ví dụ

**Input:**
```
10
```

**Output:**
```
3.16
```

## Gợi ý

- Sử dụng `math.sqrt()` để tính căn bậc 2
- Cần import module `math`

## Kiến thức cần biết

- Module `math`: `math.sqrt()`
- Định dạng số thập phân: `f"{value:.2f}"`
