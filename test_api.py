import urllib.request
import json
import time

def test_api():
    urls = ["http://localhost:8000/api/health", "http://localhost:8000/api/sessions"]
    for url in urls:
        print(f"Testing {url}...")
        data = {} if "sessions" in url else None
        headers = {"Content-Type": "application/json"}
        method = "POST" if data is not None else "GET"
        
        req = urllib.request.Request(
            url, 
            data=json.dumps(data).encode() if data is not None else None, 
            headers=headers, 
            method=method
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"  Status: {resp.status}")
                print(f"  Response: {resp.read().decode()[:100]}...")
        except Exception as e:
            print(f"  Error on {url}: {e}")
        time.sleep(1)

if __name__ == "__main__":
    test_api()
