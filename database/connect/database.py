import sqlite3


connect = sqlite3.connect('database\\database.db')
cursor = connect.cursor()


def get_widgets(page: int, title: str | None = '') -> list[tuple]:
    result = cursor.execute(f'''select * from widgets
                            where title like "%{title}%"''').fetchall()[page * 20:(page + 1) * 20]
    return result

def get_max_pages(title: str | None = '') -> int:
    result = len(cursor.execute(f'''select id from widgets
                                where title like "%{title}%"''').fetchall()) // 20
    return result