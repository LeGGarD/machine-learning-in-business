from injectable import injectable
from message_protocol import ModelInput, ModelOutput
import pickle
import pandas as pd

@injectable
class GetModelPredictions:

    def process(self, input: ModelInput) -> ModelOutput:
        model_path = '/app/models/model02.pkl'
        loaded_model = pickle.load(open(model_path, 'rb'))
        df = pd.read_json(input.json(), orient='columns')
        predictions = loaded_model.predict(df)
        return ModelOutput(predictions.tolist())
