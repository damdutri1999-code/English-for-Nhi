# Thư mục weeks/

Cách 1 (nhanh): vào web, Cài đặt, Khu người hướng dẫn, Tải bài học lên, dán JSON của GPT, Lưu. Bài được lưu lên Supabase.
Cách 2 (dự phòng, không cần database): bấm "Tải JSON" trong trang trên, bỏ file `week-N.json` vào thư mục này,
tạo file `index.json` liệt kê tên file, ví dụ `["week-1.json","week-2.json"]`, rồi đẩy lên GitHub.
Nội dung tải lên trong trình duyệt hoặc đám mây được ưu tiên hơn file trong thư mục này.
`example-week.json` chỉ là mẫu định dạng, không nằm trong index.json nên web không đọc nó.

Bài của **Trí** nằm ở thư mục `weeks-tri/` (cùng cách làm, có `index.json` riêng). `weeks-tri/example-week.json` là tuần 1 của Trí ở dạng rút gọn để xem định dạng (có bảng/biểu đồ số liệu và bài nói); prompt đầy đủ nằm ở `prompts/PROMPT-GPT-tri.md`, brief nằm ở `briefs/tri/`.
