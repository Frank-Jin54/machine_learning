# from transformers import DefaultDataCollator
import tensorflow as tf
import torch
from datasets import load_dataset
import os
from transformers import TFAutoModelForSequenceClassification, DistilBertForMaskedLM, TFBertForMaskedLM
from transformers import T5ForConditionalGeneration
from transformers import T5Tokenizer
from transformers import create_optimizer
from transformers import DataCollatorWithPadding
from transformers import AutoTokenizer
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(CURRENT_FOLDER, "model/T5")
# model = T5ForConditionalGeneration.from_pretrained('google/t5-v1_1-small')
# model.save_pretrained(os.path.join(model_path, "model"))

tokenizer = T5Tokenizer.from_pretrained('google/t5-v1_1-small')
tokenizer.save_pretrained(os.path.join(model_path, "tokenizer"))

fromconfig_path = os.path.join(CURRENT_FOLDER, "model/t5-v1_1-small")
toconfig_path = "gs://nlp_resources/pretrained_models/torch/"

os.system("gsutil cp -r {} {}".format(fromconfig_path, toconfig_path))