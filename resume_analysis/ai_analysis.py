from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline

model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_ai_feedback(resume: str, jd: str):
    prompt = (
        f"Evaluate this resume in relation to the job description.\n\n"
        f"Resume:\n{resume}\n\nJob Description:\n{jd}\n\n"
        f"Provide professional feedback:"
    )
    response = generator(prompt, max_new_tokens=300)[0]["generated_text"]
    return response.strip()
