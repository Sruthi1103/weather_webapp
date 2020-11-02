import base64
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io
from io import BytesIO
import requests
from flask import Flask, render_template, request
import pyowm
from markupsafe import Markup

app = Flask(__name__)
app.config['DEBUG'] = True
#owm = pyowm.OWM('180871ba8ac01707f015640feeb40718')
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []

    if request.method == 'POST':
        new_city = request.form.get('city')

        degree_sign = u'\N{DEGREE SIGN}'
        """url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

        #r = requests.get(url.format(new_city)).json()
        # print(r);

        # Three Hours Forecast
        mgr = owm.weather_manager()
        forecaster = mgr.forecast_at_place(new_city, '3h')
        forecast = forecaster.forecast
        weather_list = forecast.weathers[0:5]

        w = []
        performance = []
        for weather in weather_list:
            temp = weather.temperature(unit='fahrenheit')['temp']
            #print(weather.reference_time('iso'), f'Temperature: {temp}{degree_sign}F')
            performance.append(temp)
            w.append(str(temp) + degree_sign)

        #line graph------------------------------------------------------------------------
        plt.rcdefaults()
        plt.plot(w,performance)
        plt.title('3 hour weather forecast')
        plt.xlabel('days')
        plt.ylabel('Temperature')
        plt.tight_layout()
        img1 = io.BytesIO()
        plt.savefig(img1, format='png')
        img1.seek(0)
        plot_url1 = base64.b64encode(img1.getvalue()).decode();
        model_plot1 = Markup('<img src="data:image1/png;base64,{}" width: 360px; height:288px>'.format(plot_url1))


        plt.clf()

        plt.rcdefaults()
        y_pos = np.arange(len(w))

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, w, fontsize=8)
        plt.ylabel('Temperature')
        plt.title('3 hour weather forecast')
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img,format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode();
        model_plot=Markup('<img src="data:image/png;base64,{}" width: 360px; height:288px>'.format(plot_url))
        plt.clf()
        """
        weather = {
            #'city': new_city,
            #'temperature': r['main']['temp'],
            #'description': r['weather'][0]['description'],
            #'icon': r['weather'][0]['icon'],
            #'pressure': r['main']['pressure'],
            #'humidity': r['main']['pressure'],
            #'visibility': r['visibility'],
            #'model_plot':model_plot,
            #'model_plot1': model_plot1,
            'model_plot':"hello",
            'model_plot1':"hello2",

        }

        weather_data.append(weather)
    return render_template('weather.html', weather_data=weather_data)

if __name__=="__main__":
    app.run()