import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

def query_llm(prompt):
    body = {
        "inputText": prompt
    }

    response = client.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    return result["results"][0]["outputText"]