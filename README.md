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

### 3. Language Model Evaluation (LM-Eval-Harness)

[GPT-Neo MMLU 벤치마킹 결과](evaluation/excel/EleutherAI__gpt-neo-125M/output.xlsx)  
GPT-Neo 모델의 성능을 평가하기 위해 **MMLU (Massive Multitask Language Understanding) 데이터셋**을 사용하여 벤치마킹을 진행하였습니다.

#### 평가 방법
- **평가 도구:** [`lm-eval-harness`](https://github.com/EleutherAI/lm-evaluation-harness)  
- **모델:** GPT-Neo-125M (Hugging Face `EleutherAI/gpt-neo-125M`)  
- **데이터셋:** MMLU (Massive Multitask Language Understanding)  
- **실행 환경:** CPU  
- **평가 명령어:**
  ```bash
  lm-eval --model hf \
  --model_args pretrained=EleutherAI/gpt-neo-125M \
  --tasks mmlu \
  --device cpu \
  --output_path evaluation/lm_eval_harness/EleutherAI__gpt-neo-125M/results.json
  ```

#### 평가 결과 요약
- **전체 정확도(Accuracy):** `23.13%`
- **세부 평가 결과:**  
  - **인문학 (Humanities):** `24.34%`
  - **논리학 (Formal Logic):** `28.57%`
  - **고등학교 유럽사 (High School European History):** `24.24%`
  - **기타 영역 (Other Subjects):** `24.11%`
  - **사회과학 (Social Sciences):** `22.00%`
  - **STEM 분야:** `21.47%`

**자세한 평가 결과는 [엑셀 파일](evaluation/excel/EleutherAI__gpt-neo-125M/output.xlsx)에서 확인 가능**

### 4. Multimodal Inference with LLaVA

[멀티모달 추론 실습 노트북](notebooks/kt_ku_llava_demo.ipynb)  
LLaVA 1.5 기반 멀티모달 추론 실습 코드입니다.

#### 주요 내용:
- Hugging Face Transformers와 BitsAndBytes를 활용하여 LLaVA 1.5 모델 로딩
- 이미지 + 텍스트를 입력으로 받아 시각 정보를 활용한 질의응답 수행
- `generate()` 방식과 `pipeline()` 방식 두 가지 모두 실습
- 모델 추론 시 `<image>` 토큰을 활용한 멀티모달 입력 처리

이 실습은 Colab에서 GPU 환경에서 진행한 코드입니다.

### 5. Retriever Evaluation

[리트리버 평가 실습 코드](notebooks/kt_ku_retriever_eval_demo.py)  
LangChain 기반의 리트리버 평가 실습 코드입니다.

#### 주요 내용:
- **BM25Retriever + FAISSRetriever**를 조합한 EnsembleRetriever 구성
- 쿼리-문서 매핑에 대한 gold label 기준 recall, precision, F1 점수 평가
- `sklearn.metrics`를 활용한 수치 계산
- 소규모 테스트 문서를 활용한 빠른 실습 가능

📌 `EnsembleRetriever`는 각각의 리트리버에 가중치를 부여하여 검색 성능을 조합적으로 향상시키는 구조입니다.