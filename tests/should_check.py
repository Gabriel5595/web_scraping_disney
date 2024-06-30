from datetime import datetime, time
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def should_check():
    start_checking = time(7,0)
    finish_checking = time(23,30)
    now = datetime.now().time()
    
    if now >= start_checking and now <= finish_checking:
        return True
    else:
        return False

def main():
    print(should_check())

main()