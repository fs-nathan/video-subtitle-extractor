# 🧹 Git Cleanup - Files không cần thiết

## Vấn đề

Git push chạy quá lâu vì có nhiều file/folder lớn không cần thiết đang được track.

## Files/Folders không cần thiết (đã thêm vào .gitignore)

### 1. Models (512MB) - **QUAN TRỌNG NHẤT**
- `backend/models/` - 512MB
  - V2: 154MB
  - V3: 135MB  
  - V4: 223MB
- **Lý do**: Models rất lớn, nên dùng Git LFS hoặc download riêng

### 2. Test Videos (328MB)
- `test/*.mp4`, `test/*.flv` - Các file video test
- **Lý do**: File video lớn, không cần commit

### 3. User Videos (46MB)
- `mukbang/` - Video của user
- `*.mp4`, `*.flv` - Bất kỳ video nào
- **Lý do**: User-specific, không nên commit

### 4. Output Files
- `output/` - Kết quả xử lý
- `*.srt`, `*.txt` - File output
- **Lý do**: Generated files, không cần version control

### 5. Virtual Environments
- `videoEnv/`, `videoEnv312/` - Python virtual environments
- **Lý do**: Có thể tạo lại, không nên commit

### 6. Config Files
- `settings.ini`, `subtitle.ini` - User configs
- **Lý do**: User-specific settings

### 7. Temporary Files
- `test_run*.py` - Test scripts tôi đã tạo
- `*_FIX.md`, `*_INSTRUCTIONS.md` - Documentation tạm
- `*.log` - Log files

### 8. Large Design Files
- `design/*.pdf` - Paper PDF
- `design/*.gif` - Demo GIFs (giữ lại demo.png và vse.ico)

## Cách cleanup

### Nếu files đã được commit trước đó:

```bash
# 1. Remove từ git tracking (nhưng giữ file local)
git rm -r --cached backend/models/
git rm -r --cached test/*.mp4 test/*.flv
git rm -r --cached mukbang/
git rm -r --cached output/
git rm -r --cached videoEnv/ videoEnv312/
git rm --cached settings.ini subtitle.ini

# 2. Commit changes
git add .gitignore
git commit -m "Remove large files from git tracking"

# 3. Push (sẽ nhanh hơn nhiều)
git push
```

### Nếu chưa commit:

```bash
# Chỉ cần add .gitignore và commit
git add .gitignore
git commit -m "Update .gitignore to exclude large files"
git push
```

## Kích thước ước tính

- Models: ~512MB
- Test videos: ~328MB
- User videos: ~46MB
- Virtual envs: ~500MB+
- **Tổng**: ~1.4GB+ không cần thiết

## Lưu ý

⚠️ **Models**: Nếu models đã được commit, cần remove khỏi git history:
```bash
# Sử dụng git filter-branch hoặc BFG Repo-Cleaner
# Hoặc tạo repo mới nếu chưa push lên remote
```

⚠️ **Nếu đã push lên GitHub**: 
- Files lớn vẫn còn trong git history
- Cần dùng `git filter-branch` hoặc tạo repo mới

## Khuyến nghị

1. **Models**: Sử dụng Git LFS hoặc release riêng
2. **Test videos**: Upload lên cloud storage riêng
3. **Virtual envs**: Không bao giờ commit
4. **Output files**: Luôn ignore

