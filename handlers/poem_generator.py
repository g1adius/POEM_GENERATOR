import torch
from transformers import GPT2Tokenizer
import textwrap

if torch.cuda.is_available():
  device = torch.device("cuda")
else:
  device = torch.device("cpu")

morgenshtern_model = torch.load('../model_weights/morgenshtern.pth', map_location=torch.device('cpu'))
oxxxymiron_model = torch.load('../model_weights/oxxxymiron.pth', map_location=torch.device('cpu'))
scryptonite_model = torch.load('../model_weights/sсryptonite.pth', map_location=torch.device('cpu'))
tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3small_based_on_gpt2')

def gen_morgenshtern(text_message):
    prompt = text_message
    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = morgenshtern_model.generate(
        input_ids=prompt,
        max_length=88,
        num_beams=2,
        do_sample=True,
        temperature=1.,
        top_k=5,
        top_p=0.3,
        no_repeat_ngram_size=2,
        num_return_sequences=1,
    ).cpu().numpy()
    text = textwrap.fill(tokenizer.decode(out[0]), 120).replace('\n', ' ')
    return text[:text.rfind([letter for letter in text if letter.isupper()][-1])]

def gen_oxxxymiron(text_message):
    prompt = text_message
    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = oxxxymiron_model.generate(
        input_ids=prompt,
        max_length=88,
        num_beams=3,
        do_sample=True,
        temperature=1.,
        top_k=5,
        top_p=0.5,
        no_repeat_ngram_size=1,
        num_return_sequences=1,
    ).cpu().numpy()
    text = textwrap.fill(tokenizer.decode(out[0]), 120).replace('\n', ' ')
    return text[:text.rfind([letter for letter in text if letter.isupper()][-1])]

def gen_scryptonite(text_message):
    prompt = text_message
    prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)
    out = scryptonite_model.generate(
        input_ids=prompt,
        max_length=88,
        num_beams=3,
        do_sample=True,
        temperature=1.,
        top_k=5,
        top_p=0.5,
        no_repeat_ngram_size=2,
        num_return_sequences=7,
    ).cpu().numpy()
    text = textwrap.fill(tokenizer.decode(out[0]), 120).replace('\n', ' ')
    return text[:text.rfind([letter for letter in text if letter.isupper()][-1])]