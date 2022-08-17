

class Prediction:
    
    
    def getPrediction(self, pclass, sex, age, sibsp, parch, fare, C, Q, S):
        import pickle
        model = pickle.load(open("ml_app/titanic_survival_ml_model.sav", "rb"))
        scaled = pickle.load(open("ml_app/scaler.sav", "rb"))
        prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
        
        if prediction == 0:
            return "not survived"
        elif prediction == 1:
            return "survived"
        else:
            return "error"