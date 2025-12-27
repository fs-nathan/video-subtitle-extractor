#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script test KHÔNG dùng multiprocessing để tránh crash trên macOS
Sử dụng single process với threading thay vì multiprocessing
"""
import os
import sys
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
    ensure_fast_mode()
    
    # Import sau khi đã set config
    from backend.main import SubtitleExtractor
    
    video_path = os.path.join(os.path.dirname(__file__), 'mukbang', 'input.mp4')
    
    if not os.path.exists(video_path):
        print(f"❌ File không tồn tại: {video_path}")
        sys.exit(1)
    
    print(f"📹 Video: {video_path}")
    print(f"📁 Kích thước: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
    print("=" * 60)
    
    # Chỉ định vùng phụ đề để giảm tải xử lý
    # Dựa trên dữ liệu: vùng phụ đề chính ở dưới màn hình
    subtitle_area = (150, 950, 900, 1050)  # (ymin, ymax, xmin, xmax)
    
    print("⚙️  Chế độ: FAST")
    print(f"⚙️  Vùng phụ đề: {subtitle_area}")
    print("⚙️  Single process mode (không dùng multiprocessing)")
    print("=" * 60)
    
    try:
        print("🔄 Đang khởi tạo...")
        
        # Tạm thời patch multiprocessing để dùng threading
        # Note: Đây là workaround, có thể không hoạt động hoàn hảo
        import backend.tools.subtitle_ocr as subtitle_ocr_module
        original_async_start = subtitle_ocr_module.async_start
        
        def mock_async_start(video_path, raw_subtitle_path, sub_area, options):
            """Mock async_start để không dùng multiprocessing"""
            import queue
            import threading
            from backend.tools.subtitle_ocr import subtitle_extract_handler
            
            task_queue = queue.Queue()
            progress_queue = queue.Queue()
            
            # Chạy trong thread thay vì process
            thread = threading.Thread(
                target=subtitle_extract_handler,
                args=(task_queue, progress_queue, video_path, raw_subtitle_path, sub_area, 
                      type('Options', (), options)()),
                daemon=True
            )
            thread.start()
            
            return thread, task_queue, progress_queue
        
        # Patch function
        subtitle_ocr_module.async_start = mock_async_start
        
        se = SubtitleExtractor(video_path, subtitle_area)
        
        print(f"📊 Frame: {se.frame_count}, FPS: {se.fps}")
        print(f"📐 Size: {se.frame_width}x{se.frame_height}")
        print("=" * 60)
        print("🚀 Bắt đầu xử lý...")
        print("   (Single process mode - có thể chậm hơn nhưng ổn định hơn)")
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

