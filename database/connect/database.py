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


def get_title_by_id(id_widget: int) -> str:
    result = cursor.execute(f'''select title from widgets 
                            where id = ?''', (id_widget,)).fetchone()[0]
    return result


def add_widget(id_widget: int) -> None:
    cursor.execute(f'''insert into used(local_title, load, widget)
                   values (?, ?, ?)''',
                   (get_title_by_id(id_widget), 1, id_widget,))
    connect.commit()


def get_load_widgets() -> None:
    result = cursor.execute(f'''select title from widgets 
                            where load = 1''').fetchall()
    return result

def set_load_widget(local_id_widget: int) -> None:
    cursor.execute(f'''update used
                   set load = 1
                   where id = ?''',
                   (local_id_widget, ))
    connect.commit()


def set_unload_widget(local_id_widget: int) -> None:
    cursor.execute(f'''update used
                   set load = 0
                   where id = ?''',
                   (local_id_widget, ))
    connect.commit()


def remove_widget(local_id_widget: int) -> None:
    cursor.execute('''delete from used
                   where id = ?''',
                   (local_id_widget,))