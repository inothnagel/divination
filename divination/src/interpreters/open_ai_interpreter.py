from openai import OpenAI
from openai.types.chat import ChatCompletion

from divination.src.interpreters.interpreter import Interpreter
from divination.src.reading import Reading


class OpenAIInterpreter(Interpreter):
    """An interpreter that uses OpenAI's GPT-4 to interpret readings."""

    def __init__(self, api_key: str, config: dict):
        self.validate_config(config)
        self.config = config
        self.client = OpenAI(api_key=api_key)

    def _ask(
        self,
        model: str,
        system_prompt: str,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ) -> ChatCompletion:
        """Ask a question to the OpenAI API."""
        response = self.client.chat.completions.create(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        return response

    def interpret(self, reading: Reading) -> str:
        """Interpret a reading using OpenAI's GPT API."""
        prompt = reading.prompt
        system_prompt = self.config["open_ai_prompt_settings"]["system_prompt"]
        model = self.config["open_ai_prompt_settings"]["model"]
        response = self._ask(
            model=model,
            system_prompt=system_prompt,
            prompt=prompt,
            max_tokens=self.config["open_ai_prompt_settings"]["max_tokens"],
            temperature=self.config["open_ai_prompt_settings"]["temperature"],
        )
        return response.choices[0].message.content

    def validate_config(self, config: dict) -> dict:
        """Validate the given configuration dictionary."""
        if "open_ai_prompt_settings" not in config:
            raise ValueError(
                "Config should have a section called: open_ai_prompt_settings"
            )

        required_keys = ["max_tokens", "temperature", "model", "system_prompt"]
        for key in required_keys:
            if key not in config["open_ai_prompt_settings"]:
                raise ValueError(f"Config is missing required key: {key}")
        return config
