# 🔧 Giải pháp cho vấn đề bị kẹt ở 11%

## Vấn đề
Quá trình OCR trên CPU rất chậm, đặc biệt với video lớn. Process không bị kẹt, chỉ là xử lý chậm.

## Giải pháp nhanh

### 1. Kiểm tra process có đang chạy không:
```bash
ps aux | grep python | grep test_run
```

### 2. Nếu muốn dừng và chạy lại với cấu hình tối ưu:

**Option A: Chạy với script tối ưu (đã tạo)**
```bash
source videoEnv/bin/activate
python test_run_optimized.py
```

**Option B: Chỉ định vùng phụ đề để nhanh hơn**

Dựa trên dữ liệu đã có trong `output/input/subtitle/raw.txt`, vùng phụ đề chính là:
- Y: từ 150 đến 935 (phần dưới màn hình)
- X: từ 900 đến 1032 (bên phải)

Bạn có thể chỉnh sửa `test_run.py` và thêm:
```python
# Chỉ định vùng phụ đề (ymin, ymax, xmin, xmax)
subtitle_area = (150, 935, 900, 1032)
```

### 3. Tối ưu cấu hình trong `backend/config.py`:

Đã giảm `EXTRACT_FREQUENCY` từ 3 xuống 2 để xử lý ít frame hơn.

Bạn cũng có thể:
- Giảm `EXTRACT_FREQUENCY` xuống 1 (chậm nhất nhưng chính xác nhất)
- Tăng `EXTRACT_FREQUENCY` lên 5 (nhanh hơn nhưng có thể bỏ sót phụ đề)

### 4. Kiểm tra tiến trình:

Xem file raw.txt đang được cập nhật:
```bash
tail -f output/input/subtitle/raw.txt
```

Nếu file vẫn đang được cập nhật, process vẫn đang chạy, chỉ là chậm.

### 5. Nếu muốn tiếp tục process hiện tại:

Process có thể vẫn đang chạy. Hãy kiểm tra:
```bash
# Xem process
ps aux | grep python

# Xem file đang được cập nhật
watch -n 1 'wc -l output/input/subtitle/raw.txt'
```

## Lưu ý

- **CPU mode rất chậm**: Với video 46MB, có thể mất 10-30 phút hoặc hơn
- **Fast mode**: Đã được cấu hình trong script tối ưu
- **GPU mode**: Nếu có GPU, sẽ nhanh hơn rất nhiều (cần cài PaddlePaddle GPU version)

## Khuyến nghị

1. **Nếu process vẫn chạy**: Hãy đợi thêm, OCR trên CPU rất chậm
2. **Nếu muốn nhanh hơn**: Dừng process và chạy lại với vùng phụ đề đã chỉ định
3. **Nếu có GPU**: Cài PaddlePaddle GPU version để tăng tốc đáng kể

