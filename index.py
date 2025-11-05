import pandas as pd
from elasticsearch import Elasticsearch, helpers

# --- CONNECT TO ELASTICSEARCH ---
client = Elasticsearch(
    hosts=["https://kibana-a40d95.es.us-east-1.aws.elastic.cloud:443"],
    api_key="YmNFS1Nwb0JQaTNTYjBPelh1RDk6SUNyeTFPQUkwVlJleEN1bU5hSEtwUQ==",
    verify_certs=False  
)


index_name = "dummy_incident_tickets"

# --- LOAD CSV ---
df = pd.read_csv("dummy_incident_tickets.csv")

# --- CLEAN DATA ---
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.fillna("Unknown")
df = df.replace(r'^\s*$', "Unknown", regex=True)




if client.indices.exists(index=index_name):
    client.indices.delete(index=index_name)

client.indices.create(index=index_name)

records = df.to_dict(orient="records")
actions = [{"_index": index_name, "_source": record} for record in records]


helpers.bulk(client, actions)
print("Data indexed successfully!")

res = client.search(index=index_name, query={"match_all": {}}, size=5)
print("Sample indexed documents:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])