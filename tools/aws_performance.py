import json
import random
import sys

def get_pipeline_performance(pipeline_name):
    return {
        "pipeline_name": pipeline_name,
        "avg_runtime_minutes": random.randint(10, 60),
        "p95_runtime": random.randint(30, 90),
        "data_processed_gb": random.randint(50, 1000),
        "bottleneck": random.choice([
            "Glue job",
            "Athena query",
            "S3 read",
            "None"
        ])
    }

if __name__ == "__main__":
    pipeline_name = sys.argv[1] if len(sys.argv) > 1 else "default_pipeline"
    print(json.dumps(get_pipeline_performance(pipeline_name)))