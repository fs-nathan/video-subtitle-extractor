# 🔧 Fix lỗi GUI không hiển thị

## Vấn đề
Python 3.12 từ Homebrew không có tkinter được compile.

## ✅ Giải pháp

### Cách 1: Sử dụng Python 3.9 (đã có tkinter)

```bash
cd /Users/nathan/Downloads/douyin/video-subtitle-extractor
source videoEnv/bin/activate
python gui.py
```

Hoặc dùng script:
```bash
./RUN_GUI_FIXED.sh
```

### Cách 2: Cài tkinter cho Python 3.12

```bash
# Cài python-tk
brew install python-tk@3.12

# Sau đó chạy với Python 3.12
source videoEnv312/bin/activate
python gui.py
```

## Kiểm tra tkinter

Để kiểm tra Python nào có tkinter:

```bash
# Python 3.9
source videoEnv/bin/activate
python -c "import tkinter; print('✅ tkinter OK')"

# Python 3.12
source videoEnv312/bin/activate
python -c "import tkinter; print('✅ tkinter OK')"
```

## Khuyến nghị

**Sử dụng Python 3.9 (videoEnv)** vì:
- ✅ Đã có tkinter
- ✅ Đã cài đặt đầy đủ packages
- ✅ Đã được test

**Lưu ý:** Python 3.9 có thể gặp vấn đề với multiprocessing, nhưng GUI thường ổn định hơn CLI.

## Nếu vẫn không thấy GUI

1. **Kiểm tra process:**
   ```bash
   ps aux | grep python | grep gui
   ```

2. **Kiểm tra lỗi:**
   ```bash
   source videoEnv/bin/activate
   python gui.py
   ```
   (Xem output trong terminal)

3. **Thử chạy với display:**
   - Đảm bảo bạn đang login vào macOS (không phải SSH)
   - Kiểm tra X11 forwarding nếu dùng SSH

4. **Alternative: Sử dụng Google Colab**
   - Không cần GUI
   - Có GPU miễn phí
   - Nhanh hơn nhiều

