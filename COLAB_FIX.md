# 🔧 Fix lỗi PaddlePaddle trong Google Colab

## Vấn đề

Notebook đang dùng version cũ `paddlepaddle-gpu==2.4.2.post117` không còn tồn tại.

## ✅ Giải pháp

### Option 1: Dùng version mới nhất (Khuyến nghị)

Thay dòng trong Cell 9:
```python
!pip install paddlepaddle-gpu==2.4.2.post117 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

Bằng:
```python
# For Colab with CUDA 11.8
!pip install paddlepaddle-gpu==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/
```

### Option 2: Dùng version 2.6.2 (nếu 3.0.0rc1 không hoạt động)

```python
!pip install paddlepaddle-gpu==2.6.2 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

### Option 3: Auto-detect và cài version phù hợp

```python
# Check CUDA version
!nvcc --version | grep "release" || echo "CUDA not found"

# Try version 3.0.0rc1 first (for CUDA 11.8)
!pip install paddlepaddle-gpu==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/ || \
pip install paddlepaddle-gpu==2.6.2 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

## Các version có sẵn

Theo lỗi bạn gặp, các version có sẵn:
- 2.6.0, 2.6.0.post112, 2.6.0.post116, 2.6.0.post117, 2.6.0.post120
- 2.6.1, 2.6.1.post112, 2.6.1.post116, 2.6.1.post117, 2.6.1.post120
- 2.6.2

## Khuyến nghị

**Sử dụng version 3.0.0rc1** (theo README mới nhất):
- Tương thích với project hiện tại
- Hỗ trợ tốt hơn
- Được khuyến nghị trong README

Nếu không hoạt động, fallback về **2.6.2** (version mới nhất trong danh sách có sẵn).

## Đã cập nhật notebook

File `google_colab_en.ipynb` đã được cập nhật với code tự động thử version 3.0.0rc1 trước, nếu fail thì dùng 2.6.2.

