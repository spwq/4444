from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("1AZWarzUBu3zwDzXHsxCzWw7heXQh2ETFV46B2Qk5ZB01CHee9R-Vgg6q8wz8gW4Ct9ettnOVnQkIM-ay9VqgJDpF-437g362odwSiIjBd1LDkWfDkj3scysA4GvMfJ49qwFIj5h4QCB7VAmPGQfdQOKNEcj_JzHVvEcISoLPVB21fKXfCAkG6P1NG_7KmSH13cAPu30WvpQqwzTxGa5CdtpiZ1G5th8WwIz9rIIpkjdJUQUSDXM42998XKbiZnhWkkZBESpIGFk3qyfcS7o9Imshy73GB46UgwiOq9oDCCjss8hKqRVUoDB1vRGL20sVOKoAoFsA9ZgugOvakb9_BOyteY-Jno8=")
group_link = os.getenv("GROUP_LINK")

client = TelegramClient(
    StringSession(session_string),
    api_id,
    api_hash
)

sent_ids = set()

async def main():
    await client.start()
    print("✅ تم تسجيل الدخول")

    saved = await client.get_entity("me")
    group = await client.get_entity(group_link)

    print("🚀 بدأ نقل الفيديوهات...")

    while True:
        try:
            async for msg in client.iter_messages(saved, reverse=True):
                if not msg.video:
                    continue
                if msg.id in sent_ids:
                    continue

                await client.send_file(group, msg.video, caption=msg.text or "")
                sent_ids.add(msg.id)

                await asyncio.sleep(10)

            await asyncio.sleep(30)

        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            await asyncio.sleep(15)

client.loop.run_until_complete(main())
