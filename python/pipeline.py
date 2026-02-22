from kpi_engine import calculate_kpis
from ai_report_generator import generate_executive_summary


def main():
    kpis = calculate_kpis("data/saas_subscriptions.csv")
    summary = generate_executive_summary(kpis)

    print("\n=== KPIs ===")
    print(kpis)
    print("\n=== Executive Summary ===")
    print(summary)


if __name__ == "__main__":
    main()