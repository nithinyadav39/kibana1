**Steps Followed**

Opened the raw dataset file dummy_incident_tickets.csv in Excel to review data quality and structure.

Created a Python script (upload_incident_data.py) to automate cleaning and indexing tasks.

Connected to Elasticsearch Cloud using the API Key for authentication.

Loaded the CSV data into a Pandas DataFrame.

Trimmed unnecessary spaces in all text fields using lambda x: x.strip().

Replaced empty or missing values with "Unknown" to maintain data consistency.

Checked if the Elasticsearch index dummy_incident_tickets already existed — deleted it to avoid duplication.

Created a new index in Elasticsearch for clean data storage.

Converted the DataFrame into a list of JSON-like dictionaries for indexing.

Used the helpers.bulk() function to efficiently upload all records into Elasticsearch.



**Created multiple visualizations using Kibana’s Visualize Library**

![ ](screenshorts/Screenshot%202025-11-05%20161554.png)
![ ](screenshorts/Screenshot%202025-11-05%20161614.png)
![ ](screenshorts/Screenshot%202025-11-05%20161632.png)




**GitHub Branching Workflow**

Created three GitHub branches:

dev → For script development and local testing

stage → For integration and pre-deployment testing

main → For finalized, production-ready code

Cloned the GitHub repository to the local environment using:

git clone https://github.com/<your-username>/incident-data-pipeline.git
cd incident-data-pipeline


Worked and tested code changes in the dev branch.

Created a Pull Request (PR) from dev → stage after successful testing.

Verified the workflow in staging by checking data ingestion and Kibana dashboards.

Once confirmed, created a Pull Request (PR) from stage → main for final promotion.

Merged changes into main — completing the full promotion lifecycle.

**Business Insights from Dashboard**

Most incidents were raised by Automation Engines and Monitoring Systems, reducing manual workload.

About 45% of total tickets were in “Resolved” or “Closed” status, indicating healthy ticket management.

High Priority incidents represented 20% of all tickets — mainly triggered by system alerts.
