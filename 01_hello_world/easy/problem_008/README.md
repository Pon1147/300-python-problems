# Bài 008: Tính giá trị biểu thức 1

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 8

## Mô tả

Cho hai số nguyên a và b, hãy tính các biểu thức:

- P = 21a + 5b - 2009
- Q = (21a² - 5b) / (2009b²)
- R = (21a + 5b²) / (2009b + 15)

## Yêu cầu

1. Đọc hai số nguyên a và b
2. Tính P, Q, R theo công thức
3. In kết quả theo định dạng yêu cầu

## Input

- Hai số nguyên a, b (|a|, |b| ≤ 10⁹), mỗi số một dòng.

## Output

- Dòng một: P và Q, cách nhau bởi dấu cách, Q có bốn chữ số thập phân.
- Dòng hai: R, có sáu chữ số thập phân.

## Ví dụ

**Input:**
```
1
1
```

**Output:**
```
-1983 0.0020
0.005253
```

## Gợi ý

- Sử dụng ngoặc đơn `()` để đảm bảo thứ tự tính đúng
- P là số nguyên, Q và R là số thực

## Kiến thức cần biết

- Thứ tự thực hiện phép toán: ngoặc → lũy thừa → nhân/chia → cộng/trừ
- Định dạng số thập phân: `f"{value:.nf}"`
