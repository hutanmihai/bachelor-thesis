import pickle

import torch
from src.download import ENCODER, FINE_TUNED_BERT_MODEL, MULTIMODAL_ENCODER_MODEL, MULTIMODAL_MODEL, SCALER_CATEGORICAL, SCALER_NUMERICAL
from timm import create_model
from timm.data import create_transform, resolve_model_data_config
from torch import nn
from torch.nn import TransformerEncoder, TransformerEncoderLayer
from transformers import AutoModelForMaskedLM, AutoTokenizer


def get_models_and_preprocessors():
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    torch.cuda.empty_cache()

    fastvit_model = create_model("fastvit_t8.apple_in1k", pretrained=True, num_classes=0)
    fastvit_model = fastvit_model.eval()
    fastvit_model.to(DEVICE)
    fastvit_model.eval()

    data_config = resolve_model_data_config(fastvit_model)
    transforms = create_transform(**data_config, is_training=False)

    tokenizer = AutoTokenizer.from_pretrained("dumitrescustefan/bert-base-romanian-cased-v1")
    bert_model = AutoModelForMaskedLM.from_pretrained(FINE_TUNED_BERT_MODEL)
    bert_model.config.output_hidden_states = True
    bert_model.to(DEVICE)
    bert_model.eval()

    encoder_layer = TransformerEncoderLayer(
        d_model=768 * 2,
        nhead=8,
        dim_feedforward=512,
        dropout=0.1,
        activation="relu",
    )

    multimodal_encoder = TransformerEncoder(encoder_layer, num_layers=6)
    multimodal_encoder.to(DEVICE)
    multimodal_encoder.load_state_dict(torch.load(MULTIMODAL_ENCODER_MODEL, map_location=DEVICE))

    model = Net(multimodal_encoder=multimodal_encoder)
    model.to(DEVICE)
    model.load_state_dict(torch.load(MULTIMODAL_MODEL, map_location=DEVICE))

    with open(ENCODER, "rb") as f:
        target_encoder = pickle.load(f)

    with open(SCALER_NUMERICAL, "rb") as f:
        scaler_numerical = pickle.load(f)

    with open(SCALER_CATEGORICAL, "rb") as f:
        scaler_categorical = pickle.load(f)

    return fastvit_model, transforms, tokenizer, bert_model, model, target_encoder, scaler_numerical, scaler_categorical


class Net(nn.Module):
    def __init__(self, multimodal_encoder):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(12, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 1)
        self.dropout = nn.Dropout(0.2)
        self.transformer = multimodal_encoder

    def forward(self, x):
        structured_data = x[:, -10:]
        embeddings = x[:, :-10]
        x = self.transformer(embeddings)
        cls_tokens = x[:, [0, 768]]
        x = torch.cat((cls_tokens, structured_data), dim=1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.dropout(x)
        x = self.fc4(x)
        return x


class MLOps:
    def __init__(self):
        self.fastvit_model = None
        self.transforms = None
        self.tokenizer = None
        self.bert_model = None
        self.model = None
        self.target_encoder = None
        self.scaler_numerical = None
        self.scaler_categorical = None


ml_ops = MLOps()
