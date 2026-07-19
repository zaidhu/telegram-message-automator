import asyncio
import os
from pyrogram import Client as PyroClient
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import (
    SessionPasswordNeededError as TelethonPasswordNeeded,
    PhoneCodeInvalidError as TelethonCodeInvalid,
    PhoneCodeExpiredError as TelethonCodeExpired
)
from pyrogram.errors import (
    SessionPasswordNeeded as PyroPasswordNeeded,
    PhoneCodeInvalid as PyroCodeInvalid,
    PhoneCodeExpired as PyroCodeExpired
)

# Default API Credentials (Users can override via env or input)
DEFAULT_API_ID = 14688437
DEFAULT_API_HASH = "5310285db722d1dceb128b88772d53a6"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def generate_telethon_session(api_id, api_hash):
    print("\n--- Telethon Session Generation ---")
    phone = input("Enter your phone number (with country code): ")
    client = TelegramClient(StringSession(), api_id, api_hash)
    await client.connect()
    
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input("Enter the code you received: ")
        try:
            await client.sign_in(phone, code)
        except TelethonPasswordNeeded:
            password = input("Two-step verification enabled. Enter your password: ")
            await client.sign_in(password=password)
    
    session_str = client.session.save()
    print(f"\nYour Telethon String Session:\n{session_str}\n")
    await client.send_message("me", f"**Your Telethon String Session:**\n\n`{session_str}`")
    await client.disconnect()
    return session_str

async def generate_pyrogram_session(api_id, api_hash):
    print("\n--- Pyrogram (V2) Session Generation ---")
    phone = input("Enter your phone number (with country code): ")
    client = PyroClient(":memory:", api_id=api_id, api_hash=api_hash)
    await client.start()
    
    # Pyrogram start() handles the login flow interactively in the terminal
    session_str = await client.export_session_string()
    print(f"\nYour Pyrogram String Session:\n{session_str}\n")
    await client.send_message("me", f"**Your Pyrogram String Session:**\n\n`{session_str}`")
    await client.stop()
    return session_str

def read_session_info():
    print("\n--- Session Reader ---")
    session_str = input("Paste your session string: ")
    
    if session_str.startswith("1"):
        print("Detected: Telethon Session String")
        # In a real scenario, we'd connect to verify, but for now we identify
    else:
        print("Detected: Pyrogram Session String")
    
    print("Feature coming soon: Full session metadata extraction.")

async def main():
    while True:
        clear_screen()
        print("========================================")
        print("   Enhanced Telegram Session Tool")
        print("========================================")
        print("1. Generate Telethon Session")
        print("2. Generate Pyrogram Session")
        print("3. Read/Identify Session String")
        print("4. Exit")
        choice = input("\nSelect an option (1-4): ")

        api_id = int(os.getenv("API_ID", DEFAULT_API_ID))
        api_hash = os.getenv("API_HASH", DEFAULT_API_HASH)

        if choice == '1':
            await generate_telethon_session(api_id, api_hash)
        elif choice == '2':
            await generate_pyrogram_session(api_id, api_hash)
        elif choice == '3':
            read_session_info()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    asyncio.run(main())
