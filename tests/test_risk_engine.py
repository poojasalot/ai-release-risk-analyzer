from src.analyzer.risk_engine import calculate_risk


def test_high_risk_change():
    result = calculate_risk(
        files_changed=80,
        lines_added=900,
        lines_deleted=300,
        critical_files_changed=True,
        database_migration=True,
        tests_changed=False,
    )

    assert result["level"] == "HIGH"
    assert result["score"] >= 7


def test_low_risk_change():
    result = calculate_risk(
        files_changed=3,
        lines_added=20,
        lines_deleted=5,
        critical_files_changed=False,
        database_migration=False,
        tests_changed=True,
    )

    assert result["level"] == "LOW"

def test_medium_risk_change():
    result = calculate_risk(
        files_changed=30,
        lines_added=500,
        lines_deleted=200,
        critical_files_changed=False,
        database_migration=False,
        tests_changed=True,
    )

    assert result["level"] == "LOW"
    assert result["score"] == 0

