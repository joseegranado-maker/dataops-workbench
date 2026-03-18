from pyadomd import Pyadomd
import pandas as pd

PORT = "XXXXX"
QUERY = """
EVALUATE
TOPN(
    10,
    SUMMARIZECOLUMNS(
        'DimDate'[CalendarYear],
        "Sales", [Sales Amount]
    ),
    [Sales],
    DESC
)
"""

conn_str = f"Provider=MSOLAP;Data Source=localhost:{PORT};"

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(QUERY) as cur:
        df = pd.DataFrame(cur.fetchall(), columns=[c.name for c in cur.description])

print(df)
