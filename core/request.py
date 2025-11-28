# Handles incoming http rerquest data (reads JSON from the client)

import json 

def parse_json_body(handler):
    """read and decode JSON from HTTP request body."""
    length = int(handler.headers.get("Content-Length" , 0))
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))