from sqlalchemy import create_engine, text, inspect
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

inspector = inspect(engine)

print(inspector.get_table_names())