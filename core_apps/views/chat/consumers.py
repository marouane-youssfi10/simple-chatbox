import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from core_apps.core.chat.models import Message


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None

    def connect(self):
        self.room_group_name = "test"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = Message.objects.create(
            user=self.scope["user"], message=text_data_json["message"]
        )
        msg.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data_json["message"],
            },
        )

    def chat_message(self, event):
        message = event["message"]
        my_message = Message.objects.filter(message=message).last()
        my_message.save()
        self.send(
            text_data=json.dumps(
                {
                    "type": "chat",
                    "message": message,
                    "request_user": str(my_message.user),
                }
            )
        )
