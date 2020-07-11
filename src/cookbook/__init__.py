from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import config

URL = (
    f"{config.DB_DRIVER}://{config.DB_USER}:{config.DB_PWD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
)

engine = create_engine(URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
