# Analítica de Datos 2026 - Evidencia de Aprendizaje 1

## Descripción
Proyecto que carga un dataset desde Hugging Face, aplica transformaciones y genera un resumen en archivo .txt.

## Estructura del proyecto
- `hf_dataset_loader.py` → Clase para cargar datasets de Hugging Face
- `dataset_summarizer.py` → Clase para generar resúmenes de DataFrames
- `flujo_completo1.ipynb` → Notebook que coordina el flujo completo
- `resumen_dataset.txt` → Resumen generado del dataset transformado
- `requirements.txt` → Dependencias del proyecto

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
