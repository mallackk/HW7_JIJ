import pandas as pd


def main():
    data = [[1000, 25], [280, 120], [900, 30]]

    print("--unitPrice & Number--")
    df1 = pd.DataFrame(
        data, index=["store1", "store2", "store3"], columns=["unit price", "number"]
    )
    print(df1)

    print("\n--Add Total Prices--")
    df1["total price"] = df1["unit price"] * df1["number"]
    print(df1)

    print("\n--Top 2 Total Prices--")
    df2 = df1.sort_values(by=["total price"], ascending=False)
    print(df2["total price"][:2])


if __name__ == "__main__":
    main()
