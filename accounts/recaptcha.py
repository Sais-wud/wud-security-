
import os, requests

def verify_recaptcha(token: str) -> bool:
    """Server‑side check for Google reCAPTCHA v3 (score >= 0.5)."""
    secret = os.getenv("RECAPTCHA_SERVER_KEY", "")
    resp = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": secret, "response": token},
        timeout=3,
    )
    data = resp.json()
    return data.get("success") and data.get("score", 0) >= 0.5
