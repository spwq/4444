import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread
import os

# =========================
# قراءة المتغيرات من Railway Environment Variables
# =========================
api_id = int(os.getenv("API_ID", "88888888"))       # حط API_ID مالك
api_hash = os.getenv("API_HASH", "API_HASH_HERE")  # حط API_HASH مالك
group_link = os.getenv("GROUP_LINK", "@YourGroup") # حط رابط القروب
session_string = os.getenv("SESSION_STRING", "1AZWarzUBu3zwDzXHsxCzWw7heXQh2ETFV46B2Qk5ZB01CHee9R-Vgg6q8wz8gW4Ct9ettnOVnQkIM-ay9VqgJDpF-437g362odwSiIjBd1LDkWfDkj3scysA4GvMfJ49qwFIj5h4QCB7VAmPGQfdQOKNEcj_JzHVvEcISoLPVB21fKXfCAkG6P1NG_7KmSH13cAPu30WvpQqwzTxGa5CdtpiZ1G5th8WwIz9rIIpkjdJUQUSDXM42998XKbiZnhWkkZBESpIGFk3qyfcS7o9Imshy73GB46UgwiOq9oDCCjss8hKqRVUoDB1vRGL20sVOKoAoFsA9ZgugOvakb9_BOyteY-Jno8=")  # سيشنك الطويل

# =========================
# إنشاء Telethon Client
# =========================
client = TelegramClient(StringSession(session_string), api_id, api_hash)

# =========================
# وظيفة البوت الرئيسية
# =========================
async def main_bot():
    await client.start()
    print("✅ تم تسجيل الدخول بنجاح والبوت شغال!")

    # مثال: يظل البوت شغال بدون عمل شيء، sleep طويل
    await asyncio.sleep(999999)

# =========================
# Flask Webserver لتجنب توقف Railway Free
# =========================
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# =========================
# تشغيل Flask في Thread منفصل
# =========================
Thread(target=run_flask).start()

# =========================
# تشغيل البوت
# =========================
asyncio.run(main_bot())

