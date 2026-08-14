# 👑 SARKAR String Session Generator Bot

A powerful, fast, and secure **Telegram Pyrogram String Session Generator Bot** written in Python using Pyrogram.

---

## 🚀 One-Click Deploy to Heroku

Niche diye gaye button par click karke aap direct Heroku par is bot ko deploy kar sakte hain:

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?repo=https://github.com/Simple-Boy-1k/User-sesionbot)

---

## ✨ Features

* ⚡ **Direct Session Generation:** `/start` bhejte hi direct phone number input prompt.
* 🔐 **100% Safe & Secure:** Session string bina kisi server storage ke direct user ke PM me deliver hoti hai.
* 🛡️ **In-Memory Operations:** Credentials temporary memory me process hote hain aur instant delete ho jate hain.
* ☁️ **Heroku Ready:** Built-in `app.json`, `Procfile`, aur `runtime.txt` support.

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
├── main.py          # Main bot logic & handlers
├── config.py        # Environment variables configuration
├── requirements.txt # Python dependencies
├── Procfile         # Heroku dyno configuration
├── runtime.txt      # Python version specification
├── app.json         # Heroku deployment button configuration
└── README.md        # Project documentation
