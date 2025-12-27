# 📝 Giải thích về requirements_gpu.txt

## Tại sao có dòng `!pip install -r requirements_gpu.txt`?

Trong file `google_colab_en.ipynb`, có dòng:
```python
!pip install -r requirements_gpu.txt
```

### Lý do:

1. **Google Colab có GPU miễn phí**: 
   - Colab cung cấp GPU (NVIDIA) miễn phí
   - Để tận dụng GPU, cần cài dependencies phù hợp

2. **File requirements_gpu.txt**:
   - Chứa các dependencies cơ bản (giống `requirements.txt`)
   - **KHÔNG** chứa PaddlePaddle (sẽ được cài riêng sau)
   - Trong notebook, PaddlePaddle GPU được cài ở cell tiếp theo:
     ```python
     !pip install paddlepaddle-gpu==2.4.2.post117 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
     ```

3. **Tại sao tách riêng?**
   - PaddlePaddle GPU version phụ thuộc vào CUDA version
   - Colab có thể có CUDA version khác nhau
   - Tách riêng để dễ điều chỉnh theo môi trường

### So sánh:

| File | Mục đích | PaddlePaddle |
|------|----------|--------------|
| `requirements.txt` | CPU version | ❌ Không (cài riêng) |
| `requirements_gpu.txt` | GPU version (Colab) | ❌ Không (cài riêng) |
| `requirements_directml.txt` | DirectML/ONNX | ❌ Không (cài riêng) |

### Trong notebook, thứ tự cài đặt:

1. **Cell 1**: Clone repo
2. **Cell 2**: `!pip install -r requirements_gpu.txt` 
   - Cài các dependencies cơ bản
3. **Cell 3**: `!pip install paddlepaddle-gpu==2.4.2.post117 ...`
   - Cài PaddlePaddle GPU version phù hợp với Colab

### Lưu ý:

⚠️ **File `requirements_gpu.txt` ban đầu không có trong repo**:
- Có thể đã bị xóa hoặc chưa được commit
- Tôi đã tạo file này dựa trên `requirements.txt`
- Nội dung giống nhau vì chỉ khác ở PaddlePaddle (cài riêng)

### Nếu dùng Colab:

File `requirements_gpu.txt` đã được tạo và có thể sử dụng. Notebook sẽ hoạt động bình thường.

### Nếu chạy local với GPU:

Không cần `requirements_gpu.txt`, chỉ cần:
```bash
pip install paddlepaddle-gpu==3.0.0rc1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/
pip install -r requirements.txt
```

