from domain.interfaces import TransformPipelineInterface
from domain.exceptions import TransformerKeyNotFoundError
from .transformers import AllCases, Continents, Countries


class TransformPipeline(TransformPipelineInterface):
    def __init__(self):
        self._registry = {
            'all_cases': AllCases(),
            'continents': Continents(),
            'countries': Countries(),
        }

    def execute(self, datasets):
        raw_data = {}
        processed_data = {}

        for key, data in datasets.items():
            raw_data[key] = data

            transformer = self._registry.get(key)
            if transformer is None:
                raise TransformerKeyNotFoundError(key=key)
            try:
                processed_data[key] = transformer.transform(data)
            except Exception as e:
                raise RuntimeError(
                    f"Erro no transformer ({transformer.__class__.__name__})"
                ) from e
        
        return raw_data, processed_data
