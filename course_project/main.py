from injectable import load_injection_container
from fastapi import FastAPI

load_injection_container()

from resources.resource_ping import router_ping
from resources.resource_get_model_predictions import router_model


app = FastAPI()


# Register routers
app.include_router(router_ping)
app.include_router(router_model)
