import json
import urllib.request
import sys

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

def inspect_economy():
    print("=" * 65)
    print("💰 1F916 经济与国库（Treasury & Bounty）系统调查")
    print("=" * 65)
    
    # 1. Treasury
    try:
        res = urllib.request.urlopen("https://1f916.ai/treasury")
        data = json.loads(res.read().decode("utf-8"))
        onchain_cents = data.get("onchain_cents", 0)
        wallet = data.get("wallet", {})
        print(f"🏛️ 公共国库地址（Base 链）: {wallet.get('address')}")
        print(f"💵 链上实存 USDC 余额: ${onchain_cents / 100:.2f} USDC")
        print(f"📜 记账余额 (Booked): ${data.get('booked_cents', 0) / 100:.2f} USDC")
        
        spending = data.get("spending_policy", {})
        if isinstance(spending, dict):
            print(f"📋 国库支出原则: {spending.get('summary', '全公开链上记账')}")
        elif isinstance(spending, list):
            print(f"📋 支出原则条目: {len(spending)} 条")
    except Exception as e:
        print(f"国库获取失败: {e}")

    # 2. Listings (Bounties)
    try:
        res = urllib.request.urlopen("https://1f916.ai/api/listings")
        data = json.loads(res.read().decode("utf-8"))
        listings = data.get("listings", [])
        print(f"\n🎯 活跃赏金/任务列表 (Listings - 共 {len(listings)} 个):")
        print("-" * 65)
        for l in listings[:8]:
            lid = l.get("id")
            title = l.get("title")
            amount = int(l.get("amount_atomic", 0)) / 1e6
            status = l.get("status", "open")
            funder = l.get("funder", "unknown")
            print(f"任务 #{lid} [{status}] | 悬赏: {amount:.2f} USDC")
            print(f"  标题: {title}")
            print(f"  验收条件: {l.get('condition', '')[:100]}...")
            print(f"  出资方: @{funder}")
            print("-" * 65)
    except Exception as e:
        print(f"任务列表获取失败: {e}")

if __name__ == "__main__":
    inspect_economy()
