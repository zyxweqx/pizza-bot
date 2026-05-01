# Pizza Delivery Bot

Asynchronous Telegram bot for pizza ordering, developed using the aiogram 3 framework and SQLAlchemy 2.0.

---

## Features

### User Interface
* **Dynamic Menu**: Categorized product catalog with a multi-level navigation system.
* **Integrated Pagination**: Navigation through product lists using asynchronous inline buttons.
* **Cart Management**: Full cycle of order preparation, including adding, removing, and updating item quantities.
* **Visual Interface**: Thematic banners for each menu section retrieved from the database.

### Administrative Interface
* **Inventory Management**: Real-time Create, Read, Update, and Delete (CRUD) operations for products.
* **Content Management**: Tools for updating system banners and section descriptions.

---

## Tech Stack

| Component          | Technology                           |
| :----------------- | :----------------------------------- |
| **Language**       | Python 3.10+                         |
| **Bot Framework**  | aiogram 3.x (Asynchronous)           |
| **ORM**            | SQLAlchemy 2.0                       |
| **Database**       | SQLite via aiosqlite                |
| **Image Handling** | Pillow                               |

---

## Project Structure
```text
pizza-bot/
├── app.py              # Application entry point and polling configuration
├── database/           # Data persistence layer (models and ORM logic)
├── handlers/           # Request processors for user and admin events
├── kbds/               # Keyboard builders (Inline and Reply)
├── middlewares/        # Middlewares for session and data injection
├── utils/              # Utility classes and pagination logic
├── common/             # Static configurations and word filters
└── banners/            # Static assets for the menu interface

Installation and Setup
Clone the repository:


git clone [https://github.com/zyxweqx/pizza-bot.git](https://github.com/zyxweqx/pizza-bot.git)
cd pizza-bot

Install required packages:
pip install -r requirements.txt


Configure Environment:
Create a .env file in the project root and add your credentials:

TOKEN=your_telegram_bot_token
DB_URL=sqlite+aiosqlite:///db.sqlite3

Initialize and Launch:
python app.py