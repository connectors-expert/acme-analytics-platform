import json
from validation import validate_batch
from utils import log

def extract():
    return [
        {"id": 1, "source": "salesforce", "value": 1000},
        {"id": 2, "source": "zendesk", "value": 500},
        {"id": 3, "source": "github", "value": 200}
    ]

def transform(records):
    return [
        {
            "record_id": r["id"],
            "source": r["source"],
            "metric_value": r["value"]
        }
        for r in records
    ]

def load(records):
    with open("data/output.json", "w") as f:
        json.dump(records, f, indent=2)

def run_pipeline():
    log("Pipeline started")
    data = extract()
    transformed = transform(data)

    if validate_batch(transformed):
        load(transformed)
        log("Pipeline completed successfully")
    else:
        log("Validation failed")

if __name__ == "__main__":
    run_pipeline()
