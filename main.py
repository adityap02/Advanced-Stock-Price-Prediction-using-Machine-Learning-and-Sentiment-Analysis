import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
# import tk as tk
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import pandas_datareader as web
import math

from tensorflow.keras.models import load_model
import warnings

warnings.filterwarnings("ignore")
import tkinter as tk

app = tk.Tk()

HEIGHT = 700
WIDTH = 600


def execute(ticker):
    def scale_training_data(data_training):
        data_training = scaler.fit_transform(data_training)
        return data_training

    # data_training = scale_training_data(data_training)

    def prep_training_data(data_training):
        X_train = []
        y_train = []

        for i in range(60, data_training.shape[0]):
            X_train.append(data_training[i - 60:i])
            y_train.append(data_training[i, 3])

        X_train, y_train = np.array(X_train), np.array(y_train)
        return X_train, y_train

    # X_train,y_train = prep_training_data(data_training)

    def build_model():
        model = Sequential()

        model.add(LSTM(units=60, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 5)))
        model.add(Dropout(0.2))

        model.add(LSTM(units=60, activation='relu', return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=80, activation='relu', return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=120, activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    # model = load_model(module)
    # model = build_model()

    def train_model(model, X_train, y_train):
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
        trainScore = model.evaluate(X_train, y_train, verbose=0)
        print('MSE :', trainScore)
        print('RMSE : ', math.sqrt(trainScore))
        return model

    # model = train_model(model,X_train,y_train)

    def prep_test_data(data_training_copy, data_test):
        past_60_days = data_training_copy.tail(60)
        df = past_60_days.append(data_test, ignore_index=True)
        df = df.drop(['Date', 'Adj Close'], axis=1)
        inputs = scaler.fit_transform(df)

        X_test = []
        y_test = []

        for i in range(60, inputs.shape[0]):
            X_test.append(inputs[i - 60:i])
            y_test.append(inputs[i, 3])

        X_test, y_test = np.array(X_test), np.array(y_test)
        return X_test, y_test

    # X_test,y_test = prep_test_data(data_training_copy,data_test)

    def make_prediction(X_test, y_test):
        y_pred = model.predict(X_test)
        testScore = model.evaluate(X_test, y_test, verbose=0)
        print("MSE :", testScore)
        return y_pred

    # y_pred = make_prediction(X_test,y_test)

    def inverse_scale(data_test, y_test):
        last_y = data_test.tail()
        last_y = last_y.filter(['Close'])
        last_y = last_y.values.tolist()
        last_y[-1]
        scale2 = last_y[-1] / y_test[-1]
        scale2 = scale2[0]
        return scale2

    # y_pred = inverse_scale(y_pred)
    # y_test = inverse_scale(y_test)

    def plot_results():
        plt.figure(figsize=(7, 5))

        plt.plot(y_test, color='red', label='Real Stock Price')
        plt.plot(y_pred, color='blue', label='Predicted Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel(' Stock Price')
        plt.legend()
        plt.show()

    def sent_analysis(file):
        data = pd.read_csv(file)
        data = data.iloc[:, -1]
        # print(data)
        pos_count = 0
        neg_count = 0
        data = data.values.tolist()
        length = len(data)
        for i in range(length):
            if (data[i] == 'pos'):
                pos_count = pos_count + 1
            elif (data[i] == 'neg'):
                neg_count = neg_count + 1
        result_2 = "============================= \n"
        result_3 = "sentiment analysis of tweets \n "
        result_4 = "No of tweets classified as positive: " + str(pos_count) + "\n"
        result_5 = "No of tweets classified as negative: " + str(neg_count) + "\n"
        pos_percentage = pos_count * 100 / (neg_count + pos_count)
        neg_percentage = neg_count * 100 / (neg_count + pos_count)
        result_6 = "positive percentage: " + str(pos_percentage) + "\n"
        result_7 = "negative percentage: " + str(neg_percentage) + "\n"
        result_8 = "=============================="

        results_1['text'] = result_2 + result_3 + result_4 + result_5 + result_6 + result_7 + result_8
        return pos_percentage, neg_percentage

    def recommend_rating(data_test, pos_percentage, neg_percentage, final_y):
        y = data_test.filter(['Close'])
        y = y.values.tolist()
        yy = []
        for i in range(len(y)):
            yy.append(y[i][0])
        yy = yy[::-1]
        weekly_avg1 = mean(yy[0:7])
        weekly_avg2 = mean(yy[7:14])
        weekly_avg3 = mean(yy[14:21])
        monthly_avg1 = mean(yy[0:30])
        monthly_avg2 = mean(yy[30:60])
        monthly_avg3 = mean(yy[60:90])
        '''
        print("avergaes")
        print(weekly_avg1)
        print(weekly_avg2)
        print(weekly_avg3)
        print(monthly_avg1)
        print(monthly_avg2)
        print(monthly_avg3)
        '''
        star = 0
        if (weekly_avg1 >= weekly_avg2 >= weekly_avg3):
            star = star + 1

        if (monthly_avg1 >= monthly_avg2 or monthly_avg1 >= monthly_avg3):
            star = star + 1

        if (pos_percentage > neg_percentage):
            star = star + 1
        if (pos_percentage > 75):
            star = star + 1
        if (final_y > weekly_avg1):
            star = star + 1
        return star

    price_history = 'Price_History/' + ticker + ".csv"
    data = web.DataReader(ticker, data_source='yahoo', start='2004-01-01', end='2020-05-24')
    data.to_csv(price_history)
    data = pd.read_csv(price_history, date_parser=True)

    # splitting into training and testing
    data_training = data_training_copy = data[data['Date'] < '2019-04-01'].copy()
    data_test = data[data['Date'] >= '2019-04-01'].copy()

    data_training = data_training.drop(['Date', 'Adj Close'], axis=1)
    scaler = MinMaxScaler()
    module = ticker + '.h5'
    data_training = scale_training_data(data_training)
    X_train, y_train = prep_training_data(data_training)
    h5file = 'models/' + module
    model = load_model(h5file)
    # model = build_model()
    # model = train_model(model,X_train,y_train)
    X_test, y_test = prep_test_data(data_training_copy, data_test)
    y_pred = make_prediction(X_test, y_test)
    scale2 = inverse_scale(data_test, y_test)
    y_pred = y_pred * scale2
    y_test = y_test * scale2
    final_y = y_pred[-1]

    result_1 = "Predicted price for the next day is:  " + str(final_y)

    results['text'] = result_1

    sentimentsfile = 'sentiments/' + ticker + "_sentiment.csv"

    pos_percentage, neg_percentage = sent_analysis(sentimentsfile)
    star = recommend_rating(data_test, pos_percentage, neg_percentage, final_y)
    rating = '*' * star
    final_rating = "Recommendation based on Star rating ( out of 5 ) is :  ", rating
    results_2['text'] = final_rating
    plot_results()


C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image = tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

frame = tk.Frame(app, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# frame_window = C.create_window(100, 40, window=frame)

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Prediction', font=40, command=lambda: execute(textbox.get()))
# submit.config(font=)
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

lower_frame_1 = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame_1.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.35, anchor='n')

bg_color = 'white'
results_1 = tk.Label(lower_frame_1, anchor='nw', justify='left', bd=4)
results_1.config(font=40, bg=bg_color)
results_1.place(relwidth=1, relheight=1)

lower_frame_2 = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame_2.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')

bg_color = 'white'
results_2 = tk.Label(lower_frame_2, anchor='nw', justify='left', bd=4)
results_2.config(font=60, bg=bg_color)
results_2.place(relwidth=1, relheight=1)

app.mainloop()
