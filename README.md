
# 🚀 Linux System Monitor Bot

A lightweight **Python** watchdog service running on **Linux (WSL)** that monitors system health and sends real-time alerts to **Telegram**.

## 🛠️ Tech Stack
* **Language:** Python 3
* **OS:** Linux (Ubuntu via WSL 2)
* **Libraries:** `psutil` (Hardware monitoring), `requests` (API communication)
* **API:** Telegram Bot API

## ✨ Key Features
* **Real-time Monitoring:** Continuously tracks CPU and RAM utilization.
* **Automated Alerts:** Instantly notifies the user via Telegram when thresholds (e.g., 80%) are exceeded.
* **Secure Architecture:** Implements environment variables (`.env`) to protect sensitive API credentials.

## 🚀 Getting Started
1. **Clone the repo:** `git clone https://github.com/YOUR_USERNAME/system-monitor-bot.git`
2. **Install dependencies:** `pip install psutil requests python-dotenv`
3. **Configure Secrets:** Create a `.env` file with your `TELEGRAM_TOKEN` and `CHAT_ID`.
4. **Run:** `python3 monitor.py`

## 📊 ECE Context
This project demonstrates the ability to bridge **software automation** with **system-level hardware metrics**, a core skill for Embedded Systems and IoT roles.
