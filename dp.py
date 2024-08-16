import sqlite3

conection = sqlite3.connect('database.dp')
cursor = conection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products
(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INT
)
''')
products = []


def get_all_products(id_prod, title_prod, description_prod, price_prod):
    check_prod = cursor.execute("SELECT * FROM Products WHERE id=?", (id_prod, ))
    if check_prod.fetchone()[0] is None:
        for i in range(4):
            product = cursor.execute(f"INSERT INTO Products VALUES('{id_prod}', '{title_prod}', '{description_prod}', '{price_prod}')")
            products.append(product)
        return products


conection.commit()
conection.close()