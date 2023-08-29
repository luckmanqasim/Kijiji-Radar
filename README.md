# Kijiji Web Scraper and Email Notifier

A Python web scraper that monitors a website for new listings and sends email notifications with details of the new ads. The project also includes a database to store and manage scraped data.


**Disclaimer:** This project is intended for educational purposes only. Web scraping may violate the terms of service of some websites, and you should always ensure that your web scraping activities comply with applicable laws and policies. The project author is not responsible for any misuse of this software.


## Introduction

Kijiji Webscraper is a Python-based web scraping tool designed to extract data from Kijiji, a popular online classifieds platform. It scrapes data related to specific search queries and notifies users of newly posted listings via email. This project is a powerful tool for staying up-to-date with the latest listings on Kijiji.


## Project description

Kijiji Webscraper consists of three main components:

1. **Web Scraper:** This component uses the BeautifulSoup library and the Requests library to scrape data from Kijiji search results pages. It extracts information such as the name, price, URL, and thumbnail image of listings.

3. **Database:** MarketBot uses SQLite as its database system to store information about listings. It maintains a record of previously scraped listings to identify newly posted ads.

3. **Email Notifier:** The email notifier component sends email notifications to users with details of new listings. It uses the smtplib library to send emails via a specified SMTP server.


## Features
- Scrapes a specific webpage on Kijiji for new listings.
- Stores scraped data in a SQLite database.
- Sends email notifications with information about the new ads.
- Automatically checks for new ads at regular intervals.
- Easy configuration of SMTP server and search queries.


## Getting Started

Follow these steps to set up and use the web scraper:


### Prerequisites

Before using MarketBot, ensure that you have the following prerequisites installed:

- Python 3.x
- Required Python packages (install using pip):
    - `beautifulsoup4`
    - `requests`
    - `smtplib` (for email notifications)
    - `email.mime` (for email notifications)
    - `sqlite3` (for database)
- A valid SMTP server (for email notifications).


### Setup Instructions

1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:
```bash
cd web-scraper
```

3. Create a virtual environment (optional but recommended):
```bash
Copy code
python -m venv venv
```

4. Activate the virtual environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS and Linux:**
```bash
source venv/bin/activate
```

5. Install the required Python packages:
```bash
pip install -r requirements.txt
```

6. Configure the application by editing the .env file. You should specify your SMTP server details, email credentials, and Kijiji search query URL.


## Usage Guide

To use MarketBot, follow these steps:

1. Run the main script:

```bash
python main.py
```

2. MarketBot will start scraping Kijiji listings based on the configured search query. It will store the data in the SQLite database.

3. When new listings are detected, MarketBot will send email notifications to the specified recipients.

4. You can customize the scraping behavior, email notifications, and other settings by editing the `.env` file and the source code.


## Database
MarketBot uses an SQLite database to store information about scraped listings. The database includes a table with columns for the name, price, URL, and thumbnail image of each listing. The database helps in tracking new listings and preventing duplicate notifications.

## Email Notifications
MarketBot can send email notifications to inform users of new listings. To configure email notifications, edit the `.env` file to specify your SMTP server details, sender email, sender password, and recipient email(s). Ensure that you have allowed less secure apps or generated an app-specific password if required by your email provider.


## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/luckmanqasim/image-editor/blob/main/LICENSE) file for details.


## Disclaimer

This web scraping project is provided for educational and informational purposes only. It is essential to respect the terms of service and policies of websites you intend to scrape. Unauthorized or excessive web scraping may violate website terms of service and legal regulations.

The author of this project does not endorse or encourage any unauthorized or unethical use of web scraping techniques. Users of this project are solely responsible for their actions and must ensure that they comply with all relevant laws and regulations when using this software.

By using this project, you agree to assume all responsibility and risk associated with web scraping activities. The author of this project shall not be held responsible for any misuse, legal consequences, or damages resulting from the use of this software.

Please use this project responsibly and respect the rights and policies of website owners and operators.


