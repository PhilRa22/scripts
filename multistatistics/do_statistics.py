
from os.path import join, exists
import pandas as pd
from multistatistics.lda import calc_lda
from multistatistics.pca import calc_pca
from multistatistics.statistics import get_statistics
import os


def do_statistics(properties, statistic=True, pca=True, lda=True):
    # preparing result.csv for statistics
    file_path = join(
        os.getenv("DATA_PATH"), 'results', 'results.csv')
    if not exists(file_path):
        print('no results available, please run read files from main')
    else:
        features, infos = prepare_data(file_path)
        if statistic:  # simple statistics
            get_statistics(features, infos)
        if pca:
              calc_pca(features, infos, properties)
        if lda:
            calc_lda(features, infos, properties)


def prepare_data(file_path):
    df = pd.read_csv(file_path, delimiter=';', decimal=',')
    df.fillna(0)  # features without values filled with 0.
    info_cols = ['datetime',
                 'height',
                 'number',
                 'rate',
                 'sample',
                 'name']
    infos = df[info_cols]
    features = df.drop(columns=info_cols)
    features.index = infos['name']
    return features, infos


if __name__ == '__main__':
    path = 'E:\\Promotion\Daten\\29.06.21_Paper_reduziert'
    do_statistics(path)
