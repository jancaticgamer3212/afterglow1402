
import http.server
import os
import traceback

ROOT = r"C:\Users\Jan\Downloads\PS4 14.02 Jailbreak Tests\afterglow-1402-chain-2026-11-11\afterglow-1402-chain"
LOG = os.path.join(ROOT, "serve.log")
PORT = 1337


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        message = self.address_string() + " " + (fmt % args)
        print(message, flush=True)

        try:
            with open(LOG, "a") as f:
                f.write(message + "\n")
        except Exception as e:
            print("Log error:", e, flush=True)

    def do_GET(self):
        if self.path.startswith("/ag_log"):
            self.send_response(200)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        super().do_GET()


try:
    os.chdir(ROOT)

    server = http.server.ThreadingHTTPServer(
        ("0.0.0.0", PORT), H
    )

    print("================================")
    print(" AG1402 HTTP SERVER")
    print("================================")
    print(f"Root: {ROOT}")
    print(f"Port: {PORT}")
    print(f"Local: http://127.0.0.1:{PORT}")
    print("Server is running...")
    print("Press CTRL+C to stop.")
    print("================================")

    server.serve_forever()

except KeyboardInterrupt:
    print("\nServer stopped.")

except Exception:
    traceback.print_exc()
    input("Press Enter to exit...")
