import json
import random

def get_aws_pipeline_metrics():
    return {
        "pipeline_name": "daily_etl",
        "services": {
            "glue": {
                "runs_per_day": 24,
                "avg_duration_minutes": random.randint(10, 20),
                "cost_usd": round(random.uniform(30, 60), 2)
            },
            "athena": {
                "queries_per_day": 50,
                "data_scanned_gb": random.randint(200, 500),
                "cost_usd": round(random.uniform(20, 80), 2)
            },
            "s3": {
                "storage_gb": random.randint(500, 2000),
                "monthly_cost_usd": round(random.uniform(10, 40), 2)
            }
        },
        "estimated_total_cost": 0
    }

def calculate_total(data):
    total = (
        data["services"]["glue"]["cost_usd"] +
        data["services"]["athena"]["cost_usd"] +
        data["services"]["s3"]["monthly_cost_usd"]
    )
    data["estimated_total_cost"] = round(total, 2)
    return data

if __name__ == "__main__":
    data = get_aws_pipeline_metrics()
    data = calculate_total(data)
    print(json.dumps(data))