title: OAuth2 Kakfa and Python
date: 2023-07-10
<!--status: draft-->

[TOC]


This post explains how to utilize OAuth2 in [Faust
Streaming](https://faust-streaming.github.io/faust) applications. Faust is a
streaming library for Python. It provides stream/event processing primitives _a
la_ Kafka Streams to process Kafka messages in Python.

Many organizations are utilizing OAuth2 for managing authentication across
services in a centralized manner. With the introduction of the `OAUTHBEARER`
SASL mechanism in Kafka 2.0.0, both brokers and clients can be configured to
use an external identity provider for authentication.

# Authorization in Kafka

In addition to SSL encryption, Kafka supports multiple _authorization mechanisms_
via Simple Authentication and Security Layer (SASL) to enable authentication
via third-party servers.

- `GSSAPI` (Kerberos)
- `PLAIN` (Username/Password)
- `SCRAM-SHA` (Zookeeper)
- `OAUTHBEARER` (OAuth server)

See the Confluent documentation on [Enabling SASL SSL for
Kafka](https://developer.confluent.io/learn-kafka/security/authentication-ssl-and-sasl-ssl/#enabling-sasl-ssl-for-kafka)
for more information.


The `OAUTHBEARER` security mechanism enables a Kafka cluster to rely on an
external server for authentication. In the case of Confluent Cloud, setting up
an external identity provider is very straight forward, assuming you're using
an OIDC-compliant identity provider (e.g. Azure AD, Okta, Keycloak). See the
[documentation](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-providers.html)
for more information


# OAuth2 Authentication in Faust Streaming

Here's an example of a streaming application straight from their docs:

```python
import faust

app = faust.App('myapp', broker='kafka://localhost')

# Models describe how messages are serialized:
# {"account_id": "3fae-...", "amount": 3}
class Order(faust.Record):
    account_id: str
    amount: int

@app.agent(value_type=Order)
async def order(orders):
    async for order in orders:
        # process infinite stream of orders.
        print(f'Order for {order.account_id}: {order.amount}')
```

Using `OAUTHBEARER` broker credentials requires that we setup at least a
default SSL context, and provide an instance of `AbstractTokenProvider` to the
`oauth_cb`


```python
import faust
from aiokafka.conn import AbstractTokenProvider
from aiokafka.helpers import create_ssl_context

class CustomTokenProvider(AbstractTokenProvider):
    async def token(self):
        ...

broker_credentials = faust.OAuthCredentials(
    oauth_cb=CustomTokenProvider(),
    ssl_context=create_ssl_context(),
)

app = faust.App(
    "myapp",
    broker=KAFKA_BROKER,
    broker_credentials=broker_credentials,
)

```
