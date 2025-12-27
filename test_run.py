#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script test để chạy subtitle extraction với file input.mp4
"""
import os
import sys
import multiprocessing

# Thêm backend vào path
sys.path.insert(0, os.path.dirname(__file__))

from backend.main import SubtitleExtractor

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    
    # Đường dẫn đến file video
    video_path = os.path.join(os.path.dirname(__file__), 'mukbang', 'input.mp4')
    
    # Kiểm tra file có tồn tại không
    if not os.path.exists(video_path):
        print(f"❌ File không tồn tại: {video_path}")
        sys.exit(1)
    
    print(f"📹 Đang xử lý video: {video_path}")
    print(f"📁 Kích thước file: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
    print("=" * 60)
    print("⚠️  Lưu ý: Nếu video có phụ đề, bạn cần chỉ định vùng phụ đề")
    print("   Để tự động phát hiện, để trống subtitle_area (None)")
    print("=" * 60)
    
    # Để None để tự động phát hiện vùng phụ đề
    # Hoặc bạn có thể chỉ định: subtitle_area = (ymin, ymax, xmin, xmax)
    subtitle_area = None
    
    try:
        # Tạo đối tượng SubtitleExtractor
        se = SubtitleExtractor(video_path, subtitle_area)
        
        # Chạy extraction
        se.run()
        
        print("\n" + "=" * 60)
        print("✅ Hoàn tất! File SRT đã được tạo tại:")
        srt_path = os.path.splitext(video_path)[0] + '.srt'
        print(f"   {srt_path}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Lỗi khi xử lý: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

