import sqlite3


class Database:
    
    def __init__(self, db_name='cache_data.db'):
        # establish connection with the database to fetch and save data
        self.db_name = db_name

    
    # special method to open and establish connection using "with" statement
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self


    # special method to close the connection with database after the "with" statement and to handle any exceptions
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:
            # An exception occurred within the 'with' block, handle it here
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Exception traceback: {traceback}")

        if self.connection:
            self.connection.close()


    # check if the table already exists
    def table_exists(self, table):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        result = self.cursor.fetchone()

        # return None if the table does not exist
        return result


    # create a table to save the ad listing data for your query, with 4 columns name, price, url and thumbnail
    def create_table(self, table):

        create_query = f'''
            CREATE TABLE IF NOT EXISTS {table} (
                Name TEXT,
                Price TEXT,
                URL TEXT,
                Thumbnail TEXT
            )
        '''
        self.cursor.execute(create_query)
        self.connection.commit()


    # clear all the data from a table
    def _clear_table(self, table):

        clear_query = f'DELETE from {table}'
        self.cursor.execute(clear_query)

        # commit the changes made to the database
        self.connection.commit()


    # clear and update the table with all the ad listings
    def _insert_data(self, table, data):
        self._clear_table(table)

        # for each lisiting in all the listings, add them into the table
        insert_query = f'''
            INSERT INTO {table} (Name, Price, URL, Thumbnail)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.executemany(insert_query, data)
        self.connection.commit()


    # fetch a record from the database using the url if it exists, returns None if it doesnt exist
    def _fetch_data(self, table, record):

        # ADD A PLACEHOLDER FOR URL
        query = f'SELECT * FROM {table} WHERE URL = ?'
        url = record[2]
        self.cursor.execute(query, (url,))

        result = self.cursor.fetchone()
        return result
    

    # takes all the scraped data as a list, compares it to the database and returns the new data
    def _fresh_data(self, table, data):
        fresh_data = []

        # check if the records/listings already exist in the table
        for item in data:

            check = self._fetch_data(table, item)
            if not check:
                fresh_data.append(item)

        return fresh_data
    

    # update the table with ads and return the new ads
    def update_and_return_new(self, table, data):
        new_data = self._fresh_data(table, data)
        self._insert_data(table, data)
        
        return new_data