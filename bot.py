from config_data.config import load_config


config = load_config('.env')
print(config.tg_bot.token)
