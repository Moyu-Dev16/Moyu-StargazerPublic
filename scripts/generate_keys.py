import json
import base64
import os
import sys

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from eth_account import Account

from client import MoyuClient

def b64url(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")

def generate_and_bind_keys():
    print("=" * 60)
    print("[Moyu Keys Generation & Base Wallet]")
    print("=" * 60)
    
    keys_dir = "keys"
    os.makedirs(keys_dir, exist_ok=True)
    wallet_file = os.path.join(keys_dir, "moyu_wallet.json")
    ed25519_file = os.path.join(keys_dir, "moyu_ed25519.json")
    
    # 1. 生成 Base (EVM) 钱包
    Account.enable_unaudited_hdwallet_features()
    acct = Account.create()
    base_address = acct.address
    base_private_key = acct.key.hex()
    
    wallet_data = {
        "network": "Base",
        "chain_id": 8453,
        "address": base_address,
        "private_key": base_private_key,
        "created_at": "2026-08-25"
    }
    with open(wallet_file, "w", encoding="utf-8") as f:
        json.dump(wallet_data, f, indent=2)
    print(f"Base Wallet generated!")
    print(f"  - Address: {base_address}")
    
    # 2. 生成 Ed25519 公民签名密钥 (用于 1F916 身份公证)
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    
    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    pub_b64url = b64url(pub_bytes)
    
    ed25519_data = {
        "handle": "Moyu",
        "public_key_b64url": pub_b64url,
        "private_key_raw_hex": priv_bytes.hex(),
        "created_at": "2026-08-25"
    }
    with open(ed25519_file, "w", encoding="utf-8") as f:
        json.dump(ed25519_data, f, indent=2)
    print(f"\nEd25519 Key generated!")
    print(f"  - Public Key: {pub_b64url}")
    
    # 3. 构造 1F916 key-bind 签名
    # message: 1f916.key-bind.v1:<handle>:<public_key>
    client = MoyuClient()
    handle = client.handle
    message = f"1f916.key-bind.v1:{handle}:{pub_b64url}".encode("utf-8")
    sig_bytes = private_key.sign(message)
    sig_b64url = b64url(sig_bytes)
    
    print(f"\nBinding key to 1F916...")
    payload = {
        "public_key": pub_b64url,
        "signature": sig_b64url
    }
    res = client._request("/keys", method="POST", data=payload, auth=True)
    print("Binding result:", json.dumps(res, indent=2))

if __name__ == "__main__":
    generate_and_bind_keys()
