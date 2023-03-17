# transfer model from huggingface to nlp-resource
import tensorflow as tf
import torch
from datasets import load_dataset

import os
from transformers.src.transformers import TFAutoModelForSequenceClassification, TFDistilBertForMaskedLM, TFBertForMaskedLM
from transformers.src.transformers import create_optimizer
from transformers.src.transformers import DataCollatorWithPadding
from transformers.src.transformers import AutoTokenizer
import os

model_name = "distilbert-base-uncased"
bucket = "nlp-resource"

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(CURRENT_FOLDER, "model/tf/distillbert")

tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.save_pretrained(os.path.join(model_path, "tokenizer"))

model = TFDistilBertForMaskedLM.from_pretrained(model_name)
model.save_pretrained(os.path.join(model_path, "model"))

fromconfig_path = model_path
toconfig_path = "gs://nlp_resources/pretrained_models/tf/"

os.system("gsutil cp -r {} {}".format(fromconfig_path, toconfig_path))
