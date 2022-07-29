from .models import Quote
from random import choice

def process_message(message):
    if "content" in message and message["type"]=="Generic":
        message_data = Quote()
        message_data.person = message["sender_name"]
        message_data.timestamp = message["timestamp_ms"]
        message_data.quote_text = message["content"]
        message_data.save()

def random_quote():
    pks = Quote.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Quote.objects.get(pk=random_pk)
    return(random_obj)