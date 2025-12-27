#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script test an toàn với error handling tốt hơn để tránh crash
"""
import os
import sys
import multiprocessing
import configparser
import signal
import traceback

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

# Giảm số worker processes để tránh memory issue
def reduce_worker_processes():
    """Giảm số worker processes trong config"""
    import backend.config as config_module
    importlib = __import__('importlib')
    importlib.reload(config_module)
    
    # Giảm REC_BATCH_NUM và MAX_BATCH_SIZE để giảm memory usage
    if hasattr(config_module, 'REC_BATCH_NUM'):
        config_module.REC_BATCH_NUM = 3  # Giảm từ 6 xuống 3
    if hasattr(config_module, 'MAX_BATCH_SIZE'):
        config_module.MAX_BATCH_SIZE = 5  # Giảm từ 10 xuống 5
    
    print("✅ Đã giảm batch size để tránh memory issue")

def signal_handler(sig, frame):
    """Xử lý signal để graceful shutdown"""
    print("\n⚠️  Đã nhận tín hiệu dừng, đang cleanup...")
    sys.exit(0)

if __name__ == '__main__':
    # Đăng ký signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Set multiprocessing start method
        try:
            multiprocessing.set_start_method("spawn", force=True)
        except RuntimeError:
            # Đã được set rồi, bỏ qua
            pass
        
        # Đảm bảo fast mode
        ensure_fast_mode()
        
        # Import sau khi đã set config
        from backend.main import SubtitleExtractor
        import backend.config as config_module
        import importlib
        
        # Giảm batch size
        reduce_worker_processes()
        
        # Đường dẫn đến file video
        video_path = os.path.join(os.path.dirname(__file__), 'mukbang', 'input.mp4')
        
        # Kiểm tra file có tồn tại không
        if not os.path.exists(video_path):
            print(f"❌ File không tồn tại: {video_path}")
            sys.exit(1)
        
        print(f"📹 Đang xử lý video: {video_path}")
        print(f"📁 Kích thước file: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
        print("=" * 60)
        print("⚙️  Chế độ: FAST (nhanh)")
        print("⚙️  Vùng phụ đề: Tự động phát hiện")
        print("⚙️  Batch size: Đã giảm để tránh memory issue")
        print("=" * 60)
        
        # Để tự động phát hiện
        subtitle_area = None
        
        try:
            # Tạo đối tượng SubtitleExtractor
            print("🔄 Đang khởi tạo SubtitleExtractor...")
            se = SubtitleExtractor(video_path, subtitle_area)
            
            print(f"📊 Tổng số frame: {se.frame_count}")
            print(f"🎬 FPS: {se.fps}")
            print(f"📐 Kích thước: {se.frame_width}x{se.frame_height}")
            print("=" * 60)
            print("🚀 Bắt đầu xử lý...")
            print("   (Quá trình này có thể mất vài phút trên CPU)")
            print("   Nhấn Ctrl+C để dừng an toàn")
            print("=" * 60)
            
            # Chạy extraction với try-catch
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
        except MemoryError as e:
            print(f"\n❌ Lỗi Memory: {e}")
            print("💡 Gợi ý: Thử giảm EXTRACT_FREQUENCY hoặc batch size")
            traceback.print_exc()
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Lỗi khi xử lý: {type(e).__name__}: {e}")
            traceback.print_exc()
            
            # Lưu error log
            err_log_path = os.path.join(os.path.expanduser('~'), 'VSE-Error-Message.log')
            with open(err_log_path, 'w', encoding='utf-8') as f:
                f.write(traceback.format_exc())
            print(f"\n📝 Error log đã được lưu tại: {err_log_path}")
            
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Lỗi khởi tạo: {type(e).__name__}: {e}")
        traceback.print_exc()
        sys.exit(1)

