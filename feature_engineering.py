# encoding=utf-8
'''
用sklearn做特征工程，分为三部分：
1.数据预处理
2.特征选择
3.降维
'''

import pandas as pd
import numpy as np
from numpy import vstack, array, nan
from sklearn.datasets import load_iris
from sklearn import preprocessing

if __name__ == '__main__':

    # 导入IRIS数据集
    iris = load_iris()
    features = iris.data
    labels = iris.target

    '''
    1.数据预处理
    '''

    # 1.1 无量纲化：将不同规格的数据转换到同一规格
    # 1.1.1 标准化：将服从正态分布的特征值转换成标准正态分布（对列向量处理）
    # print(np.mean(features, axis=0))
    # print(np.std(features, axis=0))
    features_new = preprocessing.StandardScaler().fit_transform(features)
    # print(np.mean(features_new, axis=0))
    # print(np.std(features_new, axis=0))
    # 1.1.2 区间缩放：将特征值缩放到[0, 1]区间的数据（对列向量处理）
    features_new = preprocessing.MinMaxScaler().fit_transform(features)
    # print(features_new)
    # 1.1.3 归一化：将行向量转化为“单位向量”（对每个样本处理）
    features_new = preprocessing.Normalizer().fit_transform(features)
    # print(features_new)

    # 1.2 对定量特征二值化:设定一个阈值，大于阈值的赋值为1，小于等于阈值的赋值为0
    # print(features)
    features_new = preprocessing.Binarizer(threshold=3).fit_transform(features)
    # print(features_new)

    # 1.3 对定性（分类）特征编码
    enc = preprocessing.OneHotEncoder()
    enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
    # print(enc.transform([[0, 1, 3]]))
    # print(enc.transform([[0, 1, 3]]).toarray())

    # 1.4 缺失值计算
    # print(features)
    imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
    features_new = imp.fit_transform(vstack((array([nan, nan, nan, nan]), features)))
    # print(features_new)