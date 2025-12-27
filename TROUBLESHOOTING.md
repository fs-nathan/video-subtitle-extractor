# 🔧 Troubleshooting - Vấn đề dừng ở 14%

## Vấn đề
Process bị dừng hoặc crash ở khoảng 14% khi xử lý OCR trên macOS với Python 3.9.

## Nguyên nhân có thể

1. **Multiprocessing issue trên macOS**: macOS có vấn đề với `spawn` method trong multiprocessing, đặc biệt khi load model trong subprocess
2. **Memory issue**: OCR model loading trong subprocess có thể gây memory leak
3. **Import path issue**: Subprocess không tìm thấy module đúng cách

## Giải pháp đã thử

### ✅ Đã sửa
- Import paths (`from backend.tools.constant` thay vì `from tools.constant`)
- Giảm batch size (REC_BATCH_NUM: 6→3, MAX_BATCH_SIZE: 10→5)
- Giảm EXTRACT_FREQUENCY (3→2)
- Tạo script với error handling tốt hơn

### 🔄 Đang thử
- Chỉ định vùng phụ đề để giảm tải xử lý
- Fast mode

## Giải pháp thay thế

### Option 1: Sử dụng GUI thay vì CLI
GUI có thể ổn định hơn với multiprocessing:
```bash
source videoEnv/bin/activate
python gui.py
```

### Option 2: Chạy với Python 3.12+
Project khuyến nghị Python 3.12+. Cài đặt:
```bash
brew install python@3.12
python3.12 -m venv videoEnv312
source videoEnv312/bin/activate
pip install paddlepaddle==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
pip install -r requirements.txt
```

### Option 3: Chạy trên Google Colab
Project hỗ trợ Google Colab với GPU miễn phí:
- Mở: https://colab.research.google.com/github/YaoFANGUK/video-subtitle-extractor/blob/main/google_colab.ipynb
- Upload video và chạy

### Option 4: Sử dụng pre-built binary
Tải pre-built binary từ releases để tránh vấn đề môi trường:
- Windows: https://github.com/YaoFANGUK/video-subtitle-extractor/releases
- macOS: Có thể cần build từ source

### Option 5: Giảm video resolution
Nếu video quá lớn, có thể resize trước:
```bash
ffmpeg -i input.mp4 -vf scale=720:1280 input_small.mp4
```

## Kiểm tra process

```bash
# Xem process có đang chạy
ps aux | grep python | grep test_run

# Xem output file
tail -f output/input/subtitle/raw.txt

# Xem memory usage
top -pid $(pgrep -f "python.*test_run")
```

## Nếu process bị kẹt

1. **Kiểm tra log**: `~/VSE-Error-Message.log`
2. **Kiểm tra output**: `output/input/subtitle/raw.txt` có đang được cập nhật không
3. **Dừng và thử lại**: 
   ```bash
   pkill -f "python.*test_run"
   # Thử với vùng phụ đề đã chỉ định
   python test_run_simple.py
   ```

## Khuyến nghị

**Nếu bạn cần kết quả nhanh:**
- Sử dụng Google Colab (GPU miễn phí, nhanh hơn nhiều)
- Hoặc chạy GUI version

**Nếu muốn fix local:**
- Nâng cấp lên Python 3.12+
- Hoặc chờ process hoàn thành (có thể mất 30-60 phút trên CPU)

## Thông tin hệ thống

- OS: macOS 15.6.1 (ARM64)
- Python: 3.9.6
- PaddlePaddle: 3.0.0rc1 (CPU)
- Video: 1080x1920, 2727 frames, 30fps

