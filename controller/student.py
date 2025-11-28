import json 
from core.response import send_json, send_404
from core.request import parse_json_body
from service.student_service import (
    service_get_all
)