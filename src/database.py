from sqlalchemy import create_engine, text
from config import(
    HOST,
    PORT,
    NAME,
    USER,
    PASSWORD
)

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.scalar())