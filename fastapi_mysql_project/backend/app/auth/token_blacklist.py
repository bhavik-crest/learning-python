# app/auth/token_blacklist.py

token_blacklist = set()  # Simple in-memory blacklist; use Redis for production

def add_token_to_blacklist(token: str):
    token_blacklist.add(token)

def is_token_blacklisted(token: str) -> bool:
    return token in token_blacklist
