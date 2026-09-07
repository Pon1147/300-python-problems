# Bài 011: Chia táo

> **Chủ đề:** Phép toán cơ bản
> **Độ khó:** Easy
> **Số thứ tự:** 11

## Mô tả

Cho số học sinh của một lớp (HS) và số táo trong rổ (T). Hãy chia đều số táo cho tất cả học sinh trong lớp. Hỏi mỗi bạn sẽ được bao nhiêu quả táo? Còn dư lại bao nhiêu quả?

## Yêu cầu

1. Đọc số táo T và số học sinh HS
2. Tính số táo mỗi học sinh được chia (T // HS)
3. Tính số táo còn dư (T % HS)
4. In kết quả trên cùng một dòng

## Input

- Hai số nguyên trên một dòng, cách nhau bởi dấu cách theo thứ tự là T và HS (0 < T, HS < 10⁹).

## Output

- Là số táo mỗi học sinh được chia và số táo còn dư trên cùng một dòng, cách nhau bởi dấu cách.

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

- Đây là bài chia có dư thực tế
- Sử dụng `//` để tính số táo mỗi người
- Sử dụng `%` để tính số táo dư

## Kiến thức cần biết

- Toán tử chia nguyên: `//`
- Toán tử lấy phần dư: `%`
- Quan hệ: T = (T // HS) \* HS + (T % HS)
