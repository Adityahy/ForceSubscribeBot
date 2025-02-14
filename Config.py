import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 22821232
    API_HASH = "79ffeb00750fff0535f581d13be4e4e4
"
    BOT_TOKEN = "6668863567:AAGQFCvBTyuRWHlBk0GHqAnQdjZ4JZGUsPU"
    DATABASE_URL = "mongodb+srv://adityayad206:@cluster0.db0a2do.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "StarkBots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1744109441, 1946995626]
