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

![ ](screenshorts/Screenshot%202025-11-06%20121044.png)
![ ](screenshorts/Screenshot%202025-11-06%20121123.png)
![ ](screenshorts/Screenshot%202025-11-06%20121142.png)
![ ](screenshorts/Screenshot%202025-11-06%20121201.png)





**GitHub Branching Workflow**

Created three GitHub branches:

dev → For script development and local testing

stage → For integration and pre-deployment testing

main → For finalized, production-ready code

Cloned the GitHub repository to the local environment using:

Worked and tested code changes in the dev branch.

Created a Pull Request (PR) from dev → stage after successful testing.

created a Pull Request (PR) from stage → main for final promotion.





