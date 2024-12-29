
# About bot
**FastTelegramBot** - This project is designed to quickly create your own Telegram bot by changing only a few lines of code.
## Directory tree
    Fast Telegram bot/
    ├── main.py               # Main file
    ├── config.py             # Bot configurations (token, basic settings)
    ├── handlers/             # Directorate for Processors informs
    │   ├── __init__.py       # Registration handler
    │   ├── start.py          # Handler /start
    │   ├── help.py           # Handler /help
    │   ├── general.py        # Other processors
    │   └── callback.py       # Callback processors
    ├── keyboards/            # Keyboards (inline and reply)
    │   ├── inline.py         # Inline-keyboards
    │   └── reply.py          # Reply-keyboards
    ├── middlewares/          # Middleware (additional layers of processing)
    │   ├── message_logger.py # Logging for messages
    │   └── logging           # My own logging lib (https://github.com/LeshchyshynB/logging)
    │       ├── libraries.py  # Import libraries for logging
    │       ├── logging.py    # Main logging file
    │       ├── log_writer.py # AbstractBaseClass for log
    │       └── settings.py   # Settings for logger
    ├── utils/                # Utilities (auxiliary functions)
    │   ├── database.py       # Work with the database
    │   └── misc.py           # Various auxiliary functions
    ├── data/                 # Static files, databases
    │   ├── data.db           # SQLite
    │   └──messages.json      # Localized messages
    ├── .env                  # Confidential data (token, URLs)
    ├── requirements.txt      # Dependencies of the project
    └── README.md             # Instructions for the project
## Authors

- [@MrCronix](https://github.com/LeshchyshynB)

