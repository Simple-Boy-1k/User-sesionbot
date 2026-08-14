# 👑 SARKAR String Session Generator Bot

A powerful, fast, and secure **Telegram Pyrogram String Session Generator Bot** written in Python using Pyrogram.

---

## 🚀 Deploy to Heroku

Niche diye gaye button par click karke aap direct Heroku par is bot ko deploy kar sakte hain:

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/Simple-Boy-1k/User-sesionbot)

---

## 🛠️ Required Environment Variables

Heroku / VPS par deploy karte waqt ye variables set karein:

| Variable | Description | Source |
| :--- | :--- | :--- |
| `API_ID` | Your Telegram API ID | [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Your Telegram API Hash | [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Your Telegram Bot Token | [@BotFather](https://t.me/BotFather) |

---

## 📁 Repository Structure

```text
├── main.py          # Main bot logic
├── config.py        # Environment variables configuration
├── requirements.txt # Python dependencies
├── Procfile         # Heroku worker process
├── runtime.txt      # Python version specification
├── app.json         # Heroku deployment configuration
└── README.md        # Documentation
