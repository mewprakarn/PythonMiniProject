def confusion_matrix2(y_true,y_predict):
    from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score
    
    plt.figure(figsize = (4,3))
    sns.heatmap(confusion_matrix(y_true, y_predict), annot=True)
    plt.xlabel('Predict')
    plt.ylabel('True')
    plt.show()
    
    print('Model Evaluation Metrics')
    print('-'*50)
    print('Accuracy: ',accuracy_score(y_true,y_predict))
    print('Precision: ',precision_score(y_true,y_predict))
    print('Recall: ',recall_score(y_true,y_predict))
    print('f1-score: ',f1_score(y_true,y_predict))
    print('-'*50)
