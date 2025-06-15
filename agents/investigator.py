from transformers import pipeline

class Investigator:
    """Investigates the root cause of failure using LLM."""
    def __init__(self):
        self.llm = pipeline("text-generation", model="gpt2")  # Replace with your LLM
        self.prompt = (
            "Analyze the following failure information and determine the root cause. "
            "Is it a selector issue, API response change, or missing element?\n"
            "Failure Info: {failure_info}\nOutput:"
        )

    def investigate(self, failure_info):
        print(f"Investigator: Using LLM to analyze root cause for {failure_info['test_case']}...")
        input_prompt = self.prompt.format(failure_info=failure_info)
        # result = self.llm(input_prompt, max_length=100)[0]['generated_text']
        # Parse result (mocked)
        return {"root_cause": "Selector changed in UI"}
