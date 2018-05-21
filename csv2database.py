import os, csv, pandas
from sqlalchemy import Table, Column, String, Integer, Boolean

import sqlalchemy
from sqlalchemy import Table, Column


def main_method(csv_filepath, user, passwoed, db):
    df = pandas.read_csv(csv_filepath)
    conn = connect(user, passwoed, db)
    df.to_sql('pokemon', conn[0])
    # pass


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


def main():
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    csv_filepath = os.path.join(ROOT_DIR, "raw_data", 'pokemon.csv')
    user = 'npiedy'
    password = 'root'
    db = 'pokemon'
    main_method(csv_filepath, user, password, db)
    pass

if __name__ == '__main__':
    main()
    pass