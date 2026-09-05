from pydantic import ValidationError
from schema import HackerNewsResponse
from prompt_template import repair_prompt, system_prompt, user_prompt
from LLM_extractor import call_llm


def extract_and_validate(cleaned_text: str, max_retries: int = 3):
    current_user_prompt = user_prompt.format(cleaned_text=cleaned_text[:4000])
    last_output = None

    for attempt in range(max_retries):
        print(f"--- Attempt {attempt + 1} ---")
        
        raw_llm_output = call_llm(system_prompt, current_user_prompt)
        last_output = raw_llm_output 
        
        try:
            validated_data = HackerNewsResponse.model_validate_json(raw_llm_output)
            
            print("Pydantic validation passed!")
            return validated_data.model_dump()
            
        except ValidationError as e:
            print(f"Pydantic validation failed!")
            print(f"Error: {e}")
            
            current_user_prompt = repair_prompt.format(
            previous_response=raw_llm_output,
            error_message=str(e))
            
    raise Exception(f"Failed after {max_retries} retries. Last output: {last_output}")