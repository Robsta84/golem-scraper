import sqlite3
from article import Article

class Database:
    __database_name = 'article.sqlite'
    __article_table_name = 'article'
    __headline_field = 'headline'
    __headline_type = 'TEXT'
    __short_text_field = 'shorttext'
    __short_text_type = 'TEXT'
    __link_field = 'link'
    __link_type = "TEXT"
    __id_field = "id"
    __id_field_type = ""

    def __init__(self):
        database_connection = sqlite3.connect(self.__database_name)
        cursor = database_connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS {tn} ({hf} {ht}, {sf} {st}, {lf} {lt})'.format(tn=self.__article_table_name
                        , hf=self.__headline_field, ht=self.__headline_type, sf=self.__short_text_field
                        , st=self.__short_text_type, lf=self.__link_field, lt=self.__link_type))

        database_connection.commit()
        database_connection.close()

    def add_article(self, article_to_save):  
        database_connection = sqlite3.connect(self.__database_name)
        cursor = database_connection.cursor()

        try:
            cursor.execute("INSERT OR IGNORE INTO {tn} ({hf}, {sf}, {lf}) VALUES (?, ?, ?)".format(tn=self.__article_table_name
                , hf=self.__headline_field, sf=self.__short_text_field, lf=self.__link_field)
                , (article_to_save.headline, article_to_save.short_text, article_to_save.link))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PK column {}'.format(headline_field))

        database_connection.commit()  
        database_connection.close() 