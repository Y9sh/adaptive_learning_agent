import os
from smolagents import OpenAIModel

def callModel():
    model = OpenAIModel(
        model_id="stealth/crouton-alpha", 
        api_base="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPEN_ROUTER_KEY"),
    )
    return model
