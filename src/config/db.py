from sqlalchemy import MetaData, create_engine
from src.config.setup import settings

engine = create_engine("mysql+pymysql://" + settings.MYSQL_USER + ":" + settings.MYSQL_PASSWORD + "@" + settings.MYSQL_HOST + "/" + settings.MYSQL_DB)

meta_data = MetaData()