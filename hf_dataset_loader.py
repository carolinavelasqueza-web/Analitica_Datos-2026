import pandas as pd
import os
from datasets import load_dataset, DatasetDict
from dotenv import load_dotenv

# Cargar variables del archivo .env al importar el módulo
load_dotenv()


class HFDatasetLoader:
    """Carga un dataset de Hugging Face y lo devuelve como DataFrame de pandas."""

    def __init__(self, dataset_id: str, split: str | None = None):
        self.dataset_id = dataset_id
        self.split = split

    def load(self) -> pd.DataFrame:
        """Descarga el dataset desde Hugging Face y lo convierte a DataFrame."""
        # Leer el token desde la variable de entorno (viene del .env)
        token = os.environ.get("HF_TOKEN")

        try:
            data = load_dataset(self.dataset_id, split=self.split, token=token)
        except Exception as e:
            raise RuntimeError(f"No se pudo cargar '{self.dataset_id}': {e}") from e

        # Sin split, load_dataset devuelve un DatasetDict (varios splits)
        if isinstance(data, DatasetDict):
            first_split = list(data.keys())[0]
            data = data[first_split]

        return data.to_pandas()