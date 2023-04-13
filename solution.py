import pandas as pd
import numpy as np
import scipy.stats


chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = scipy.stats.ttest_ind(x, y, alternative='less')[1]
    p = 0.03
    if a <= p:
      return True
    else:
      return False
