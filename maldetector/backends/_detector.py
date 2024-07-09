from joblib import load
from re import findall


class MaliciousDetector:
    __ru_answers = {
        'benign': 'неопасно',
        'phishing': 'фишинг',
        'defacement': 'порча данных',
        'malware': 'вредоностная ссылка'
    }

    def __init__(self,
                 model_path: str,
                 label_encoder_path: str) -> None:
        self._classifier = load(model_path)
        self._encoder = load(label_encoder_path)

    @staticmethod
    def find_urls(message: str) -> list[str]:
        pattern = r'''(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+
        [a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.
        [^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.
        [a-zA-Z0-9]+\.[^\s]{2,}|[a-zA-Z0-9]+\.[^\s]{2,})'''
        result = findall(pattern, message)
        return result

    def inspect_urls(self, message: str) -> list[str]:
        urls = self.find_urls(message)
        if urls:
            logits = self._classifier.predict(urls)
            return [f'{url}: {self.__ru_answers[label]}'
                    for url, label in zip(
                        urls,
                        self._encoder.inverse_transform(logits)
                    )]
        return []
