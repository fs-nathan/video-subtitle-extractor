#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script test tối ưu để chạy subtitle extraction với file input.mp4
Sử dụng fast mode và chỉ định vùng phụ đề để tăng tốc
"""
import os
import sys
import multiprocessing
import configparser

# Thêm backend vào path
sys.path.insert(0, os.path.dirname(__file__))

# Đảm bảo sử dụng fast mode
def ensure_fast_mode():
    """Đảm bảo settings.ini sử dụng fast mode"""
    settings_file = os.path.join(os.path.dirname(__file__), 'settings.ini')
    config = configparser.ConfigParser()
    
    if os.path.exists(settings_file):
        config.read(settings_file, encoding='utf-8')
    else:
        config['DEFAULT'] = {}
    
    # Đặt mode thành fast
    config['DEFAULT']['Mode'] = 'fast'
    config['DEFAULT']['Language'] = 'ch'  # Tiếng Trung
    if 'Interface' not in config['DEFAULT']:
        config['DEFAULT']['Interface'] = '简体中文'
    
    with open(settings_file, 'w', encoding='utf-8') as f:
        config.write(f)
    print("✅ Đã cấu hình fast mode")

from backend.main import SubtitleExtractor

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    
    # Đảm bảo fast mode
    ensure_fast_mode()
    
    # Đường dẫn đến file video
    video_path = os.path.join(os.path.dirname(__file__), 'mukbang', 'input.mp4')
    
    # Kiểm tra file có tồn tại không
    if not os.path.exists(video_path):
        print(f"❌ File không tồn tại: {video_path}")
        sys.exit(1)
    
    print(f"📹 Đang xử lý video: {video_path}")
    print(f"📁 Kích thước file: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
    print("=" * 60)
    
    # Dựa trên dữ liệu raw.txt đã có, vùng phụ đề có vẻ ở:
    # Frame 1: (161, 923, 910, 1008) - ymin=161, ymax=923, xmin=910, xmax=1008
    # Frame 11: (149, 935, 900, 1032) - ymin=149, ymax=935, xmin=900, xmax=1032
    # Có 2 vùng phụ đề khác nhau, nhưng vùng chính có vẻ ở dưới cùng
    
    # Để tự động phát hiện, để None
    # Hoặc chỉ định vùng phụ đề để nhanh hơn (dựa trên dữ liệu đã có)
    # subtitle_area = (ymin, ymax, xmin, xmax)
    # Vùng phụ đề chính: y từ ~150-935, x từ ~900-1032
    # Nhưng để an toàn, để None để tự động phát hiện
    subtitle_area = None
    
    print("⚙️  Chế độ: FAST (nhanh)")
    print("⚙️  Vùng phụ đề: Tự động phát hiện")
    print("=" * 60)
    
    try:
        # Tạo đối tượng SubtitleExtractor
        se = SubtitleExtractor(video_path, subtitle_area)
        
        print(f"📊 Tổng số frame: {se.frame_count}")
        print(f"🎬 FPS: {se.fps}")
        print(f"📐 Kích thước: {se.frame_width}x{se.frame_height}")
        print("=" * 60)
        print("🚀 Bắt đầu xử lý...")
        print("   (Quá trình này có thể mất vài phút trên CPU)")
        print("=" * 60)
        
        # Chạy extraction
        se.run()
        
        print("\n" + "=" * 60)
        print("✅ Hoàn tất! File SRT đã được tạo tại:")
        srt_path = os.path.splitext(video_path)[0] + '.srt'
        if os.path.exists(srt_path):
            print(f"   {srt_path}")
            print(f"   Kích thước: {os.path.getsize(srt_path) / 1024:.2f} KB")
        else:
            print(f"   ⚠️  File SRT không tìm thấy tại: {srt_path}")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n⚠️  Đã dừng bởi người dùng (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Lỗi khi xử lý: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

