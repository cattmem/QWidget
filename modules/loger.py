import datetime

log_text = []


def warn(message: str) -> None:
    log_text.append(f'[WARN | {datetime.datetime.now()}] {message}\n')


def info(message: str) -> None:
    log_text.append(f'[INFO | {datetime.datetime.now()}] {message}\n')


def to_file() -> None:
    with open(f'logs/{datetime.datetime.now().strftime("%Y.%m.%d %H.%M.%S")}.txt', 'w', encoding='utf-8') as file:
        file.writelines(log_text)
