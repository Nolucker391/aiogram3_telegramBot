from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsUser(BaseFilter):

    def __init__(self, user_id: int):
        self.user_id = user_id

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id