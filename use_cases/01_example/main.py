import sys
import os

# [EN] Set the directory path for code module.
# [PT] Define o caminho do diretório para o módulo code.
current_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.join(current_dir, '../../lib')

# [EN] Add the code directory to sys.path to allow imports.
# [PT] Adiciona o diretório code ao sys.path para permitir importações.
sys.path.append(code_dir)

# [EN] Import the function from using_code module.
# [PT] Importa a função do módulo using_code.
from math_operations_runner import execute_math_operations

# [EN] Import local configuration.
# [PT] Importa a configuração local.
import config

if __name__ == "__main__":
    # [EN] Call the function using local configuration values.
    # [PT] Chama a função usando valores de configuração locais.
    execute_math_operations(config.a, config.b)
