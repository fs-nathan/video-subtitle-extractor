# 🎯 Giải pháp cho vấn đề Python Crash trên macOS

## Vấn đề
Python bị crash khi chạy CLI version do vấn đề với multiprocessing trên macOS.

## ✅ Giải pháp khuyến nghị: Sử dụng GUI

GUI version ổn định hơn và đã được test kỹ trên macOS:

```bash
cd /Users/nathan/Downloads/douyin/video-subtitle-extractor
source videoEnv312/bin/activate
python gui.py
```

### Cách sử dụng GUI:

1. **Mở file video:**
   - Click nút "打开" (Open)
   - Chọn file `mukbang/input.mp4`

2. **Điều chỉnh vùng phụ đề:**
   - Sử dụng các slider để chọn vùng phụ đề trên video preview
   - Vùng phụ đề sẽ được highlight bằng khung màu xanh

3. **Chọn chế độ:**
   - Click nút "设置" (Settings)
   - Chọn "快速" (Fast) mode
   - Chọn ngôn ngữ: "简体中文" (Chinese)

4. **Chạy extraction:**
   - Click nút "运行" (Run)
   - Theo dõi progress bar

5. **Kết quả:**
   - File SRT sẽ được tạo cùng thư mục với video
   - `mukbang/input.srt`

## 🚀 Giải pháp nhanh nhất: Google Colab

Nếu GUI vẫn có vấn đề, sử dụng Google Colab (có GPU miễn phí, nhanh hơn 10-20 lần):

1. **Mở notebook:**
   - https://colab.research.google.com/github/YaoFANGUK/video-subtitle-extractor/blob/main/google_colab_en.ipynb

2. **Upload video:**
   - Click "Files" → "Upload to session storage"
   - Upload file `input.mp4`

3. **Chạy các cells:**
   - Chạy từng cell theo thứ tự
   - Kết quả sẽ được tạo trong vài phút (thay vì hàng giờ trên CPU)

4. **Download kết quả:**
   - File SRT sẽ được tạo và có thể download

## 📝 Thông tin môi trường hiện tại

- **OS:** macOS 15.6.1 (ARM64)
- **Python:** 3.12.5 ✅
- **Virtual Environment:** `videoEnv312/` ✅
- **Packages:** Đã cài đặt đầy đủ ✅
- **Vấn đề:** Multiprocessing crash trên macOS

## 🔍 Nguyên nhân

Multiprocessing với `spawn` method trên macOS có vấn đề khi:
- Load model trong subprocess
- Share memory giữa processes
- Python 3.9 có vấn đề đặc biệt, Python 3.12 tốt hơn nhưng vẫn có thể crash

## 💡 Khuyến nghị

**Nếu bạn cần kết quả ngay:**
→ Sử dụng **Google Colab** (nhanh nhất, có GPU)

**Nếu muốn chạy local:**
→ Sử dụng **GUI version** (ổn định hơn CLI)

**Nếu vẫn muốn CLI:**
→ Có thể cần chờ bản fix từ developers hoặc sử dụng Docker container

## 📞 Hỗ trợ

Nếu vẫn gặp vấn đề:
1. Kiểm tra error log: `~/VSE-Error-Message.log`
2. Xem troubleshooting: `TROUBLESHOOTING.md`
3. Tạo issue trên GitHub: https://github.com/YaoFANGUK/video-subtitle-extractor/issues

