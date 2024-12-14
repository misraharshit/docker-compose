from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import psutil

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Here creating json to Collect CPU and memory stats
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        metrics = {
            "cpu_percent": cpu_percent,
            "memory": {
                "total": memory.total,
                "used": memory.used,
                "free": memory.free,
                "percent": memory.percent,
            },
        }

        # Preparing response..
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(metrics).encode())

# Start the HTTP server on port 5050
def run_server():
    server_address = ('0.0.0.0', 5050)
    httpd = HTTPServer(server_address, MetricsHandler)
    print("Starting server on port 5050...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

