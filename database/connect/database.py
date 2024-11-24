import sqlite3

connect = sqlite3.connect('database/database.db')
cursor = connect.cursor()


def get_widgets(page: int, title: str | None = '') -> list[tuple]:
    result = cursor.execute(f'''select * from widgets
                            where title like "%{title}%"
                            order by star, title, id''').fetchall()[page * 20:(page + 1) * 20]
    return result[::-1]


def get_max_pages(title: str | None = '') -> int:
    result = len(cursor.execute(f'''select id from widgets
                                where title like "%{title}%"''').fetchall()) // 20
    return result


def get_title_by_id(id_widget: int) -> str:
    result = cursor.execute(f'''select title from widgets
                            where id = ?''', (id_widget,)).fetchone()[0]
    return result


def remove_widget(id_widget: int) -> None:
    cursor.execute('''delete from widgets
                   where id = ?''', (id_widget, ))

    connect.commit()


def get_star(id_widget: int) -> int:
    result = cursor.execute('''select star from widgets
                            where id = ?''', (id_widget,)).fetchone()[0]

    return result


def change_star(id_widget: int) -> int:
    cursor.execute(f'''update widgets
                   set star = ?
                   where id = ?''',
                   (0 if get_star(id_widget) else 1, id_widget))

    connect.commit()


def new_widget(name: str) -> int:
    cursor.execute(f'''insert into widgets(title,type)
                   values(?, 1)''', (name, ))
    connect.commit()

    result = cursor.execute('''select id from widgets
                            order by id''').fetchall()[-1][0]
    return result


def get_types() -> None:
    result = cursor.execute('''select id, title from types''').fetchall()
    return dict(result)
