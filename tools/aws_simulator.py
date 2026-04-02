import json
import random
import sys

def get_aws_pipeline_metrics(pipeline_name):
    base_cost = random.uniform(50, 200)

    return {
        "pipeline_name": pipeline_name,
        "services": {
            "glue": {
                "runs_per_day": random.choice([6, 12, 24]),
                "avg_duration_minutes": random.randint(10, 30),
                "cost_usd": round(base_cost * 0.4, 2)
            },
            "athena": {
                "queries_per_day": random.randint(10, 100),
                "data_scanned_gb": random.randint(100, 1000),
                "cost_usd": round(base_cost * 0.4, 2)
            },
            "s3": {
                "storage_gb": random.randint(100, 5000),
                "monthly_cost_usd": round(base_cost * 0.2, 2)
            }
        }
    }

if __name__ == "__main__":
    pipeline_name = sys.argv[1] if len(sys.argv) > 1 else "default_pipeline"
    result = get_aws_pipeline_metrics(pipeline_name)
    print(json.dumps(result))