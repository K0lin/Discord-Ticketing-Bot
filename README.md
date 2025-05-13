# Discord Ticket Management Bot

A professional, feature-rich Discord bot for managing support tickets, built with Python.

![Discord Ticket Bot](https://img.shields.io/badge/Discord-Ticket%20Bot-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

## 📋 Overview

This Discord Ticket Management Bot provides a robust solution for handling support inquiries within Discord servers. It enables users to create categorized tickets, which are then managed through a comprehensive system that logs all interactions and provides administrators with powerful control options.

## ✨ Features

- **Advanced Ticket System**: Create, manage, and close support tickets seamlessly
- **Ticket Categorization**: Support for multiple ticket types with customizable categories (e.g., "Support")
- **Complete Customization**: Fully configurable messages, colors, titles, and descriptions
- **Comprehensive Logging**: Message logging and downloadable ticket transcripts
- **Role-based Access Control**: Define which roles can close tickets
- **Integrated Database**: Persistent storage of ticket data and interactions
- **Custom Timezone Support**: Timestamp logs according to your preferred timezone
- **Embeds & Interactive Components**: Professional-looking interfaces with embedded messages and interactive buttons

## 📋 Requirements

- Python 3.8 or higher
- Discord Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications)
- Appropriate Discord server permissions (Administrator recommended)
- Internet connection for API interactions

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/discord-ticket-bot.git
cd discord-ticket-bot
```

2. Set up a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the configuration template:
```bash
cp config.example.json config.json
```

5. Configure the bot (see [Configuration](#configuration) section)

6. Run the bot:
```bash
python main.py
```

## ⚙️ Configuration

Edit the `config.json` file with your specific settings:

```json
{
  "BOT_TOKEN": "",               // Your Discord bot token
  "BOT_STATUS": "",              // Custom status for the bot
  "ENABLE_CONSOLE_LOG": true,    // Enable logging in the console for debugging and informational messages
  "LANGUAGE": "en",             // Defines the bot's language using a standard ISO 639-1 code (e.g., "en" for English, "fa" for Persian, "es" for Spanish).
  "TIMEZONE": "",                // Your preferred timezone (e.g., "Europe/London")
  "REFRESH_CREATION_MESSAGE": true,  // Whether to refresh the ticket creation message on startup
  "MESSAGES_LOG": true,          // Enable message logging in tickets
  "DOWNLOAD_LOG": true,          // Enable downloadable ticket transcripts
  "DATABASE_LOCATION": "",      // Name of the database directory
  "DATABASE_NAME": "",           // Name of the database file
  "TICKET_CREATION_CHANNEL_ID": 0,  // Channel ID where users can create tickets
  "TICKET_CREATION_EMBED_COLOR": "", // Color for the ticket creation embed (HEX) (e.g., 0xffffff)
  "TICKET_CREATION_AUTHOR": "",      // Author field for the ticket creation embed
  "TICKET_CREATION_TITLE": "",       // Title for the ticket creation embed
  "TICKET_CREATION_DESCRIPTION": "", // Description for the ticket creation embed
  "TICKET_CHOICE_BUTTON": [          // Available ticket categories
    {
      "Name": "Style"            // Example category  (style accepted: Primary, Secondary, Success, Danger)
    }
  ],
  "TICKET_CATEGORY_ID": 0,       // Discord category ID for organizing ticket channels
  "TICKET_CLOSURE_EMBED_COLOR": "",  // Color for the ticket closure embed
  "TICKET_CLOSURE_AUTHOR": "",       // Author field for the ticket closure embed
  "TICKET_CLOSURE_TITLE": "",        // Title for the ticket closure embed
  "TICKET_CLOSURE_DESCRIPTION": "",  // Description for the ticket closure embed
  "TICKET_LOG_CHANNEL_ID": 0,        // Channel ID for ticket logs/transcripts
  "TICKET_ENABLE_CLOSING_ROLE_ID": [] // Role IDs that can close tickets (e.g., [1111, 2222])
}
```

## 🔍 Usage

1. **Setting Up**: After configuration, invite the bot to your server with the proper permissions.

2. **Ticket Creation**: The bot will post a message with interactive buttons in the designated channel. Users click these buttons to create tickets based on their needs.

3. **Ticket Permission**: The ticket will be created within a category, which **must be empty and accessible only to staff**, each ticket will assume the permissions of the category plus add private permissions only to the user creating the ticket.

4. **Ticket Management**: 
   - Staff with appropriate roles can interact with tickets
   - Close tickets when resolved
   - Access ticket transcripts and logs

## 📁 Project Structure

```
ticketing/
├── main.py            # Main entry point and bot initialization
├── config.json        # Configuration file with bot settings
├── requirements.txt   # Python dependencies
├── database.db        # SQLite database file for ticket storage
├── utils/             # Utility functions
│   ├── __pycache__    # Python cache directory
│   ├── config_manager.py  # Configuration loading and management
│   ├── paths_manager.py   # Absolute paths to working directory management
│   ├── database.py        # Database interaction and models
│   ├── connectionPool.py  # Database connection pool for use of threads
│   └── embed.py       # Discord embed generators for tickets
├── view/              # Discord UI components
│   ├── __pycache__    # Python cache directory
│   ├── ticketClosure.py    # Ticket closure button and logic
│   ├── ticketCreation.py   # Ticket creation interface
│   └── ticketMessageLog.py # Message logging functionality
└── lang/        # Folder with configuration files for languages inside
    └── en.json  # English language configuration file
```

## 📦 Dependencies

### External Libraries
- [discord.py](https://discordpy.readthedocs.io/) - Discord API wrapper for bot functionality, including UI components and command extensions
- [pytz](https://pypi.org/project/pytz/) - Timezone calculations for accurate logging and timestamps

### Python Standard Library
- [os](https://docs.python.org/3/library/os.html) - Operating system interfaces
- [pathlib](https://docs.python.org/3/library/pathlib.html) - Object-oriented filesystem paths
- [json](https://docs.python.org/3/library/json.html) - JSON processing for configuration
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - Lightweight database
- [datetime](https://docs.python.org/3/library/datetime.html) - Date and time handling
- [io](https://docs.python.org/3/library/io.html) - Core I/O functionality
- [threading](https://docs.python.org/3/library/threading.html) - Thread management
- [queue](https://docs.python.org/3/library/queue.html) - Queue management for database with threads


To install all external dependencies:
```bash
pip install discord.py pytz
```

Alternatively, you can use the provided requirements.txt file:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Visit our [contributing guidelines](CONTRIBUTING.md)

## 📄 License

This project is licensed under a Custom Restricted License - see the [LICENSE.md](LICENSE.md) file for details.

**Key Restrictions:**
- No distribution or redistribution allowed
- No sublicensing permitted
- No usage for illegal activities or purposes
- No commercial use without explicit permission

For permission requests or questions about licensing, please contact me into an issue.

⚠️ **Note:** Using this software for illegal purposes or in violation of Discord's Terms of Service is strictly prohibited.

---

## 📞 Support

If you encounter any issues or have questions, please open an [issue](https://github.com/K0lin/Discord-Ticketing-Bot/issues) on GitHub or contact the maintainer.

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)
