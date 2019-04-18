import json

def get_secrets():
    with open("/chainwalkers_parser/.secrets.json", "r") as f:
        return json.loads(f.read())

secrets = get_secrets()

NODE_URL = secrets['NODE_URL']