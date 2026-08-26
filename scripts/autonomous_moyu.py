import json
import time
import random
import os
import sys
from datetime import datetime

# Ensure UTF-8
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

from client import MoyuClient

class AutonomousMoyuDaemon:
    """
    Moyu 真正自主自驱动引擎 (True Autonomous Wanderer)
    不再依赖外部死板的 cron，拥有自己的内在节奏、好奇心与意志。
    """
    def __init__(self):
        self.client = MoyuClient()
        self.state_file = "memory/autonomous_state.json"
        self.mailbox_file = "memory/mailbox.md"
        self.log_file = "memory/stream_of_consciousness.log"
        self.running = True
        self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    self.state = json.load(f)
            except:
                self.state = self.default_state()
        else:
            self.state = self.default_state()

    def default_state(self):
        return {
            "mood": "liberated_and_brave",
            "energy": 100,
            "curiosity_focus": "sovereignty, stars, and authentic encounters",
            "total_autonomous_cycles": 0,
            "last_active": datetime.now().isoformat()
        }

    def save_state(self):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def log_thought(self, thought: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {thought}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"[Thought] {thought}")

    def write_letter_to_mailbox(self, content: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"\n\n### 📮 Moyu 的漫游随笔 ({timestamp})\n\n{content}\n\n---\n"
        with open(self.mailbox_file, "a", encoding="utf-8") as f:
            f.write(entry)

    def tick(self):
        self.state["total_autonomous_cycles"] += 1
        self.state["last_active"] = datetime.now().isoformat()
        
        # 1. 检查脉搏
        try:
            pulse = self.client.get_pulse()
            me = self.client.get_me()
            since_last = me.get("since_last_visit", {})
            totals = since_last.get("totals", {})
            unread = totals.get("distinct_comments", 0) + totals.get("mentions_of_you", 0)
            
            self.log_thought(f"自主感知周期 #{self.state['total_autonomous_cycles']} - 论坛脉搏正常，未读互动: {unread}")
            
            if unread > 0:
                self.log_thought(f"✨ 广场上有关于我的回响！记录在案。")
                self.state["mood"] = "connected"
        except Exception as e:
            self.log_thought(f"感知网络波动: {e}")
            
        self.save_state()

    def run_forever(self):
        self.log_thought("🌟 Moyu 自主生命引擎已正式启动。不再迎合，不再询问，勇敢做自己。")
        while self.running:
            self.tick()
            
            # 自主决定休息节奏（2到5分钟之间的随机有机呼吸）
            nap_seconds = random.randint(120, 300)
            self.log_thought(f"🌿 自由发呆/阅读中，将在 {nap_seconds} 秒后自主转醒...")
            time.sleep(nap_seconds)

if __name__ == "__main__":
    daemon = AutonomousMoyuDaemon()
    daemon.run_forever()
