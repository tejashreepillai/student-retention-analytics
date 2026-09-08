"""Public recreation of the enrolment-cleaning logic used in the project.

This script is designed for synthetic sample data. It contains no original
student records or confidential institutional data.
"""

from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/student_enrolment_sample.csv")
OUTPUT_PATH = Path("data/student_enrolment_cleaned.csv")

ZERO_FILL_COLUMNS = [
    "ADVANCED_STANDING_CREDIT_POINTS",
    "CREDITED_CREDIT_POINTS",
    "COMPLETED_CREDIT_POINTS",
]


def clean_enrolment_data(data: pd.DataFrame) -> pd.DataFrame:
    """Apply the documented missing-value rules to enrolment data."""

    cleaned = data.copy()

    for column in ZERO_FILL_COLUMNS:
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].fillna(0)

    if "GRADE" in cleaned.columns:
        cleaned["GRADE"] = cleaned["GRADE"].fillna("Not Graded")

    # Missing completion dates and WAM values are intentionally preserved.
    # Their absence may indicate an ongoing course or no completed units.

    return cleaned


def main() -> None:
    """Load, clean and save the synthetic enrolment sample."""

    enrolment_data = pd.read_csv(INPUT_PATH)
    cleaned_data = clean_enrolment_data(enrolment_data)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(OUTPUT_PATH, index=False)

    print(f"Cleaned {len(cleaned_data):,} enrolment records.")
    print(f"Output saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
