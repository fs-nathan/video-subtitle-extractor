#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script đơn giản với vùng phụ đề đã chỉ định để tránh crash
"""
import os
import sys
import multiprocessing
import configparser

# Thêm backend vào path
sys.path.insert(0, os.path.dirname(__file__))

def ensure_fast_mode():
    """Đảm bảo settings.ini sử dụng fast mode"""
    settings_file = os.path.join(os.path.dirname(__file__), 'settings.ini')
    config = configparser.ConfigParser()
    
    if os.path.exists(settings_file):
        config.read(settings_file, encoding='utf-8')
    else:
        config['DEFAULT'] = {}
    
    config['DEFAULT']['Mode'] = 'fast'
    config['DEFAULT']['Language'] = 'ch'
    if 'Interface' not in config['DEFAULT']:
        config['DEFAULT']['Interface'] = '简体中文'
    
    with open(settings_file, 'w', encoding='utf-8') as f:
        config.write(f)
    print("✅ Đã cấu hình fast mode")

if __name__ == '__main__':
    try:
        multiprocessing.set_start_method("spawn", force=True)
    except RuntimeError:
        pass
    
    ensure_fast_mode()
    
    from backend.main import SubtitleExtractor
    
    video_path = os.path.join(os.path.dirname(__file__), 'mukbang', 'input.mp4')
    
    if not os.path.exists(video_path):
        print(f"❌ File không tồn tại: {video_path}")
        sys.exit(1)
    
    print(f"📹 Video: {video_path}")
    print(f"📁 Kích thước: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
    print("=" * 60)
    
    # Dựa trên dữ liệu đã có trong raw.txt:
    # Frame 1: (161, 923, 910, 1008) - vùng phụ đề chính ở dưới
    # Frame 46: (318, 760, 1350, 1422) - vùng phụ đề phụ ở trên
    
    # Chỉ định vùng phụ đề chính (dưới màn hình)
    # Video resolution: 1080x1920
    # Vùng phụ đề chính: y từ 150-950, x từ 900-1050
    # Format: (ymin, ymax, xmin, xmax)
    subtitle_area = (150, 950, 900, 1050)
    
    print("⚙️  Chế độ: FAST")
    print(f"⚙️  Vùng phụ đề: {subtitle_area}")
    print("   (Đã chỉ định để tránh xử lý toàn bộ frame)")
    print("=" * 60)
    
    try:
        print("🔄 Đang khởi tạo...")
        se = SubtitleExtractor(video_path, subtitle_area)
        
        print(f"📊 Frame: {se.frame_count}, FPS: {se.fps}")
        print(f"📐 Size: {se.frame_width}x{se.frame_height}")
        print("=" * 60)
        print("🚀 Bắt đầu xử lý...")
        print("=" * 60)
        
        se.run()
        
        srt_path = os.path.splitext(video_path)[0] + '.srt'
        if os.path.exists(srt_path):
            print("\n" + "=" * 60)
            print(f"✅ Hoàn tất! File SRT: {srt_path}")
            print(f"   Kích thước: {os.path.getsize(srt_path) / 1024:.2f} KB")
            print("=" * 60)
        else:
            print(f"\n⚠️  File SRT không tìm thấy: {srt_path}")
            
    except KeyboardInterrupt:
        print("\n⚠️  Đã dừng bởi người dùng")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Lỗi: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        
        err_log = os.path.join(os.path.expanduser('~'), 'VSE-Error-Message.log')
        with open(err_log, 'w', encoding='utf-8') as f:
            f.write(traceback.format_exc())
        print(f"📝 Error log: {err_log}")
        sys.exit(1)

