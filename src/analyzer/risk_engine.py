def calculate_risk(
    files_changed: int,
    lines_added: int,
    lines_deleted: int,
    critical_files_changed: bool,
    database_migration: bool,
    tests_changed: bool,
) -> dict:
    """Calculate a release risk score based on the scope and characteristics of a code change.

    This function assesses the risk level of a proposed code change by summing weighted
    signals from several risk factors, including the size of the change, modifications to
    critical files, database migration activity, and whether tests were updated. The score
    is then mapped to a categorical risk level.

    Args:
        files_changed (int): The total number of files modified in the change.
        lines_added (int): The number of lines added by the change.
        lines_deleted (int): The number of lines removed by the change.
        critical_files_changed (bool): True if the change modifies files considered critical
            to application stability or production behavior.
        database_migration (bool): True if the change includes a database schema or data
            migration.
        tests_changed (bool): True if the change includes accompanying test updates.

    Returns:
        dict: A dictionary with the following keys:
            - "score" (int): The cumulative risk score.
            - "level" (str): The risk classification, one of "LOW", "MEDIUM", or "HIGH".
            - "reasons" (list[str]): A list of human-readable explanations for the score.
    """
    score = 0
    reasons = []

    # Size of change
    if files_changed > 50:
        score += 2
        reasons.append("Large number of files changed")

    if lines_added + lines_deleted > 1000:
        score += 2
        reasons.append("Large code change")

    # Critical systems
    if critical_files_changed:
        score += 2
        reasons.append("Critical system code modified")

    # Database
    if database_migration:
        score += 2
        reasons.append("Database migration detected")

    # Testing
    if not tests_changed:
        score += 2
        reasons.append("No test changes detected")

    if score >= 7:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "reasons": reasons,
    }