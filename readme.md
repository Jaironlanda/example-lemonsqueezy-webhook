# Lemonsqueezy Webhook with FastAPI (Example)

Example [Lemonsqueezy](lemonsqueezy.com) webhook to capture:
- `order_created`
- `subscription_created`
- `subscription_updated`

Learn More: [Lemonsqueezy Webhook](https://docs.lemonsqueezy.com/api/webhooks)

## Setup environment

1. Rename `.env-temp` to `.env`
2. `SIGNING_SECRET` The secret can be anything you want but is normally a random string between 6 and 40 characters in length.
3. Minimum python version `3.10`


## Install
`pip install -r requirements.txt`

## Run

`uvicorn main:app --reload`
