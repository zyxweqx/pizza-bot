# Pizza Delivery Bot

Asynchronous Telegram bot for pizza ordering, developed using the aiogram 3 framework and SQLAlchemy 2.0.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/aiogram-3.x-2CA5E0.svg?style=flat&logo=telegram&logoColor=white" alt="aiogram">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-red.svg" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white" alt="Docker">
</p>

## 📸 Demo

<div align="center">
  <img src="https://github.com/user-attachments/assets/e0e80038-c85e-4cff-b484-507098772785" alt="Main Menu" width="180">
  &nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/e523b485-d4f2-4574-a617-c197d0dd928b" alt="Pizza Catalog" width="180">
  &nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/b0c39c55-57ee-4f83-aa7f-a7ed2f5e007d" alt="Drinks Catalog" width="180">
  &nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/68f826f9-6e55-4601-826d-022e596fd9d5" alt="Cart Management" width="180">
</div>

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

| Component            | Technology                           |
| :------------------- | :----------------------------------- |
| **Language**         | Python 3.10+                         |
| **Bot Framework**    | aiogram 3.x (Asynchronous)           |
| **ORM**              | SQLAlchemy 2.0                       |
| **Database**         | SQLite via aiosqlite                 |
| **Containerization** | Docker & Docker Compose              |
| **Image Handling**   | Pillow                               |

---


## Project Structure
```text
pizza-bot/
├── banners/            # Static assets for the menu interface
├── common/             # Static configurations and word filters
├── database/           # Data persistence layer (models and ORM logic)
├── filters/            # Custom aiogram filters (e.g., IsAdmin)
├── handlers/           # Request processors for user and admin events
├── kbds/               # Keyboard builders (Inline and Reply)
├── middlewares/        # Middlewares for session and data injection
├── utils/              # Utility classes and pagination logic
├── .dockerignore       # Files excluded from Docker build context
├── .gitignore          # Files excluded from Git tracking
├── app.py              # Application entry point and polling configuration
├── docker-compose.yml  # Container orchestration settings
├── Dockerfile          # Docker image configuration
└── requirements.txt    # Python dependencies
```
## Installation and Setup

### Option 1: Running via Docker (Recommended)
The easiest way to get the bot running is using Docker. It handles all dependencies automatically.

1. **Clone the repository:**  
   ```
   git clone https://github.com/zyxweqx/pizza-bot.git
   cd pizza-bot
   ```
2. **Configure Environment:**   
Create a .env file in the root directory and add your credentials: 
    ```
    TOKEN=your_telegram_bot_token
    ```
3. **Launch:**
Run the following command in your terminal:
    ```
    docker-compose up -d --build
    ```
### Option 2: Manual Installation
Use this method if you prefer running the bot directly on your host machine without Docker.

1. **Clone and install dependencies:**
    ```
    git clone https://github.com/zyxweqx/pizza-bot.git 
    cd pizza-bot
    pip install -r requirements.txt
    ```
2. **Configure Environment:**  
Create a .env file in the root directory:
    ```
    TOKEN=your_telegram_bot_token
    DB_URL=sqlite+aiosqlite:///db.sqlite3
    ```
3. **Initialize and Launch:**
    ```
    python app.py
    ```