import pandas as pd
from datetime import datetime

AS_OF_DATE = datetime(2026, 2, 22)

def calculate_kpis(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)

    total_customers = len(df)
    churned_customers = df["Churned"].sum()
    churn_rate = churned_customers / total_customers

    mrr = (df["MonthlyPrice"] * (1 - df["Churned"])).sum()
    arpu = df["MonthlyPrice"].mean()

    avg_usage = df["UsageScore"].mean()

    overdue_rate = (df["PaymentStatus"] == "Overdue").mean()

    risk_level = "HIGH" if churn_rate > 0.5 else "MEDIUM" if churn_rate > 0.3 else "LOW"

    return {
        "total_customers": total_customers,
        "churned_customers": int(churned_customers),
        "churn_rate": round(churn_rate, 4),
        "monthly_recurring_revenue": round(mrr, 2),
        "arpu": round(arpu, 2),
        "average_usage_score": round(avg_usage, 2),
        "overdue_rate": round(overdue_rate, 4),
        "risk_level": risk_level
    }


if __name__ == "__main__":
    kpis = calculate_kpis("data/saas_subscriptions.csv")
    print(kpis)