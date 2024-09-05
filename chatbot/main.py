import string
import pickle
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from util import JSONParser


def preprocess(chat):
    # convert to lowercase
    chat = chat.lower()
    # remove punctuation
    punct = tuple(string.punctuation)
    chat = "".join(ch for ch in chat if ch not in punct)
    return chat


def bot_response(chat, pipeline, jp):
    chat = preprocess(chat)
    res = pipeline.predict_proba([chat])
    max_prop = max(res[0])
    # treshold
    if max_prop < 0.2:
        return "Mohon maaf, saya tidak mengerti :(", None
    else:
        max_id = np.argmax(res[0])
        pred_tag = pipeline.classes_[max_id]
        return jp.get_response(pred_tag), pred_tag


def chat(pipeline, jp):
    print("[INFO] Bot sudah terhubung")
    while True:
        chat = input("Anda >>> ")
        res, tag = bot_response(chat, pipeline, jp)
        print(f"Bot >>> {res}")
        if tag == "bye":
            break


# load data
path = "data/intents.json"
jp = JSONParser()
jp.parse(path)
df = jp.get_dataframe()

# preprocess data
# case folding -> convert to lowercase & remove punctuation
# add to column `text_input_prep`
df["text_input_prep"] = df.text_input.apply(preprocess)

# modeling
pipeline = make_pipeline(CountVectorizer(), MultinomialNB())

# train
print("[INFO] Training data ...")
pipeline.fit(df.text_input_prep, df.intents)

# save model
with open("model/chatbot_irufano_model.pkl", "wb") as model_file:
    pickle.dump(pipeline, model_file)

# interaction with bot
if __name__ == "__main__":
    chat(pipeline, jp)
