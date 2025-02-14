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

## **3. Language Model Evaluation (LM-Eval-Harness)**
[GPT-Neo MMLU 벤치마킹 결과](evaluation/excel/EleutherAI__gpt-neo-125M/output.xlsx)  
GPT-Neo 모델의 성능을 평가하기 위해 **MMLU (Massive Multitask Language Understanding) 데이터셋**을 사용하여 벤치마킹을 진행하였습니다.

### **평가 방법**
- **평가 도구:** [`lm-eval-harness`](https://github.com/EleutherAI/lm-evaluation-harness)  
- **모델:** GPT-Neo-125M (Hugging Face `EleutherAI/gpt-neo-125M`)  
- **데이터셋:** MMLU (Massive Multitask Language Understanding)  
- **실행 환경:** CPU  
- **평가 명령어:**
  ```bash
  lm-eval --model hf --model_args pretrained=EleutherAI/gpt-neo-125M --tasks mmlu --device cpu --output_path evaluation/lm_eval_harness/EleutherAI__gpt-neo-125M/results.json
  ```

### **평가 결과 요약**
- **전체 정확도(Accuracy):** `23.13%`
- **세부 평가 결과:**  
  - **인문학 (Humanities):** `24.34%`
  - **논리학 (Formal Logic):** `28.57%`
  - **고등학교 유럽사 (High School European History):** `24.24%`
  - **기타 영역 (Other Subjects):** `24.11%`
  - **사회과학 (Social Sciences):** `22.00%`
  - **STEM 분야:** `21.47%`

📄 **자세한 평가 결과는 [엑셀 파일](evaluation/excel/EleutherAI__gpt-neo-125M/output.xlsx)에서 확인 가능**  
