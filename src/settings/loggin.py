import logging

logger = logging.getLogger(__name__)

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(filename='../log/pipeline.log', level=logging.INFO, format=FORMAT)

def log_fabric(status, message):
    """Fábrica de logs

    Args:
        status (str): info | warning | error | critical
        message (str): Mensagem a ser registrada
    """
    log_method = {
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
        
    }
    if status not in log_method:
        raise ValueError(f"Status de long inválido {status}")
    
    log_method[status](message)
    
    
    

    