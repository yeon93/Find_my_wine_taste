# 와인 추천 프로젝트
내가 선호하는 와인과 비슷한 와인을 추천하는 모델 개발



## 프로젝트 기획 배경
와인에 입문하면서 느꼈던 진입장벽
+ 섬세한 취향에 따라 선택할 수 있는 매우 다양한 종류가 있으므로, 구글링을 통한 검색에도 한계가 있음
+ 보통 판매처에서 제공되는 간단한 정보(dry-wet, bitter-sweet의 정도, 가격 등)만을 바탕으로 와인을 선택하는 경우가 많음 
> '예전에 xx와인 마셔봤을 때 맛있던데, 그거랑 비슷한 다른 와인 또 없나?'  
 
=>특정 와인에 대한 특성을 입력하면 그와 유사한 와인을 평점 순으로 추천해주는 서비스 개발



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
+ 데이터의 특성당 범주가 매우 많아 모두 인코딩하기가 어려움  
 => 범주형 자료에 바로 적용가능한 클러스터링 모델인 KModes 이용
+ 클러스터링 학습에 사용할 feature들만 선택 (wine, appellation, rating, reviwer, review는 이후 추천 시스템에서 활용)
![elbow_method_for_optimal_k](https://user-images.githubusercontent.com/88722429/170510089-5a4eff65-58a6-4d28-9bb4-bbaecadbbe5e.png)
+ n_clusters=100, n_init=5, init='random'
+ 클러스터링 결과(1~100)를 Data에 추가, appellation 관련 새로 만든 feature들 drop  
  => 추천 시스템에서 사용할 데이터셋 (323065, 12)  



## 문제점
모든 데이터를 100개의 클러스터로 나누는 데에는 성공했으나,   
이를 학습한 모델을 이용해 새로운 와인 데이터를 예측하면 항상 같은 클러스터로 예상함  
=> 예측에는 KModes가 아닌 새로운 알고리즘을 이용해야 함  



## 더 진행해야 할 점
+ KModes를 통한 클러스터 정보를 이용한 예측 위한 알고리즘 만들기
+ 추천 와인의 정보(wine, appellation, rating, reviwer, review 포함)를 return하는 클래스 만들기
