# Bài 009: Tính giá trị biểu thức 2

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 9

## Mô tả

Cho ba số nguyên a, b, c, hãy tính các biểu thức:

- P = (21a² + 5b²) / (2009c² + 15)
- Q = √(a² - 2b) / (3c² + 4)

## Yêu cầu

1. Đọc ba số nguyên a, b, c
2. Tính P và Q theo công thức
3. In kết quả trên cùng một dòng

## Input

- Ba số nguyên a, b, c (|a|, |b|, |c| ≤ 10⁹), trên cùng một dòng, cách nhau bởi dấu cách.

## Output

- P và Q trên một dòng, cách nhau bởi dấu cách, có bốn chữ số thập phân.

## Ví dụ

**Input:**
```
1 1 1
```

**Output:**
```
0.0050 0.1429
```

## Gợi ý

- Sử dụng `map(int, input().split())` để đọc nhiều số trên cùng một dòng
- Sử dụng `math.sqrt()` cho căn bậc 2

## Kiến thức cần biết

- Đọc nhiều số trên cùng một dòng: `input().split()`
- Module `math`: `math.sqrt()`
