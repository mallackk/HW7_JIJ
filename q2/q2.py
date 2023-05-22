import numpy as np


def main():
    docs = np.array([[1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0]])
    query = np.array([1, 1, 0, 0, 1, 0])

    # 문서와 질의의 내적을 계산
    dot_product = np.dot(docs, query)

    # 문서와 질의의 크기(노름)을 계산
    docs_norm = np.linalg.norm(docs, axis=1)
    query_norm = np.linalg.norm(query)

    # 코사인 유사도를 계산
    cos_similarities = dot_product / (docs_norm * query_norm)

    # 결과를 소수점 둘째자리까지 출력
    doc1 = round(cos_similarities[0], 2)
    doc2 = round(cos_similarities[1], 2)
    doc3 = round(cos_similarities[2], 2)

    print(f"doc1 = ", doc1)
    print(f"doc2 = ", doc2)
    print(f"doc3 = ", doc3)


if __name__ == "__main__":
    main()
