import pickle

import torch
from src.download import (
    ENCODER,
    FINE_TUNED_BERT_MODEL,
    FINE_TUNED_FASTVIT_MODEL,
    MULTIMODAL_MODEL,
    SCALER_CATEGORICAL,
    SCALER_NUMERICAL,
    TARGET_SCALER,
)
from timm import create_model
from timm.data import create_transform, resolve_model_data_config
from torch import nn
from transformers import AutoModel, AutoTokenizer


def get_models_and_preprocessors():
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    torch.cuda.empty_cache()

    # Load FastViT model
    fastvit = create_model("fastvit_t8.apple_in1k", pretrained=True, num_classes=0)
    fastvit.head = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(fastvit.num_features, 1))
    fastvit.load_state_dict(torch.load(FINE_TUNED_FASTVIT_MODEL, map_location=DEVICE))

    fastvit.eval()
    fastvit.to(DEVICE)

    data_config = resolve_model_data_config(fastvit)
    transforms = create_transform(**data_config, is_training=False)

    class FastViTEmbedding(nn.Module):
        def __init__(self, model):
            super(FastViTEmbedding, self).__init__()
            self.model = model
            self.pool = nn.AdaptiveAvgPool2d(1)

        def forward(self, x):
            # This accesses the last layer before the regression head.
            x = self.model.forward_features(x)
            x = self.pool(x)
            x = x.view(x.size(0), -1)
            return x

    fastvit_model = FastViTEmbedding(fastvit).to(DEVICE)
    fastvit_model.eval()

    # Load BERT model
    tokenizer = AutoTokenizer.from_pretrained(
        "dumitrescustefan/bert-base-romanian-uncased-v1", do_lower_case=True, add_special_tokens=True, max_length=512, padding=True, truncation=True
    )
    bert_model = AutoModel.from_pretrained("dumitrescustefan/bert-base-romanian-uncased-v1")
    bert_model.eval()
    bert_model.to(DEVICE)

    class BERTEmbeddings(nn.Module):
        def __init__(self):
            super(BERTEmbeddings, self).__init__()
            self.bert = bert_model
            self.fc = nn.Linear(768, 1)

        def forward(self, input_ids, attention_mask):
            outputs = self.bert(input_ids, attention_mask)
            outputs = outputs[1]  # Use the output of the [CLS] token
            return outputs

    bert_model = BERTEmbeddings().to(DEVICE)

    bert_model.load_state_dict(torch.load(FINE_TUNED_BERT_MODEL, map_location=DEVICE))
    bert_model.eval()

    model = Net()
    model.to(DEVICE)
    model.load_state_dict(torch.load(MULTIMODAL_MODEL, map_location=DEVICE))

    with open(ENCODER, "rb") as f:
        target_encoder = pickle.load(f)

    with open(SCALER_NUMERICAL, "rb") as f:
        scaler_numerical = pickle.load(f)

    with open(SCALER_CATEGORICAL, "rb") as f:
        scaler_categorical = pickle.load(f)

    with open(TARGET_SCALER, "rb") as f:
        target_scaler = pickle.load(f)

    return fastvit_model, transforms, tokenizer, bert_model, model, target_encoder, scaler_numerical, scaler_categorical, target_scaler


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1546, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)

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
        self.target_scaler = None


ml_ops = MLOps()
