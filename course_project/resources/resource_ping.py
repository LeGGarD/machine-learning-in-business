from message_protocol import PingOutput
from shared_utils import UtilsPing

from fastapi import APIRouter

router_ping = APIRouter()
utils_ping = UtilsPing()


@router_ping.get("/ping", response_model=PingOutput)
def ping():
    return utils_ping.build()
