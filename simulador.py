import random
from collections import deque


# CONFIGURAÇÕES DO SISTEMA
MEMORIA_PRINCIPAL = 64 * 1024      # 64 KB
MEMORIA_VIRTUAL = 1 * 1024 * 1024  # 1 MB
TAMANHO_PAGINA = 8 * 1024          # 8 KB

NUM_FRAMES = MEMORIA_PRINCIPAL // TAMANHO_PAGINA
NUM_PAGINAS = MEMORIA_VIRTUAL // TAMANHO_PAGINA



# PROCESSO LEVE
class Processo:
    def __init__(self, pid, tamanho):
        self.pid = pid
        self.tamanho = tamanho
        self.memoria = bytearray(random.getrandbits(8) for _ in range(tamanho))



# MMU E SIMULADOR
class MMU:
    def __init__(self):
        self.frames = [None] * NUM_FRAMES  # memória principal
        self.tabela_paginas = {}  # (pid, pagina) -> frame
        self.fila_fifo = deque()  # para substituição FIFO

    def traduzir_endereco(self, processo, endereco_virtual):
        pagina = endereco_virtual // TAMANHO_PAGINA
        offset = endereco_virtual % TAMANHO_PAGINA

        chave = (processo.pid, pagina)

        if chave in self.tabela_paginas:
            frame = self.tabela_paginas[chave]
            endereco_fisico = frame * TAMANHO_PAGINA + offset

            print(f"[HIT] Processo {processo.pid} -> vAddr {endereco_virtual} "
                  f"=> pAddr {endereco_fisico}")
            return endereco_virtual

        else:
            print(f"[PAGE FAULT] Processo {processo.pid}, página {pagina}")
            self.tratar_page_fault(processo, pagina)
            return self.traduzir_endereco(processo, endereco_virtual)

    def tratar_page_fault(self, processo, pagina):
        # Procurar frame livre
        if None in self.frames:
            frame = self.frames.index(None)
            print(f"-> Carregando página no frame livre {frame}")
        else:
            # Substituição FIFO
            frame = self.fila_fifo.popleft()
            print(f"-> Substituindo frame {frame}")

            # Remove página antiga
            for k, v in list(self.tabela_paginas.items()):
                if v == frame:
                    del self.tabela_paginas[k]

        # Carrega página
        self.frames[frame] = (processo.pid, pagina)
        self.tabela_paginas[(processo.pid, pagina)] = frame
        self.fila_fifo.append(frame)

    def ler_memoria(self, processo, endereco):
        if endereco >= processo.tamanho:
            print("Endereço inválido no processo")
            return None

        valor = processo.memoria[endereco]
        print(f"Conteúdo lido: {valor}")
        return valor


# SIMULAÇÃO
def simular():
    mmu = MMU()

    # Criando 2 processos leves
    p1 = Processo(pid=1, tamanho=20000)
    p2 = Processo(pid=2, tamanho=50000)

    processos = [p1, p2]

    # Gerando instruções aleatórias
    for i in range(20):
        proc = random.choice(processos)
        endereco = random.randint(0, proc.tamanho - 1)

        print("\n==============================")
        print(f"Instrução {i+1}")
        print(f"Processo {proc.pid} acessa {endereco}")

        mmu.traduzir_endereco(proc, endereco)
        mmu.ler_memoria(proc, endereco)


# EXECUÇÃO
if __name__ == "__main__":
    simular()