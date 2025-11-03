import pandas as pd
from elasticsearch import Elasticsearch, helpers

# --- CONNECT TO ELASTICSEARCH ---
client = Elasticsearch(
    hosts=["https://kibana-a40d95.es.us-east-1.aws.elastic.cloud:443"],
    api_key="YmNFS1Nwb0JQaTNTYjBPelh1RDk6SUNyeTFPQUkwVlJleEN1bU5hSEtwUQ==",
    verify_certs=False  # This skips SSL check (okay for testing)
)

# Step 2: Set the index name
index_name = "dummy_incident_tickets"

# Step 3: Load the CSV file
df = pd.read_csv("dummy_incident_tickets.csv")


# --- CONVERT TO LIST OF DICTS ---
records = df.to_dict(orient="records")

# --- BULK INDEX INTO ELASTICSEARCH ---
actions = [
    {"_index": index_name, "_source": record}
    for record in records
]

helpers.bulk(client, actions)
print("Data indexed successfully!")

# --- VERIFY DATA ---
res = client.search(index=index_name, query={"match_all": {}}, size=5)
print("Sample indexed documents:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])