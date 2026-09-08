# Student Retention & Progression Analytics

**Tools:** Power BI • DAX • Data Cleaning • Data Modelling • Dashboard Design

## Project Overview

This academic group project examined student retention, withdrawal and progression patterns using de-identified institutional datasets covering 2020–2025. The objective was to help university decision-makers identify progression bottlenecks, understand differences between student cohorts and determine where earlier support may be beneficial.

The project was completed by a team of five. This repository explains the overall business problem while clearly identifying the components I personally completed. The original institutional datasets are confidential and are not included.

## Business Questions

The analysis was designed around two dashboard audiences: University Executives and Unit Convenors.

The project examined:

- How retention and withdrawal rates changed across different student cohorts
- Whether study load, academic performance and other student characteristics were associated with different outcomes
- Which units showed potential progression bottlenecks or differences between actual and expected pass rates
- Where repeat enrolments and early academic signals could indicate a need for additional support
- How university leaders could use these findings for intervention planning and resource allocation

## Data Preparation

I completed most of the enrolment-data cleaning and prepared the retention classifications used in the dashboard.

The enrolment dataset contained approximately 285,000 records across 43 fields. This was a exisitng de-identified dataset at the university. My preparation work included:

- Profiling the dataset structure, data types and completeness
- Auditing missing values across the available fields
- Replacing missing advanced-standing, credited and completed credit points with zero where the missing value represented no recorded credit
- Labelling missing grades as `Not Graded`
- Retaining missing course-completion dates and weighted average marks where the absence carried meaningful information, rather than applying an unsupported imputation
- Creating a code tag in the retention data to classify whether a course was retained or discontinued based on course transfers and withdrawals

The source datasets and student-level records are not included in this public repository due to data privacy concerns.
  
## My Contribution

My individual contribution focused on preparing the data, developing key dashboard components and communicating the results clearly to a business audience.

- Completed the majority of the data cleaning required for analysis
- Built most of the charts used in the University Executive dashboard
- Developed the dashboard colour scheme and reviewed design options proposed by other team members
- Created the retention-rate and withdrawal-rate KPIs
- Developed DAX calculations supporting the dashboard metrics
- Connected the student enrolment and retention datasets so they could jointly inform the KPIs
- Redesigned the final presentation to communicate the findings in business-friendly language rather than technical jargon

The Student Success Risk Predictor was developed by other members of the project team and is not presented as my individual work, although I did assess the data used and the methodology.
