import pandas as pd


def main():
    data = pd.read_csv("./gender2.csv", encoding="cp949", index_col=0)

    ncol = data[["2022년_계_총인구수", "2022년_남_총인구수", "2022년_여_총인구수"]]
    ncol.columns = ["Total", "Male", "Female"]
    print(ncol)


if __name__ == "__main__":
    main()
