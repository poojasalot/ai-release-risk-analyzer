from pathlib import Path


CRITICAL_PATHS = [
    "auth",
    "payment",
    "security",
    "database",
]


def analyze_files(files: list[str]) -> dict:
    critical_files = []

    database_migration = False
    tests_changed = False

    for file in files:
        lower_file = file.lower()

        if any(path in lower_file for path in CRITICAL_PATHS):
            critical_files.append(file)

        if "migration" in lower_file:
            database_migration = True

        if "test" in lower_file:
            tests_changed = True

    return {
        "critical_files": critical_files,
        "critical_files_changed": bool(critical_files),
        "database_migration": database_migration,
        "tests_changed": tests_changed,
    }