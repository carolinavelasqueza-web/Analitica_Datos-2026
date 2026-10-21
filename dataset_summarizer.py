import pandas as pd


class DatasetSummarizer:
    """Genera un resumen de un DataFrame y lo guarda en un archivo .txt."""

    def __init__(self, df: pd.DataFrame, title: str = "Resumen del dataset"):
        self.df = df
        self.title = title

    def build_summary(self) -> str:
        """Construye el texto del resumen."""
        df = self.df
        nulos = df.isnull().sum()

        lines = [
            self.title,
            "=" * len(self.title),
            f"Filas: {df.shape[0]}",
            f"Columnas: {df.shape[1]}",
            "",
            "Columnas y tipos de datos:",
        ]
        for col, dtype in df.dtypes.items():
            lines.append(f"  - {col}: {dtype}")

        lines += ["", "Valores nulos por columna:"]
        for col, n in nulos.items():
            lines.append(f"  - {col}: {n}")
        lines.append(f"Total de nulos: {int(nulos.sum())}")

        lines += [
            "",
            "Estadísticas descriptivas:",
            df.describe(include="all").to_string(),
        ]
        return "\n".join(lines)

    def save_txt(self, path: str = "resumen_dataset.txt") -> str:
        """Guarda el resumen en un archivo .txt y devuelve la ruta."""
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.build_summary())
        return path 