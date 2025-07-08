# Marketing-insight-dashboard
This project simulates a B2B email marketing campaign for DHL’s CSI unit, including audience segmentation, email generation, LinkedIn scheduling, and analytics.

## Setup
1. Install dependencies: `pip install pandas streamlit jinja2 matplotlib sqlite3`
2. Run segmentation: `python scripts/segment_customers.py`
3. Generate emails: `python scripts/generate_emails.py`
4. View dashboard: `streamlit run scripts/dashboard.py`

## Folder Structure
- `emails/`: Contains email templates and generated emails.
- `data/`: Mock datasets for customers, metrics, and LinkedIn posts.
- `scripts/`: Python scripts for segmentation, email generation, and dashboard.
- `docs/`: Documentation and process improvement report.

## Process Improvements
- Automate email rendering with GitLab CI.
- Integrate AWS Aurora for real-time data storage.
- Enhance personalization with AMPscript-like logic.
