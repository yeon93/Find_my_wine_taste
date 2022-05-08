## 프로젝트 목표
+ 와인 추천 서비스를 제공하는 웹서비스 개발 및 배포
+ 데이터 파이프라인을 구축하는 과정을 혼자 구성해보기
+ 데이터베이스 구축, API 서비스 개발, 대시보드에 데이터 분석 시각화



## Data
+ [Kaggle의 wine데이터](https://www.kaggle.com/datasets/samuelmcguire/wine-reviews-data)
+ 원본 데이터셋 (323237, 10)
+ 전처리
  + drop_duplicates(), 결측치 확인
  + price, alcohol : object => float, 결측치를 median값으로 대체
  + alcohol : outlier(25 이상) 삭제
  + category : 'Fortified', 'Port/Sherry'는 한 클래스로 병합
  + appelltion : 국가 및 하위지역들로 split해 새로운 feature에 저장
+ 최종 데이터셋 (323065, 16)



## Model
+ KModes 모델 이용
+ 클러스터링에 사용할 feature들만 선택 (wine, appellation, rating, reviwer, review는 이후 추천 시스템에서 활용)
+ n_clusters=300, n_init=5, init='random'
+ 클러스터링 결과(1~300 값)를 Data에 추가, appellation 관련 새로 만든 feature들 drop
  => 추천 시스템에서 사용할 데이터셋 (323065, 12)
  => sqlite 데이터베이스에 저장
