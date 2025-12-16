from .transform import TransformError

class OrchestratorError(TransformError):
    """
    Erro base do orquestrador de transformação.
    """
    
class TransformerKeyNotFoundError(OrchestratorError):
    """ 
    Erro quando a chave de identificação não existe.
    """
    def __init__(self, key) -> None:
        super().__init__(
            f"Chave para acessar a função não foi encontrada: {key}"
        )
