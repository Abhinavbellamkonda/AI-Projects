from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
print(generator("AI is transforming the world because", max_length=50))
