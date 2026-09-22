import json

from analyzer.ai_assessor import assess_risk
from analyzer.pr_analyzer import analyze_files
from analyzer.risk_engine import calculate_risk


def main():
    with open("docs/sample_pr.json") as file:
        pr = json.load(file)

    file_analysis = analyze_files(pr["files"])

    risk = calculate_risk(
        files_changed=pr["files_changed"],
        lines_added=pr["lines_added"],
        lines_deleted=pr["lines_deleted"],
        critical_files_changed=file_analysis["critical_files_changed"],
        database_migration=file_analysis["database_migration"],
        tests_changed=file_analysis["tests_changed"],
    )

    print("\n=== AI Release Risk Analyzer ===\n")

    print(f"PR: {pr['title']}")
    print(f"Risk Level: {risk['level']}")
    print(f"Risk Score: {risk['score']}/10")

    print("\nRisk Factors:")

    for reason in risk["reasons"]:
        print(f"- {reason}")

    assessment = assess_risk(pr, risk)

    print(assessment)

if __name__ == "__main__":
    main()