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

def load_dataframe(df, table_name):
    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{len(df)} registros inseridos em {table_name}")