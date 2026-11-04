# Thư mục weeks/

Cách 1 (nhanh): vào web, Cài đặt, Khu người hướng dẫn, Tải bài học lên, dán JSON của GPT, Lưu.
Cách 2 (mọi thiết bị đều thấy, không cần Firebase): bấm "Tải JSON" trong trang trên, bỏ file `week-N.json` vào thư mục này,
tạo file `index.json` liệt kê tên file, ví dụ `["week-1.json","week-2.json"]`, rồi đẩy lên GitHub và deploy lại.
Nội dung tải lên trong trình duyệt hoặc Firebase được ưu tiên hơn file trong thư mục này.
`example-week.json` chỉ là mẫu định dạng, không nằm trong index.json nên web không đọc nó.
