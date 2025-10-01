import sys
import json
import base64
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

json_file = Path("../data/processed/modified_sms_v2.json")

transactions = []
next_id = 1

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "secret"


def load_data():
    global transactions, next_id
    
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            transactions = json.load(f)
    else:
        print("Records Json file does not exist.")
        sys.exit(1)
    
    # make sure every trans has an integer id
    for i, tr in enumerate(transactions, start=1):
        tr["id"] = i
    next_id = len(transactions) + 1

def save_data():
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent=4, ensure_ascii=False)

class HTTPHandler(BaseHTTPRequestHandler):

    def _check_auth(self):
        auth_header = self.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return False
        # Decode username:password
        encoded = auth_header.split(" ")[1]
        try:
            decoded = base64.b64decode(encoded).decode("utf-8")
            user, pw = decoded.split(":", 1)
        except Exception:
            return False
        
        return user == USERNAME and pw == PASSWORD
    
    def _require_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Transactions API"')
        self.end_headers()
        self.wfile.write(b"Unauthorized")

    def _send_json(self, status_code, data):
        if not self._check_auth():
            self._require_auth()
            return
        
        body = json.dumps(data, indent=4).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    
    def do_GET(self):
        if not self._check_auth():
            self._require_auth()
            return
        parts = self.path.strip("/").split("/")

        if self.path == "/transactions":
            self._send_json(200, transactions)
            return
        
        if len(parts) == 2 and parts[0] == "transactions":
            try:
                t_id = int(parts[1])
                tr = next((t for t in transactions if t["id"] == t_id), None)
                if tr:
                    self._send_json(200, tr)
                else:
                    self._send_json(404, {"error": "Not found"})
            except ValueError:
                self._send_json(400, {"error": "Invalid ID"})
            return
        
        self._send_json(404, {"error": "Not found"})
    
    def do_POST(self):
        if not self._check_auth():
            self._require_auth()
            return
        
        if self.path != "/transactions":
            self._send_json(404, {"error": "Not found"})
            return
        
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length).decode("utf-8")

        try:
            new_transaction = json.loads(data)
            global next_id
            new_transaction["id"] = next_id
            next_id += 1
            transactions.append(new_transaction)
            save_data()
            self._send_json(201, new_transaction)
        except Exception:
            self._send_json(400, {"error": "Invalid JSON"})
    
    def do_PUT(self):
        if not self._check_auth():
            self._require_auth()
            return
        
        parts = self.path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "transactions":
            self._send_json(404, {"error": "Not found"})
            return
        
        try:
            t_id = int(parts[1])
        except ValueError:
            self._send_json(400, {"error": "Invalid ID"})
            return
        
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length).decode("utf-8")

        try:
            updated = json.loads(data)
            tr = next((t for t in transactions if t["id"] == t_id), None)
            if tr:
                updated["id"] = t_id
                idx = transactions.index(tr)
                transactions[idx] = updated
                save_data()
                self._send_json(200, updated)
            else:
                self._send_json(404, {"error": "Not found"})
        except Exception:
            self._send_json(400, {"error": "Invalid JSON"})
    
    def do_DELETE(self):
        if not self._check_auth():
            self._require_auth()
            return
        
        parts = self.path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "transactions":
            self._send_json(404, {"error": "Not found"})
            return
        
        try:
            t_id = int(parts[1])
            tr = next((t for t in transactions if t["id"] == t_id), None)
            if tr:
                transactions.remove(tr)
                save_data()
                self._send_json(200, {"message": "Deleted"})
            else:
                self._send_json(404, {"error": "Not found"})
        except ValueError:
            self._send_json(400, {"error": "Invalid ID"})


if __name__ == "__main__":
    load_data()
    server = HTTPServer(("127.0.0.1", 8000), HTTPHandler)
    print("Server running at http://127.0.0.1:8000")
    server.serve_forever()