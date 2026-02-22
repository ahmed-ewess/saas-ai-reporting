import sqlite3
from datetime import datetime


DB_PATH = "data/saas_reports.db"


def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExecutiveReports (
            ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
            CreatedAt TEXT,
            TotalCustomers INTEGER,
            ChurnRate REAL,
            MRR REAL,
            ARPU REAL,
            RiskLevel TEXT,
            Summary TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_report(kpis: dict, summary: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ExecutiveReports (
            CreatedAt,
            TotalCustomers,
            ChurnRate,
            MRR,
            ARPU,
            RiskLevel,
            Summary
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        kpis["total_customers"],
        kpis["churn_rate"],
        kpis["monthly_recurring_revenue"],
        kpis["arpu"],
        kpis["risk_level"],
        summary
    ))

    conn.commit()
    conn.close()