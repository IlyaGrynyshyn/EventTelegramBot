# Event telegram bot

"Event Bot" is Telegram bot designed for convenient registration for events, 
accepting payments for tickets, and providing detailed information about event.

## Features

- Event Registration
- Ticket Payment Handling
- Detailed Event Information
- Updates and Notifications

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IlyaGrynyshyn/event_telegram_bot.git

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Create the configuration file `.env` and add next parameters:
   ```bash
    BOT_TOKEN = 'your_telegram_bot_token'
    ADMINS = "your_telegram_id"
    PROVIDER_TOKEN = "your_payment_provider_token"

4. Run the bot:
    ```bash
     python app.py

## Bot Commands
    
   `/start` - Start using the bot.
   
## Contribution
If you have ideas or would like to contribute to the project, please fork the repository and create a pull request.
Thank you for your interest in the "event_telegram_bot" project!