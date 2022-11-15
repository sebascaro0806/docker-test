from sqlalchemy import MetaData, create_engine
from src.config.setup import settings


#host=base-imetrix.postgres.database.azure.com port=5432 dbname={your_database} user=admin2 password={your_password} sslmode=require
engine = create_engine("postgresql://admin2:Imetrix2022@base-imetrix.postgres.database.azure.com:5432/postgres")

meta_data = MetaData()