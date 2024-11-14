import sqlite3


connect = sqlite3.connect('database\\database.db')
cursor = connect.cursor()


def get_widgets(page: int) -> list[tuple]:
    result = cursor.execute('''select * from widgets''').fetchall()[page * 20:(page + 1) * 20]
    return result