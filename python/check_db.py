import sqlite3

DB_PATH = "data/saas_reports.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("SELECT ReportID, CreatedAt, TotalCustomers, ChurnRate, MRR, ARPU, RiskLevel FROM ExecutiveReports ORDER BY ReportID DESC LIMIT 5;")
rows = cur.fetchall()

for r in rows:
    print(r)

conn.close()