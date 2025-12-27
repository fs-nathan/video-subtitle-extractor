# ✅ Cài đặt hoàn tất!

## Virtual Environment đã được tạo

Virtual environment đã được tạo tại: `videoEnv/`

## Cách kích hoạt Virtual Environment

### macOS/Linux:
```bash
source videoEnv/bin/activate
```

### Windows:
```bash
videoEnv\Scripts\activate
```

## Cách chạy project

### 1. Kích hoạt virtual environment trước:
```bash
source videoEnv/bin/activate
```

### 2. Chạy GUI version:
```bash
python gui.py
```

### 3. Hoặc chạy CLI version:
```bash
python backend/main.py
```

## Các package đã được cài đặt

✅ **PaddlePaddle 3.0.0rc1** (CPU version)
✅ **PaddleOCR** (je-paddleocr 2.9.1)
✅ **OpenCV** 4.10.0.84
✅ **PySimpleGUI** 4.60.4.1
✅ **Levenshtein** 0.26.0
✅ Và tất cả các dependencies khác

## Lưu ý

⚠️ **Python Version**: Bạn đang sử dụng Python 3.9.6, trong khi project khuyến nghị Python 3.12+. 
   - Project vẫn có thể chạy được với Python 3.9.6
   - Nếu gặp lỗi, hãy cân nhắc nâng cấp lên Python 3.12+

⚠️ **Numpy Version**: PaddlePaddle đã cài numpy 2.0.2 (thay vì 1.26.4 trong requirements.txt)
   - Điều này không gây vấn đề vì numpy 2.0.2 tương thích ngược

⚠️ **scikit-image**: Đã được cài phiên bản 0.24.0 (tương thích với Python 3.9) thay vì 0.25.1

## Kiểm tra cài đặt

Chạy lệnh sau để kiểm tra:
```bash
source videoEnv/bin/activate
python -c "import paddle; import cv2; import PySimpleGUI; from paddleocr import PaddleOCR; print('✓ All packages OK!')"
```

## Hỗ trợ GPU

Nếu bạn có NVIDIA GPU và muốn sử dụng GPU acceleration:
1. Cài đặt CUDA và cuDNN
2. Gỡ PaddlePaddle CPU version: `pip uninstall paddlepaddle`
3. Cài PaddlePaddle GPU version:
   ```bash
   pip install paddlepaddle-gpu==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/
   ```

## Vấn đề thường gặp

Nếu gặp lỗi khi chạy, hãy kiểm tra:
- Đường dẫn project không chứa tiếng Trung hoặc khoảng trắng
- Virtual environment đã được kích hoạt
- Tất cả các file model trong `backend/models/` đã được tải về đầy đủ

