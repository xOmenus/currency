import requests
import sqlite3
import os
import logging
import datetime
import time


class Currency:
    def __init__(self, currency, baseCurrency, conn):
        self.currency = currency
        self.baseCurrency = baseCurrency
        self.exchange = None
        self.conn = conn

    def getExchange(self):
        try:
            for item in self.baseCurrency:
                exchange = requests.get(
                    'https://api.exchangeratesapi.io/latest?symbols=' + self.currency + '&base=' + item
                ).json()
                self.exchange = exchange['rates'][self.currency]
                self.updateSQL(item)
        except ConnectionError:
            logging.log(40, 'Сетевая ошибка подключения к API api.exchangeratesapi.io')

    def createShema(self):
        try:
            currentCursor = self.conn.cursor()
            currentCursor.execute("CREATE TABLE exchange(updateTime timestamp, currency text, rate real)")
            self.conn.commit()
        except sqlite3.Error:
            logging.log(40, 'Не удалось создать таблицу в базе!')

    def updateSQL(self, baseCurr):
        try:
            sql_insert_custom = """INSERT INTO 'exchange' ('updateTime', 'currency', 'rate') VALUES (?,?,?)"""
            updateTime = datetime.datetime.now()
            payload = (updateTime, baseCurr, self.exchange)
            currentCursor = self.conn.cursor()
            currentCursor.execute(sql_insert_custom, payload)
            self.conn.commit()
            logging.log(20, 'Обновлена валюта: ' + baseCurr + ', курс к рублю: ' + str(self.exchange))
        except sqlite3.Error:
            logging.log(40, 'Не удалось обновить данные в таблице!')


if __name__ == '__main__':
    logging.basicConfig(filename="/dev/stdout", level=logging.INFO)
    logging.log(20, 'Server exchange started')
    try:
        connect = sqlite3.connect(os.environ['SQLDB_PATH'])
        selfCurrency = Currency(os.environ['CURRENCY'], (os.environ['BASE_CURRENCY']).replace(' ', '').split(','), connect)
        selfCurrency.createShema()
    except FileNotFoundError:
        logging.log(40, 'Не найден файл с БД sqlLite!')
    while True:
        selfCurrency.getExchange()
        time.sleep(int(os.environ["TIME_DELTA"]))
