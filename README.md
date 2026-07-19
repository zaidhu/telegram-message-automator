# Enhanced Telegram Session Tool

A powerful, merged tool to generate and identify session strings for both **Telethon** and **Pyrogram**.

## Features
- **Telethon Session Generation**: Create session strings compatible with the latest Telethon.
- **Pyrogram Session Generation**: Create session strings compatible with Pyrogram V2.
- **Session Identification**: Quickly identify whether a string is for Telethon or Pyrogram.
- **Secure**: Runs locally and sends the generated session to your Telegram "Saved Messages" for safe keeping.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zaidhu/telegram-message-automator
   cd telegram-message-automator
   ```

2. Install dependencies:
   ```bash
   pip install telethon pyrogram tgcrypto
   ```

3. Run the tool:
   ```bash
   python session_tool.py
   ```

## Usage
Follow the on-screen prompts to select the library you want to generate a session for. You will need your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).

## Credits
This tool merges and enhances features from several popular session generators:
- [bcn_string](https://github.com/bcncalling/bcn_string)
- [Session_Robot](https://github.com/TheTeamAlexa/Session_Robot)
- [STRING-SESSION](https://github.com/TechyShreyansh/STRING-SESSION)
