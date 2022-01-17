from message_protocol import ModelOutput, ModelInput
from shared_utils.utils_ping import UtilsPing

from services.service_get_model_predictions import GetModelPredictions

from fastapi import APIRouter
import time

router_model = APIRouter()
utils_ping = UtilsPing()

service_get_model_prediction = GetModelPredictions()


@router_model.post("/predict", response_model=ModelOutput)
def predict(input: ModelInput) -> ModelOutput:
    t1 = time.time()
    output = service_get_model_prediction.process(input)
    t2 = time.time()
    print('resource_model_prediction.predict(): Took ' + str(round(t2 - t1, 2)) + ' seconds')
    return output
