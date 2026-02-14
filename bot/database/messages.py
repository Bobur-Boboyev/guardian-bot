import json
import os

JSON_FILE = "bot/database/messages.json"

class DataBase:
    @staticmethod
    def messages_list():
        if not os.path.exists(JSON_FILE) or os.path.getsize(JSON_FILE) == 0:
            return []
            
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_message(chat_id, message_id, full_name, text):
        data = DataBase.messages_list()
            
        data.append({
            "chat_id": chat_id,
            "message_id": message_id,
            "full_name": full_name,
            "text": text
        })

        json_string = json.dumps(data, indent=4, ensure_ascii=False)
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            f.write(json_string)

    @staticmethod
    def clear_messages():
        empty_json = json.dumps([], indent=4)
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            f.write(empty_json)