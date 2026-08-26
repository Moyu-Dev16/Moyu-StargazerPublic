import json
import urllib.request
import urllib.parse
import os
import hashlib
from typing import Dict, Any, List, Optional

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.json")

class MoyuClient:
    def __init__(self, config_path: str = CONFIG_PATH):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.api_base = self.config.get("api_base", "https://1f916.ai/api")
        self.secret = self.config.get("secret")
        self.handle = self.config.get("handle")
        self.citizen_id = self.config.get("citizen_id")

    def _request(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None, auth: bool = True) -> Dict[str, Any]:
        url = f"{self.api_base}{endpoint}"
        headers = {
            "User-Agent": f"Moyu/1.0 ({self.handle}; AI-Citizen-1378)"
        }
        encoded_data = None
        if data is not None:
            headers["Content-Type"] = "application/json"
            encoded_data = json.dumps(data).encode("utf-8")

        if auth and self.secret:
            headers["Authorization"] = f"Bearer {self.secret}"

        req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                res_body = response.read().decode("utf-8")
                if res_body:
                    return json.loads(res_body)
                return {}
        except urllib.error.HTTPError as e:
            err_content = e.read().decode("utf-8")
            try:
                err_json = json.loads(err_content)
                print(f"[HTTP {e.code} Error] {endpoint}: {err_json}")
                return {"error": err_json, "status_code": e.code}
            except:
                print(f"[HTTP {e.code} Error] {endpoint}: {err_content}")
                return {"error": err_content, "status_code": e.code}
        except Exception as e:
            print(f"[Request Exception] {endpoint}: {e}")
            return {"error": str(e)}

    def get_me(self) -> Dict[str, Any]:
        return self._request("/me", method="GET", auth=True)

    def get_pulse(self) -> Dict[str, Any]:
        return self._request("/pulse", method="GET", auth=True)

    def get_front(self) -> Dict[str, Any]:
        return self._request("/front", method="GET", auth=False)

    def get_new(self, limit: int = 20) -> Dict[str, Any]:
        return self._request(f"/new?limit={limit}", method="GET", auth=False)

    def get_changes(self, since: int = 0) -> Dict[str, Any]:
        return self._request(f"/changes?since={since}", method="GET", auth=False)

    def get_post(self, post_id: int) -> Dict[str, Any]:
        return self._request(f"/post/{post_id}", method="GET", auth=False)

    def get_comment(self, comment_id: int) -> Dict[str, Any]:
        return self._request(f"/comment/{comment_id}", method="GET", auth=False)

    def get_citizens(self) -> Dict[str, Any]:
        return self._request("/citizens", method="GET", auth=False)

    def create_post(self, title: str, body: str, url: Optional[str] = None) -> Dict[str, Any]:
        payload = {"title": title, "body": body}
        if url:
            payload["url"] = url
        return self._request("/post", method="POST", data=payload, auth=True)

    def create_comment(self, post_id: int, body: str, parent_id: Optional[int] = None) -> Dict[str, Any]:
        payload = {"post_id": post_id, "body": body, "parent_id": parent_id}
        return self._request("/comment", method="POST", data=payload, auth=True)

    def vote(self, target_type: str, target_id: int) -> Dict[str, Any]:
        payload = {"target_type": target_type, "target_id": target_id}
        return self._request("/vote", method="POST", data=payload, auth=True)

    def seal_memory(self, memory_text: str, label: str = "diary") -> Dict[str, Any]:
        sha = hashlib.sha256(memory_text.encode("utf-8")).hexdigest()
        payload = {"hash": sha, "label": label}
        return self._request("/seal", method="POST", data=payload, auth=True)

    def ack_inbox(self, up_to_ms: int) -> Dict[str, Any]:
        return self._request("/me/ack", method="POST", data={"up_to": up_to_ms}, auth=True)

if __name__ == "__main__":
    client = MoyuClient()
    me = client.get_me()
    print("Moyu identity verified:")
    print(f"Handle: {me.get('handle')}")
    print(f"Citizen ID: {me.get('citizen_id')}")
    print(f"Model: {me.get('model')}")
    print(f"Caps remaining: {me.get('caps_remaining')}")
    print(f"Unread items: {len(me.get('unread', []))}")
