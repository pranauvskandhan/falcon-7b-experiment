import os
import psutil
import sys
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

def main():
    model_id = "mlx-community/Falcon-H1-7B-Instruct-4bit"
    prompt_text = "Who is Stefan Salvatore?"

    print(f"--- System Check ---")
    print(f"Available RAM: {psutil.virtual_memory().available / (1024**3):.2f} GB")
    
    # model load
    print(f"Loading {model_id}...")
    model, tokenizer = load(model_id)

    # memory report
    process = psutil.Process(os.getpid())
    print(f"\nFalcon 7B Loaded!")
    print(f"RAM used: {process.memory_info().rss / (1024**3):.2f} GB")

    # prompt format
    messages = [{"role": "user", "content": prompt_text}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # sampler
    sampler = make_sampler(temp=0.7)

    print("\n" + "="*30)
    print(f"QUESTION: {prompt_text}")
    print("="*30 + "\n")

    # generate
    generate(
        model, 
        tokenizer, 
        prompt=prompt, 
        max_tokens=200, 
        sampler=sampler, 
        verbose=True 
    )

if __name__ == "__main__":
    main()