from datetime import datetime


def convert_timestamp_to_iso(ts: str, format: str):
    date = datetime.fromtimestamp(float(int(ts) / 1000)).strftime(format)
    return date


def aggregate_data(format_aggregate: str, data):
    format_date = {
        "hour": "%Y-%m-%dT%H:00:00",
        "day": "%Y-%m-%dT00:00:00",
        "month": "%Y-%m-01T00:00:00",
    }

    result = {}
    for el in data:
        date = convert_timestamp_to_iso(
            el["dt"], format=format_date.get(format_aggregate, "%Y-%m-%dT%H:00:00")
        )
        if result.get(date, None) is None:
            result.update({date: int(el["value"])})
        else:
            result[str(date)] += int(el["value"])

    return {"dataset": [*result.values()], "labels": [*result.keys()]}


if __name__ == "__main__":
    ...
