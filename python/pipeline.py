from kpi_engine import calculate_kpis
from ai_report_generator import generate_executive_summary
from db_manager import initialize_database, insert_report


def main():
    initialize_database()

    kpis = calculate_kpis("data/saas_subscriptions.csv")
    summary = generate_executive_summary(kpis)

    insert_report(kpis, summary)

    print("\n=== KPIs ===")
    print(kpis)
    print("\n=== Executive Summary ===")
    print(summary)
    print("\nReport stored in database.")


if __name__ == "__main__":
    main()