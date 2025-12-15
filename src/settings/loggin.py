import logging
import os 

from .constants import PATHLOG
from .constants import FORMAT

logger = logging.getLogger(__name__)

os.makedirs(PATHLOG, exist_ok=True)

logging.basicConfig(filename=f'{PATHLOG}/pipeline.log', level=logging.INFO, format=FORMAT)

def log(status, message):
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
    
    
    

    