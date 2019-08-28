import pandas as pd
from pathlib import Path

def csv_to_tsv(input_file, output_file):
    df = pd.read_csv(input_file,  sep='\t')
    print(df.columns)

    #df.to_csv(output_file, sep='\t', header=None)


if __name__ == "__main__":
    root = Path('../hedwig-data/datasets/personality/')


    for s in ['train', 'val', 'test']:
        csv_to_tsv(root / f'{s}.tsv', root / f'{s}.tsv')
