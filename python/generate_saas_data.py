import random
import csv
from datetime import datetime, timedelta

random.seed(42)

N_CUSTOMERS = 2000
AS_OF_DATE = datetime(2026, 2, 22)

plans = [
    ("Basic", 19.0),
    ("Pro", 49.0),
    ("Enterprise", 199.0),
]

channels = ["Organic", "Paid Search", "Partner", "Referral", "Outbound"]
payment_statuses = ["Paid", "Overdue"]

def rand_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

rows = []
start_date = datetime(2024, 1, 1)

for cid in range(1, N_CUSTOMERS + 1):
    signup = rand_date(start_date, AS_OF_DATE - timedelta(days=7))
    plan, price = random.choices(plans, weights=[0.6, 0.3, 0.1])[0]

    # usage score: higher plans tend to have higher usage
    base_usage = {"Basic": 40, "Pro": 60, "Enterprise": 75}[plan]
    usage_score = max(0, min(100, int(random.gauss(base_usage, 15))))

    # last active: usually near as_of_date, but churned users are older
    last_active = rand_date(signup, AS_OF_DATE)
    inactivity_days = (AS_OF_DATE - last_active).days

    # churn probability increases with inactivity and low usage
    churn_prob = 0.03 + (inactivity_days / 180) * 0.5 + ((50 - usage_score) / 200)
    churn_prob = max(0.02, min(0.85, churn_prob))

    churned = 1 if random.random() < churn_prob else 0

    # if churned, force last_active older more often
    if churned and inactivity_days < 30:
        last_active = AS_OF_DATE - timedelta(days=random.randint(30, 200))
        inactivity_days = (AS_OF_DATE - last_active).days

    # overdue slightly more likely among low usage / churn
    payment_status = random.choices(
        payment_statuses,
        weights=[0.92, 0.08 + (0.1 if churned else 0.0) + (0.05 if usage_score < 40 else 0.0)]
    )[0]

    rows.append({
        "CustomerID": cid,
        "Plan": plan,
        "MonthlyPrice": price,
        "SignupDate": signup.date().isoformat(),
        "LastActiveDate": last_active.date().isoformat(),
        "UsageScore": usage_score,
        "InactivityDays": inactivity_days,
        "AcquisitionChannel": random.choice(channels),
        "PaymentStatus": payment_status,
        "Churned": churned
    })

out_path = "data/saas_subscriptions.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Created {out_path} with {len(rows)} rows")