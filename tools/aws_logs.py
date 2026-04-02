import json
import random
import sys

def get_pipeline_logs(pipeline_name):
    return {
        "pipeline_name": pipeline_name,
        "failures_last_7_days": random.randint(0, 5),
        "last_error": random.choice([
            "Out of memory",
            "Timeout",
            "Schema mismatch",
            "None"
        ]),
        "retry_rate": round(random.uniform(0, 0.3), 2)
    }

if __name__ == "__main__":
    pipeline_name = sys.argv[1] if len(sys.argv) > 1 else "default_pipeline"
    print(json.dumps(get_pipeline_logs(pipeline_name)))