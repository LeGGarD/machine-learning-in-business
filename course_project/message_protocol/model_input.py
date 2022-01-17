from typing import Dict
from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class ModelInput(BaseModel):
    age: Dict[int, int]
    education: Dict[int, str]
    marital_status: Dict[int, str]
    occupation: Dict[int, str]
    relationship: Dict[int, str]
    capital_gain: Dict[int, int]
    capital_loss: Dict[int, int]
    hours_per_week: Dict[int, int]

    def __init__(self, age: Dict[int, int], education: Dict[int, str], marital_status: Dict[int, str], occupation: Dict[int, str],
                 relationship: Dict[int, str],
                 capital_gain: Dict[int, int], capital_loss: Dict[int, int], hours_per_week: Dict[int, int]) -> None:
        super().__init__(age=age, education=education, marital_status=marital_status, occupation=occupation,
                         relationship=relationship, capital_gain=capital_gain, capital_loss=capital_loss,
                         hours_per_week=hours_per_week)

input = b'{"age":{"34609":69,"40474":28,"24172":54},"education":{"34609":"HS-grad","40474":"Some-college","24172":"Some-college"},"marital_status":{"34609":"Widowed","40474":"Never-married","24172":"Married-civ-spouse"},"occupation":{"34609":"Adm-clerical","40474":"Sales","24172":"Transport-moving"},"relationship":{"34609":"Unmarried","40474":"Other-relative","24172":"Husband"},"capital_gain":{"34609":1848,"40474":0,"24172":0},"capital_loss":{"34609":0,"40474":0,"24172":0},"hours_per_week":{"34609":12,"40474":40,"24172":30}}'
input_alt = ModelInput.parse_raw(input)
print()
