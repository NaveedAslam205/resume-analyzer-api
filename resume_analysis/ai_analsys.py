from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "meta-llama/Llama-2-7b-chat-hf"  # replace if you're using another variant
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_ai_feedback(resume: str, jd: str):
    prompt = (
        f"You are an HR expert. Analyze the resume below in relation to the job description.\n\n"
        f"Resume:\n{resume}\n\nJob Description:\n{jd}\n\n"
        f"Return a professional evaluation."
    )

    response = generator(prompt, max_new_tokens=300)[0]["generated_text"]
    return response.strip()
