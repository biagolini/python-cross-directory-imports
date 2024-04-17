from shared_functions import add, multiply

# [EN] Uses functions from shared_functions.py to perform addition and multiplication, and prints results.
# [PT] Usa funções de shared_functions.py para realizar adição e multiplicação, e imprime os resultados.
def execute_math_operations(a, b):
    result_add = add(a, b)
    print(f"Addition: {result_add}")
    result_multiply = multiply(a, b)
    print(f"Multiplication: {result_multiply}")
