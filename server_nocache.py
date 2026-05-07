#!/usr/bin/env python3
"""
캐시 비활성화 헤더를 포함한 정적 파일 서버
"""
import http.server
import os

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # 로그 억제

if __name__ == '__main__':
    os.chdir('/home/ubuntu/roadsafer-dashboard')
    server = http.server.HTTPServer(('0.0.0.0', 8081), NoCacheHandler)
    print('No-cache server running on port 8081')
    server.serve_forever()
