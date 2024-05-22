from pathlib import Path

GRAPHS_PATH = Path("../graphs")
# DATA_PATH = Path("../../scraper/data/best")
DATA_PATH = Path("../data")
MODELS_PATH = Path("../models")
PRECOMPUTED_EMBEDDINGS_PATH = Path("../precomputed_embeddings")
SPLIT_DATA_PATH = Path("../split_data")
JSON_PATH = Path("../json/json.json")

IMAGES_PATH = DATA_PATH / "images"
FINAL_CSV = DATA_PATH / "final.csv"

CORE_CLEANED_CSV = DATA_PATH / "core_cleaned.csv"
CORE_FORMATTED_CSV = DATA_PATH / "core_formatted.csv"

ROCAR_CSV = DATA_PATH / "rocar.csv"

PREPROCESSORS_PATH = Path("../preprocessors")
NUMERICAL_SCALER_PATH = PREPROCESSORS_PATH / "numerical_scaler.pkl"
CATEGORICAL_SCALER_PATH = PREPROCESSORS_PATH / "categorical_scaler.pkl"
ENCODER_PATH = PREPROCESSORS_PATH / "encoder.pkl"
TARGET_SCALER_PATH = PREPROCESSORS_PATH / "target_scaler.pkl"

MLP_MODEL_PATH = MODELS_PATH / "mlp_model.pth"
MULTIMODAL_MODEL_PATH = MODELS_PATH / "multimodal_model.pth"
FINE_TUNED_BERT_MODEL_PATH = MODELS_PATH / "fine_tuned_bert_model.pth"
FINE_TUNED_FASTVIT_MODEL_PATH = MODELS_PATH / "fine_tuned_fastvit_model.pth"

TEST_IMAGE_FEATURES_PATH = PRECOMPUTED_EMBEDDINGS_PATH / "test_image_features.npy"
TRAIN_IMAGE_FEATURES_PATH = PRECOMPUTED_EMBEDDINGS_PATH / "train_image_features.npy"
TEST_TEXT_FEATURES_PATH = PRECOMPUTED_EMBEDDINGS_PATH / "test_text_features.npy"
TRAIN_TEXT_FEATURES_PATH = PRECOMPUTED_EMBEDDINGS_PATH / "train_text_features.npy"

TRAIN_DATA_CSV = SPLIT_DATA_PATH / "train_data.csv"
TEST_DATA_CSV = SPLIT_DATA_PATH / "test_data.csv"
