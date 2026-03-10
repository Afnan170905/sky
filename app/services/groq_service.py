from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def explain_topic(topic,level):

    prompt=f"""
    Explain {topic} for a {level} level ML student.
    Include visual explanation ideas and simple examples.
    """

    chat_completion = client.chat.completions.create(
        messages=[{"role":"user","content":prompt}],
        model="llama3-70b-8192"
    )

    return chat_completion.choices[0].message.content