"""Public recreation of the retention classification used in the project.

This script works only with synthetic sample data and contains no original
institutional records.
"""

from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/student_retention_sample.csv")
OUTPUT_PATH = Path("data/student_retention_classified.csv")


def classify_retention(row: pd.Series) -> str:
    """Classify a student's year-to-year progression outcome."""

    if row["COURSE_COMPLETION_COUNT"] > 0:
        return "Completed"

    if row["COURSE_CONTINUE_ENROLMENT_X1"] == 1:
        return "Course Retained"

    if row["FACULTY_CONTINUE_ENROLMENT_X1"] == 1:
        return "Faculty Retained"

    if row["UNIVERSITY_CONTINUE_ENROLMENT_X1"] == 1:
        return "MQ Retained"

    return "Not Retained in Year X + 1"


def main() -> None:
    """Load the synthetic retention data and create CODE_TAG."""

    retention_data = pd.read_csv(INPUT_PATH)
    retention_data["CODE_TAG"] = retention_data.apply(
        classify_retention,
        axis=1,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    retention_data.to_csv(OUTPUT_PATH, index=False)

    print(retention_data["CODE_TAG"].value_counts())
    print(f"Output saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
