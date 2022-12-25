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
    API_ID = 16246834
    API_HASH = "29b3ffa9245c07f05375b92f38e8f13d"
    BOT_TOKEN = "5894485189:AAHKL7pEKVdVWa9OEaBlJ-wqb27xB251rl8"
    DATABASE_URL = "postgres://lbppnpzg:anX6J9dllmK1q0R9hGHUykgqGcTJfw_4@rosie.db.elephantsql.com/lbppnpzg"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "nakama_asl"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
