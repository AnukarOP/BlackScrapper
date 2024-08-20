
# Telegram CC Scraper Bot 🚀

This Telegram bot is designed to scrape messages from different groups or channels and extract credit card information. The extracted data is then sent to a specified channel of your choice. This bot is intended for educational purposes only and should not be used for any illegal activities.

## Features

- Scrapes messages from specified Telegram groups or channels.
- Filters out credit card information using regular expressions.
- Performs BIN lookup to retrieve information about the credit card.
- Sends the formatted credit card information to a specified Telegram channel.
- Adds random delays to simulate more human-like behavior.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/AnukarOP/BlackScrapper
cd BlackScrapper
```

2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. Replace the placeholder values in `main.py` with your actual Telegram API credentials:

```python
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'
```

## Usage

1. Start the bot:

```bash
python3 main.py
```

2. The bot will automatically start scraping messages from the configured groups or channels and send the extracted information to your specified channel 24/7.

## Disclaimer

This bot is meant for educational purposes only. The use of this bot for illegal activities such as unauthorized access to information or credit card fraud is strictly prohibited. The authors do not take any responsibility for any misuse of this bot.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

<p align="center">
  <a href="https://github.com/AnukarOP" target="_blank">
    <img src="https://img.shields.io/badge/Made%20with%20%E2%9D%A4%20by-AnukarOP-%23FF0000.svg" alt="Made with love by AnukarOP"/>
  </a>
</p>
