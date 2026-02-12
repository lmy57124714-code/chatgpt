import os
from openai import OpenAI

# Initialize the client (API key and base URL are pre-configured in the environment)
client = OpenAI()

def test_codex_automation():
    print("--- Starting Codex-style Automation Test ---")
    
    # Prompt for code generation
    prompt = "Write a short Python script that prints 'Hello from Codex Automation!' and lists the files in the current directory."
    
    print(f"Requesting code generation for: {prompt}")
    
    try:
        # Using gpt-4.1-nano for speed as requested
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes only raw Python code without any markdown formatting or explanations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        
        generated_code = response.choices[0].message.content.strip()
        
        # Clean up markdown if the model accidentally included it
        if generated_code.startswith("```python"):
            generated_code = generated_code.split("```python")[1].split("```")[0].strip()
        elif generated_code.startswith("```"):
            generated_code = generated_code.split("```")[1].split("```")[0].strip()

        print("\n--- Generated Code ---")
        print(generated_code)
        print("----------------------\n")
        
        print("Executing generated code...")
        # Execute the generated code
        exec(generated_code)
        
        print("\n--- Test Completed Successfully ---")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_codex_automation()
