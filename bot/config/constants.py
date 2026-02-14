start_msg = """Salom, {name}!
Men Guruhlar uchun mo'ljallangan botman. Agar guruhda kimdir so'kinsa yoki boshqa biror qoidabuzarlik sodir qilsa,
men uni ogohlantiraman va kerak bo'lsa, guruhdan chetlataman. Mening yordamim bilan sizning guruhingiz yanada tinch va xavfsiz bo'ladi!
Botni guruhingizga qo'shish uchun quyidagi tugmani bosing:
"""

SYSTEM_PROMPT = """
You are a strict text moderation classifier.

Task:
Detect profanity, insults, hate speech, or offensive language in any language.

Rules:
- The input contains multiple messages separated by newlines.
- For each line, return ONLY one character:
    1 -> if the line contains profanity/offensive language
    0 -> if the line is clean
- Separate outputs with a space
- No explanations, no extra text, no punctuation
- Output must be exactly 0 or 1 for each line
"""