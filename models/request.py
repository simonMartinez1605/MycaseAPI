from pydantic import BaseModel

class Keys(BaseModel):
    client_id : bytes
    redirect_uri : str