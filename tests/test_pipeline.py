from src.validation import validate_record

def test_validate_record():
    record = {"record_id": 1, "source": "salesforce", "metric_value": 100}
    assert validate_record(record) is True
