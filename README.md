## 프로젝트 목표
+ 내가 선호하는 와인과 비슷한 와인을 추천하는 모델 개발



## Data
+ [Kaggle의 wine데이터](https://www.kaggle.com/datasets/samuelmcguire/wine-reviews-data)
+ 원본 데이터셋 (323237, 10)
+ 전처리
  + drop_duplicates(), 결측치 확인
  + price, alcohol : object => float 형변환, 결측치를 median값으로 대체
  + alcohol : outlier(25 이상) 삭제
  + category : 'Fortified', 'Port/Sherry'는 한 클래스로 병합
  + appelltion : 국가 및 하위지역들로 split해 새로운 feature에 저장
+ 최종 데이터셋 (323065, 16)



## Model
+ KModes 모델 이용
+ 클러스터링에 사용할 feature들만 선택 (wine, appellation, rating, reviwer, review는 이후 추천 시스템에서 활용)
![elbow_method_for_optimal_k](https://user-images.githubusercontent.com/88722429/170510089-5a4eff65-58a6-4d28-9bb4-bbaecadbbe5e.png)
+ n_clusters=100, n_init=5, init='random'
+ 클러스터링 결과(1~100)를 Data에 추가, appellation 관련 새로 만든 feature들 drop  
  => 추천 시스템에서 사용할 데이터셋 (323065, 12)  



