## Phân loại

### MNIST ( Thư viện tiêu chuẩn)
 -- Nó bao gồm 70.000 bộ dữ liệu trong đó có 60.000 bộ dữ liệu để train  10.000 bộ dữ liệu test
 ### Training a Binary Classier(Đào tạo lớp nhị phân)
Stochastic Gradient Descent (SGD), sử dụng lớp SGDClassifier Scikit-Learn.
Lợi thế của trình phân loại là có khả năng làm với tập dữ liệu lớn một cách hiệu quả 
```
from sklearn.linear_model import SGDClassifier
```
** Nếu bạn muốn các kết quả có thể lặp lại bạn hãy sử dụng prammeter `random_state`
### Performance Measures (Các biện pháp thực hiện)
Đánh giá một bộ phân loại thường khó hơn đánh giá một bộ hồi quy.

### Measuring Accuracy Using Cross-Validation ( Đo lường chính xác bằng cách sử dụng xác nhận chéo)
```
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
```
lớp StratifiedKFold thực hiện lấy mẫu phân tầng để tạo các nếp gấp có chứa tỉ lệ đại diện của mỗi lớp. ở mỗi lần lặp , mã tạo ra một bản sao của trình phân loại các. Đếm số lượng dự đoán chính xác và đưa ra tỉ lệ dự đoán đúng

 Sử dụng K_fold chéo xác nhận có nghĩa là chia tập huấn luyện thành các nếp gấn K sau đó đưa ra dự đoán  và đánh giá chúng trên mỗi nếu gấp 
 ```
 skfolds = StratifiedKFold(n_splits=3, random_state=42)
 ```
 ### Confusion Matrix( Ma trận hỗi loạn )
 Một cách tốt hơn để đánh giá hiệu suất của trình phân loại là xem xsrt ma trận. Ý tưởng chung là đếm số lần thể hiện của lớp A được phân loại vào lớp B. Bạn có thể đưa ra dự đoán về bộ thử nghiệm, Thay vào đó bạn có thể sử dụng hàm `cross_val_predict ()`
 ```
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
 ```
Giống như hàm  `cross_val_score()` cross_val_predict() thực hiện các thực chéo K-fold nhưng thay vì trả về điểm đánh giá,nó trả về dự đoán được trên mỗi lần kiểm tra
Sử dụng hàm confusion_matrix
```
from sklearn.metrics import confusion_matrix
confusion_matrix(y_train_5, y_train_pred)
```

### Precision and Recall (Chính xác và thu hồi)
Scikit-learn cung cấp một số chức năng để tính toán các số liệu phân loại bao gồm độ chính xác và thu hồi :
```
from sklearn.metrics import precision_score, 
precision_score(y_train_5, y_train_pred)
recall_score(y_train_5, y_train_pred) 
```
Với mỗi cách xác định một lớp là positive,   
Precison được định nghĩa là tỉ lệ số điểm true Positive trong những điểm được phân loại là positive (TP+FP).  
Recall được định nghĩa là tỉ lệ số điểm true Positive trong số những điểm thực sự là positive(TP+FN)
Precison và Recall là hai phân số có tử số bằng nhau và mẫu số khác nhau 
```
Precison = TP/(TP+FP)
Recall = TP/(TP+FN)
```
Để tính toán F1_score chỉ cần gọi hàm f1_score()
```
from sklearn.metrics import f1_score
f1_score(y_train_5, y_train_pred)
```
công thức tính   
```
2/F1 = 1/Precision + 1/Recall   
hay   
F1 = 2*(1/(1/Precision +1/Recall)) = 2*(precision*recall)/(precision+recall)
```
F1 càng cao, bộ phân lớp càng tốt . Khi cả recall và precision đều bằng 1 

### Precision/Recall Tradeoff

Scikit - Learn ko cho phép bạn đặt ngưỡng trực tiếp mà thay vào đó bạn truy cập đến điểm số quyết định mà nó sử dụng để đưa ra dự đoán, thay vì phương thức dự đoán phân loại, bạn có thể gọi phương thức quyết định của nó phương thức này trả về điểm cho từng trường hợp và sau đó đưa ra dự đoán trên các điểm đó bằng cách sử dụng ngưỡng phù hợp

- Tính toán 
```
y_scores = sgd_clf.decision_function([some_digit])
```
- sử dujung ngưỡng để đưa ra dự đoán trên các điểm
```
threshold = 800
y_some_digit_pred = (y_scores > threshold)
```
Kết quả trả về True hoặc False
### Multiclass Classification
Sử dụng nhiều trong các bài toán   `Random Forest classifiers or naive Bayes classifiers ` .Có nhiều chiến lược khác nhau mà bạn có thể sử dụng để thức hiện phân loại đa lớp bằng nhiều phân loại nhị phân
### Multilabel Classification
trong trường hợp, bạn muốn trình phân loại của mình xuất ra nhiều lớp cho mỗi phiên bản.

### Multiouput Classification
