# Request Class: Define a class Request with attributes such as request_id (unique identifier, e.g., an integer),
# description (string describing the issue), and maybe a status ("open" or "resolved"). The request_id can be auto-generated
# (for example, use a class variable or a counter in the tracker to assign incremental IDs).

import random

statusTypes = {'OPEN', 'RESOLVED'}

class Request:
    def __init__(self, description: str, status: str):
        self.id = random.randint(1000000, 9999999)  # 7-digit random ID
        self.description = description
        
        status = status.upper()
        
        if status not in statusTypes:
            raise ValueError("Status is not valid")
        
        self.status = status