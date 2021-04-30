from util.jieba_test import paddle_cut, correct_cut, full_cut
from concurrent.futures import ThreadPoolExecutor


def main():
    datas = ["NIKON D780 單機身 公司貨",
             "3M 瞬涼5度抑螨可水洗烘乾涼夏兩用被-星空藍(180x210cm)",
             "【madd capp】I AM 拼圖 我是小熊貓 - 100 系列 極限逼真動物 不規則切邊 適合多人挑戰"]
    with ThreadPoolExecutor(max_workers=10) as executor:
        for data in datas:
            executor.map(lambda x: print(correct_cut(x)), (data,))
            print(data)


if __name__ == "__main__":
    main()



