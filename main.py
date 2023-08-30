from web_scraper import WebScraper
from database import Database
from email_message import Message
from dotenv import load_dotenv
import os


def main():

    # load environment variables from .env file
    load_dotenv()

    # access environmental variables
    search_url = os.getenv('SEARCH_URL')
    table_name = os.getenv('TABLE_NAME')
    smtp_server = os.getenv('SMTP_SERVER')
    port = os.getenv('PORT')
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD') 
    receiver_email = os.getenv('RECEIVER_EMAIL')


    # intialize the webscraper and extract data
    scraper = WebScraper(search_url)
    all_data = scraper.scrape_all_pages()


    # use a with statement to connect with the database
    with Database() as db:
        if not db.table_exists(table_name):
            db.create_table(table_name)

        new_data = db.update_and_return_new(table_name, all_data)


    # send an email notification
    email_config = {
        'smtp_server': smtp_server,
        'port': port,
        'sender_email': sender_email,
        'sender_password': sender_password,
    }


    # intialize the email client
    message = Message(**email_config)

    if message.send_email(receiver_email, new_data):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")


if __name__ == "__main__":
    main()