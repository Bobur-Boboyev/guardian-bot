from google import genai
from bot.config.settings import Settings
from bot.config.constants import SYSTEM_PROMPT

client = genai.Client(api_key=Settings.GEMINI_API_KEY)

class Detection:
    def preparation_messages(self, messages_list: list[dict[str:str|int]]) -> str:
        
        if not messages_list:
            return None
        
        analyze = "\n".join([f"{i}. {m['text']}" for i, m in enumerate(messages_list)])

        return analyze


    def is_bawdy(self, analyze: str) -> list:

        if analyze is None:
            return
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=analyze,
                config={
                    "system_instruction": SYSTEM_PROMPT,
                    "temperature": 0,
                    "max_output_tokens": 2 * analyze.count("\n") + 2,
                }
            )
            
            result = response.text.split()
            return result
                
        except Exception as e:
            print(f"AI Error: {e}") 
            return
            
        return

detection = Detection()