import glob

def ngram_sequence(data, window_size):
    """
    Gera todas as sequências de ngramn a partir dos dados das syscall.
    @return:
    """
    grams = []

    for idx in range((len(data) + 1 - window_size)):
        grams.append(
            [data[i] for i in range(idx, idx + window_size)])

    return grams

def extract_calls_id(file_name):
    """
    Extrai a sequência de id nos arquivos .idx.
    """
    with open(file_name, 'r') as input_data:
        r_data = input_data.read().split()
        return ([d.split(',')[1] for d in r_data])

def output_gram(file_name, grams):
    """
    Gera os arquivos .gram a partir da lista de grams fornecida.
    """
    with open(file_name+'.gram', 'w') as output:
        for idx in range(len(grams) - 1):
            data = [str(value) for value in grams[idx]]
            data = ",".join(data)
            output.write(data + "\n")

        data = [value for value in grams[-1]]
        data = ",".join(data)
        output.write(data)

def syscall_id(syscall_file):
    """
    Gera os arquivos csv .idx contendo cada syscall e seu id a partir
    dos arquivos .log presentes no diretório de trabalho.
    """

    with open(syscall_file, 'r') as fhand:
        idx_file = syscall_file[:syscall_file.rfind('.')] + '.idx'

        id_calls = {}

        calls = [line[:line.find('(')] for line in fhand][:-1]

        for call in calls:
            if not id_calls.keys():
                id_calls[call] = 0
            elif call in id_calls.keys():
                continue
            else:
                id_calls[call] = max(id_calls.values()) + 1

        with open(idx_file + '.idx', 'w') as output:
            for idx in range(len(calls) - 1):
                output.write(
                    calls[idx] + "," + str(id_calls[calls[idx]]) + "\n")

            output.write(
                calls[-1] + "," + str(id_calls[calls[-1]]))

        return idx_file, list(range(max(id_calls.values()) + 1))

def ngram_score(base_model, test_model):
    """
    Calcula o score de similaridade entre ngrams ente o
    arquivo de teste e o modelo base.
    """
    with open(base_model, 'r') as f1:
        with open(test_model, 'r') as f2:
            base = f1.read().split()
            test = f2.read().split()

            upper_b = len(base)
            count = 0

            for x, y in zip(base, test):
                x = "".join(x.split(','))
                y = "".join(y.split(','))

                if x == y:
                    continue
                else:
                    count +=1

            return count / upper_b

if __name__ == "__main__":
    # Gera o arquivo com cada syscall e seu id
    syscall_id()

    # Extrai somente os ids do arquivo de syscall para gerar os ngrams
    call_id = extract_calls_id('data/ls_syscall.idx')

    # Gera os ngrams com uma janela de tamanho 10
    grams = ngram_sequence(call_id, 10)

    # Gera um arquivo em estilo csv contendo todos os ngrams
    output_gram('data/ls_syscall', grams)

    # Imprime o valor do método ngram_score que determina o escore
    # da diferença de ngrams entre dois arquivos .gram fornecidos
    print(
        "Score: " + str(ngram_score('data/ls_syscall.gram', 'data/test.gram')))
