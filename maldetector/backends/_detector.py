from joblib import load


class MaliciousDetector:
    def __init__(self,
                 model_path: str,
                 label_encoder_path: str) -> None:
        self._classifier = load(model_path)
        self._encoder = load(label_encoder_path)

    def inspect_urls(self, urls: list[str]) -> list[str]:
        logits = self._classifier.predict(urls)
        return list(self._encoder.inverse_transform(logits))
