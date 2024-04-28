import os
from pathlib import Path

from cloudpathlib import S3Client, S3Path
from src.settings import settings

S3_DIR_PATH = os.path.join(os.getcwd(), "src/" + "s3/")
PARENT_DIR_PATH = os.path.join(os.getcwd(), "src/" + "s3/")

AWS_MODELS_FOLDER = "models/"
AWS_PREPROCESSORS_FOLDER = "preprocessors/"

AWS_FINE_TUNED_BERT_MODEL = "fine_tuned_bert_model/"
AWS_MULTIMODAL_ENCODER_MODEL = "multimodal_encoder_model.pth"
AWS_MULTIMODAL_MODEL = "multimodal_model.pth"
AWS_SCALER_NUMERICAL = "numerical_scaler.pkl"
AWS_SCALER_CATEGORICAL = "categorical_scaler.pkl"
AWS_ENCODER = "encoder.pkl"

FINE_TUNED_BERT_MODEL = Path(PARENT_DIR_PATH + AWS_MODELS_FOLDER + AWS_FINE_TUNED_BERT_MODEL)
MULTIMODAL_ENCODER_MODEL = Path(PARENT_DIR_PATH + AWS_MODELS_FOLDER + AWS_MULTIMODAL_ENCODER_MODEL)
MULTIMODAL_MODEL = Path(PARENT_DIR_PATH + AWS_MODELS_FOLDER + AWS_MULTIMODAL_MODEL)
SCALER_NUMERICAL = Path(PARENT_DIR_PATH + AWS_PREPROCESSORS_FOLDER + AWS_SCALER_NUMERICAL)
SCALER_CATEGORICAL = Path(PARENT_DIR_PATH + AWS_PREPROCESSORS_FOLDER + AWS_SCALER_CATEGORICAL)
ENCODER = Path(PARENT_DIR_PATH + AWS_PREPROCESSORS_FOLDER + AWS_ENCODER)


def download_dirs_from_s3():
    if not os.path.exists(S3_DIR_PATH):
        os.makedirs(S3_DIR_PATH)

    s3_client = S3Client(aws_access_key_id=settings.aws_access_key, aws_secret_access_key=settings.aws_secret_access_key)

    bucket = "s3://" + settings.bucket_name + "/"
    models_path = S3Path(bucket + AWS_MODELS_FOLDER, client=s3_client)
    preprocessors_path = S3Path(bucket + AWS_PREPROCESSORS_FOLDER, client=s3_client)

    print("Downloading models and preprocessors from S3...\n")
    print("Downloading from S3: ", AWS_MODELS_FOLDER)
    models_path.download_to(S3_DIR_PATH + AWS_MODELS_FOLDER)
    print("S3 download ended successfully!\n")

    print("Downloading from S3: ", AWS_PREPROCESSORS_FOLDER)
    preprocessors_path.download_to(S3_DIR_PATH + AWS_PREPROCESSORS_FOLDER)
    print("S3 download ended successfully!\n")
    print("Downloaded models and preprocessors from S3 successfully!\n")
