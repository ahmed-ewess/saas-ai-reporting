from datetime import datetime
from typing import Dict


def generate_executive_summary(kpis: Dict) -> str:
    """
    Generates an executive-style summary from KPI values (no external AI yet).
    Later we can replace this with a real LLM call.
    """
    total = kpis["total_customers"]
    churn_rate = kpis["churn_rate"]
    churned = kpis["churned_customers"]
    mrr = kpis["monthly_recurring_revenue"]
    arpu = kpis["arpu"]
    avg_usage = kpis["average_usage_score"]
    overdue_rate = kpis["overdue_rate"]
    risk = kpis["risk_level"]

    churn_pct = churn_rate * 100
    overdue_pct = overdue_rate * 100

    # Simple, readable business logic for recommendations
    if churn_rate > 0.50:
        churn_msg = "Churn is critically high and requires immediate retention actions."
        recs = [
            "Trigger win-back campaigns for inactive users (email + in-app).",
            "Identify low-usage segments and improve onboarding + product activation.",
            "Offer targeted plan adjustments (downgrade paths) instead of cancellations."
        ]
    elif churn_rate > 0.30:
        churn_msg = "Churn is elevated and should be addressed with targeted retention efforts."
        recs = [
            "Segment churn by plan/channel and focus on the worst-performing segments.",
            "Improve activation funnels and reduce time-to-value for new users."
        ]
    else:
        churn_msg = "Churn is within a controllable range; continue monitoring and optimizing."
        recs = [
            "Sustain product engagement initiatives and monitor early churn signals."
        ]

    if overdue_rate > 0.10:
        pay_msg = "Overdue payments are notable; improve dunning and payment recovery."
        recs.append("Introduce automated dunning workflows and clearer billing reminders.")
    else:
        pay_msg = "Payment health is relatively stable."

    summary = (
        f"Executive Summary ({datetime.now().strftime('%Y-%m-%d %H:%M')}):\n"
        f"- Customer Base: {total} total customers.\n"
        f"- Revenue: Estimated MRR of €{mrr:,.2f} with ARPU of €{arpu:,.2f}.\n"
        f"- Retention: Churn rate is {churn_pct:.1f}% ({churned} churned customers). Risk Level: {risk}. "
        f"{churn_msg}\n"
        f"- Engagement: Average usage score is {avg_usage:.1f}/100.\n"
        f"- Billing: Overdue rate is {overdue_pct:.1f}%. {pay_msg}\n\n"
        f"Recommended Actions:\n"
        + "\n".join([f"- {r}" for r in recs])
    )

    return summary


if __name__ == "__main__":
    # Quick manual test (so you can run this file standalone)
    demo_kpis = {
        "total_customers": 2000,
        "churned_customers": 1200,
        "churn_rate": 0.60,
        "monthly_recurring_revenue": 45000.0,
        "arpu": 32.5,
        "average_usage_score": 51.2,
        "overdue_rate": 0.09,
        "risk_level": "HIGH",
    }
    print(generate_executive_summary(demo_kpis))