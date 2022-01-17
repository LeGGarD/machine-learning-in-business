import json
from injectable import load_injection_container
load_injection_container()
load_injection_container('../')
from message_protocol import ModelInput

from resources.resource_get_model_predictions import predict
from services.service_get_model_predictions import GetModelPredictions

service_get_model_predictions = GetModelPredictions()

# create mock data and JSON object
sample_data = b'{"age":{"34609":69,"40474":28,"24172":54},"education":{"34609":"HS-grad","40474":"Some-college","24172":"Some-college"},"marital_status":{"34609":"Widowed","40474":"Never-married","24172":"Married-civ-spouse"},"occupation":{"34609":"Adm-clerical","40474":"Sales","24172":"Transport-moving"},"relationship":{"34609":"Unmarried","40474":"Other-relative","24172":"Husband"},"capital_gain":{"34609":1848,"40474":0,"24172":0},"capital_loss":{"34609":0,"40474":0,"24172":0},"hours_per_week":{"34609":12,"40474":40,"24172":30}}'
input = ModelInput.parse_raw(sample_data)

output = predict(input)
print(output.json())

# sample_data = service_random_var_counts.get_truncated_normal(mean=50000, std=5000, low=0, upp=100000).rvs(10)
# input_json_dict = f'{{"random_var_data": {list(sample_data)}}}'
# input_json = json.loads(input_json_dict)
# input = RandomVarCountsInput.parse_obj(input_json)
# print(input.json())
#
# output = random_var_counts(input)
# print(output.json())
