import os
from groq import Groq


class LLMService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment")
        self.client = Groq(api_key=api_key)

    def ask(self, question: str, system_prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ]
        )

        choice = response.choices[0]
        answer = choice.message.content

        if choice.finish_reason == "length":
            raise ValueError("Response was truncated (max_tokens reached)")

        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens

        return {
            "answer": answer,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        }
    