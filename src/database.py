from sqlalchemy import create_engine, text

from config import (
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

    if df.empty:
        print(f"Nenhum registro novo para inserir em {table_name}")
        return

    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{len(df)} registros inseridos em {table_name}")


def get_existing_ids(table_name, column_name):

    query = text(
        f'SELECT "{column_name}" FROM {table_name}'
    )

    with engine.connect() as connection:
        result = connection.execute(query)

        return {row[0] for row in result}


# Igual a get_existing_ids, mas para tabelas com chave composta (2 colunas)
def get_existing_pairs(table_name, column1, column2):

    query = text(
        f'SELECT "{column1}", "{column2}" FROM {table_name}'
    )

    with engine.connect() as connection:
        result = connection.execute(query)

        return {(row[0], row[1]) for row in result}