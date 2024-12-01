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

### 2. Semi-structured RAG

[반구조화된 RAG 작업 파일](notebooks/semi_structed_RAG.ipynb)  
반구조화된 데이터를 처리하여 RAG 시스템을 구축하는 방법을 실습한 코드입니다.

#### 반구조적 데이터를 처리하는 방법:

1. **텍스트와 표 파싱**

   - [Unstructured.io](https://unstructured.io/)를 사용하여 PDF에서 텍스트와 표를 모두 추출합니다.

2. **MultiVectorRetriever 구성**

   - 원본 표, 텍스트와 함께 요약된 표를 저장하여 효율적으로 검색합니다.

3. **체인 구현**
   - LCEL(LangChain Execution Layer)을 사용하여 검색 및 처리를 자동화합니다.
