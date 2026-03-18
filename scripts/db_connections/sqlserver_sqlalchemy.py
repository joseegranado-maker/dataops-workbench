from sqlalchemy import create_engine, text

engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/master?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT @@VERSION"))
    for row in result:
        print(row)
