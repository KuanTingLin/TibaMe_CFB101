# encoding=utf-8
import jieba
import time
import jieba.analyse
from functools import wraps


def time_count_wrapper(func):
    @wraps(func)
    def time_count(*args, **kw):
        start = time.time()
        return_value = func(*args, **kw)
        end = time.time()
        time_diff = end - start
        print("time consume: {} sec".format(time_diff))
        return return_value

    return time_count


@time_count_wrapper
def paddle_cut(data):
    seg_list = jieba.cut(data, use_paddle=True)
    return list(seg_list)


@time_count_wrapper
def search_cut(data):
    seg_list = jieba.cut_for_search(data)
    return list(seg_list)


@time_count_wrapper
def full_cut(data):
    seg_list = jieba.cut(data, cut_all=True)
    return list(seg_list)


@time_count_wrapper
def correct_cut(data):
    seg_list = jieba.cut(data, cut_all=False)
    return list(seg_list)


@time_count_wrapper
def tfidf_cut(data):
    seg_list = jieba.analyse.extract_tags(data, topK=5, withWeight=True)
    return seg_list


def main():
    datas = ["NIKON D780 單機身 公司貨", "3M 瞬涼5度抑螨可水洗烘乾涼夏兩用被-星空藍(180x210cm)"]
    for data in datas:
        print("full: ", full_cut(data))
        print("correct: ", correct_cut(data))
        print("search: ", search_cut(data))
        print("paddle: ", paddle_cut(data))
        print("TFIDF: ", tfidf_cut(data))


if __name__ == '__main__':
    jieba.enable_paddle()
    main()

