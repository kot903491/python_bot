from dataclasses import dataclass
from environs import Env


@dataclass()
class DatabaseConfig:
    db_name: str  # Название базы данных
    db_host: str  # Хост
    db_user: str  # Имя пользователя базы данных
    db_password: str  # Пароль базы данных


@dataclass()
class TgBot:
    token: str  # Токен к боту
    admin_ids: list[int]  # Список админов бота


@dataclass()
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  db=DatabaseConfig(db_name=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))
