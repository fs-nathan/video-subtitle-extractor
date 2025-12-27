# 📖 Hướng dẫn sử dụng GUI

## GUI đã được khởi động!

Nếu bạn thấy cửa sổ GUI, hãy làm theo các bước sau:

## Các bước sử dụng:

### 1. Mở file video
- Click nút **"打开"** (Open) ở góc trên bên trái
- Tìm và chọn file: `mukbang/input.mp4`
- Hoặc navigate đến: `/Users/nathan/Downloads/douyin/video-subtitle-extractor/mukbang/input.mp4`

### 2. Điều chỉnh vùng phụ đề
Sau khi video được load, bạn sẽ thấy:
- **Video preview** ở trên
- **4 slider** để điều chỉnh vùng phụ đề:
  - **Vertical (垂直)**: 2 slider bên trái - điều chỉnh vị trí Y (chiều dọc)
  - **Horizontal (水平)**: 2 slider bên phải - điều chỉnh vị trí X (chiều ngang)

**Cách điều chỉnh:**
- Kéo slider để chọn vùng phụ đề trên video
- Vùng được chọn sẽ hiển thị bằng khung màu xanh
- Dựa trên dữ liệu đã có, vùng phụ đề chính ở:
  - Y: khoảng 150-950 (phần dưới màn hình)
  - X: khoảng 900-1050 (bên phải)

### 3. Chọn cài đặt (Settings)
- Click nút **"设置"** (Settings)
- Chọn:
  - **识别模式 (Mode)**: "快速" (Fast) - nhanh nhất
  - **字幕语言 (Subtitle Language)**: "简体中文" (Simplified Chinese)
  - **界面语言 (Interface Language)**: "简体中文" (Simplified Chinese)

### 4. Chạy extraction
- Click nút **"运行"** (Run)
- Theo dõi progress bar ở dưới
- Quá trình có thể mất 10-30 phút tùy vào video

### 5. Kết quả
- File SRT sẽ được tạo tại: `mukbang/input.srt`
- File TXT (nếu được bật) tại: `mukbang/input.txt`

## Lưu ý:

⚠️ **Nếu GUI không hiển thị:**
- Kiểm tra terminal có lỗi gì không
- Thử chạy lại: `./RUN_GUI.sh`
- Hoặc: `source videoEnv312/bin/activate && python gui.py`

⚠️ **Nếu process bị kẹt:**
- Đợi thêm vài phút (OCR trên CPU rất chậm)
- Kiểm tra progress bar có đang tăng không
- Nếu không, có thể cần restart

⚠️ **Nếu muốn dừng:**
- Click nút X để đóng cửa sổ
- Hoặc nhấn Ctrl+C trong terminal

## Tips:

💡 **Để nhanh hơn:**
- Chỉ chọn vùng phụ đề chính xác (không chọn toàn bộ frame)
- Sử dụng Fast mode
- Nếu có GPU, cài PaddlePaddle GPU version

💡 **Nếu video có nhiều vùng phụ đề:**
- Chọn vùng phụ đề chính (thường ở dưới)
- Các vùng khác có thể được filter tự động

## Troubleshooting:

Nếu gặp lỗi, xem file:
- `TROUBLESHOOTING.md` - Hướng dẫn xử lý lỗi
- `SOLUTION.md` - Các giải pháp thay thế

