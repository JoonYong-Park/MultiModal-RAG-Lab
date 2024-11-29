# MultiModal-RAG-Lab

### 1. MultiVector Retriever

[멀티벡터 스토어 작업 파일](notebooks/multivector_retriever.ipynb)  
멀티벡터 스토어를 사용하여 문서당 여러 벡터를 생성하고 효율적으로 검색하는 방법을 실습한 코드입니다.

#### 문서당 여러 벡터를 생성하는 방법:

1. **더 작은 청크(Smaller chunks)**  
   문서를 더 작은 청크로 나누고, 그것들을 임베딩합니다 (ParentDocumentRetriever를 활용).

2. **요약(Summary)**  
   각 문서에 대한 요약을 생성하고, 그것을 문서와 함께(또는 문서 대신) 임베딩합니다.

3. **가상 질문(Hypothetical questions)**  
   각 문서가 적절하게 답변할 수 있는 가상 질문(hypothetical questions)을 생성하고, 그것들을 문서와 함께(또는 문서 대신) 임베딩합니다.
