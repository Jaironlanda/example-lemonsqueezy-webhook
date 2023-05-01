from fastapi import FastAPI, Request, HTTPException, status
from dotenv import load_dotenv
import os
import hashlib
import hmac
import json

load_dotenv()

app = FastAPI()

secret = os.getenv('SIGNING_SECRET')

def validateWebhook(req_body, x_signature):
  digest = hmac.new(secret.encode(), req_body, hashlib.sha256).hexdigest()

  if not hmac.compare_digest(digest, x_signature):
    return False
  
  return True


def decode_event_name(event):
  """
  By default, the request header type is in bytes.
  This method converts the bytes to JSON objects.
  """
  
  json_str = event.decode('utf-8') # Convert bytes to string
  data  = json.loads(json_str) # Parse JSON data into a python object
  
  return data

@app.post('/webhook')
async def webhook(req: Request):

  signature = req.headers.get('x-signature')
  body = await req.body()

  if validateWebhook(body, signature):
    event_name = req.headers.get('x-event-name')
    
    if event_name == 'order_created':
      data = decode_event_name(body)
      # do something with this data
      print(data)

    elif event_name == 'subscription_created':
      # subscriptions
      data = decode_event_name(body)
      # do something with this data
      print(data)
    
    elif event_name == 'subscription_updated':
      data = decode_event_name(body)
      # do something with this data
      print(data)

    else:
      print('Invalid Event Name')

    return {"message":"Success"}

  raise HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Invalid Signing Secret"
  )


  