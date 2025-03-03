from vllm import LLM

class Codestral2501:
    def __init__(self, host, port, protocol, api_key):
        self.llm = LLM(
            model="codestral_25_01",
            host=host,
            port=port,
            protocol=protocol,
            api_key=api_key,
        )

    def generate(self, prompt, system_prompt):
        response = self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
        )
        return response.outputs[0].text