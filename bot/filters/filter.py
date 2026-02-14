from telegram.ext import BaseFilter
from telegram import Update, Chat


class CustomFilters:
    class IsGroup(BaseFilter):
        def __call__(self, update: Update):
            if update.message is None:
                return False
        
            return update.message.chat.type in (Chat.GROUP, Chat.SUPERGROUP)
    
    class IsPrivate(BaseFilter):
        def __call__(self, update: Update):
            if update.message is None:
                return False

            return update.message.chat.type in (Chat.PRIVATE)
    
    is_group = IsGroup()
    is_private = IsPrivate()
     
