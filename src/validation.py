def validate_record(record):
    required_fields = ["record_id", "source", "metric_value"]
    return all(field in record for field in required_fields)

def validate_batch(records):
    return all(validate_record(r) for r in records)
