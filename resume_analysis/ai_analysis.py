import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "meta-llama/Llama-2-7b-chat-hf"
hf_token = os.getenv("HUGGINGFACE_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(model_name, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", load_in_4bit=True, token=hf_token
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_ai_feedback(resume: str, jd: str):
    prompt = (
        f"You are an HR expert. Analyze the resume below in relation to the job description.\n\n"
        f"Resume:\n{resume}\n\nJob Description:\n{jd}\n\n"
        f"Return a professional evaluation."
    )
    response = generator(prompt, max_new_tokens=300)[0]["generated_text"]
    return response.strip()
