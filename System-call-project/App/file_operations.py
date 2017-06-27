import glob


def ngram_sequence(data, window_size):
    """
    Gera todas as sequencias de ngramn a partir dos dados das syscall.
    @return:
    """
    grams = []

    for idx in range((len(data) + 1 - window_size)):
        grams.append([data[i] for i in range(idx, idx + window_size)])

    return grams


def extract_calls_id(file_name):
    """
    Extrai a sequencia de id nos arquivos .idx.
    :return array of strings of numbers
    """
    with open(file_name, 'r') as input_data:
        r_data = input_data.read().split()
        return ([d.split(',')[1] for d in r_data])


def output_gram(file_name, grams):
    """
    Gera os arquivos .gram a partir da lista de grams fornecida.
    """
    with open(file_name, 'w') as output:
        for idx in range(len(grams) - 1):
            # data = [str(value) for value in grams[idx]]
            # data = ",".join(data)
            output.write(grams[idx] + "\n")

        # data = [value for value in grams[-1]]
        # data = ",".join(data)
        output.write(grams[-1])


def syscall_id(syscall_file):
    """
    Gera os arquivos csv .idx contendo cada syscall e seu id a partir
    dos arquivos .log presentes no diretorio de trabalho.
    """

    with open(syscall_file, 'r') as fhand:
        idx_file = syscall_file[:syscall_file.rfind('.')] + '.idx'

        id_calls = {}

        calls = [line[:line.find('(')] for line in fhand]

        if calls[-1][0] == '+':
            calls = calls[:-1]

        for call in calls:
            if not id_calls.keys():
                id_calls[call] = 0
            elif call in id_calls.keys():
                continue
            else:
                id_calls[call] = max(id_calls.values()) + 1

        with open(idx_file, 'w') as output:
            for idx in range(len(calls) - 1):
                output.write(
                    calls[idx] + "," + str(id_calls[calls[idx]]) + "\n")

            output.write(
                calls[-1] + "," + str(id_calls[calls[-1]]))

        return idx_file, sorted(list(id_calls.values()))


def reformat_input(file_name):
    file_id = file_name[:file_name.rfind('.')]

    with open(file_name, 'r') as fhand:
        with open(file_id+".log", 'w') as log:
            for line in fhand:
                line = line[line.find('[')+1:]
                line = line[line.find(']')+1:]

                log.write(line)


def ngram_score_file(base_model, test_model):
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