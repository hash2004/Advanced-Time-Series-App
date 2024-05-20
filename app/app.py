from src.create_plot import plot_predictions
from flask import (
    Flask,
    render_template,
    request
)
import pandas as pd
import json
import plotly

application=Flask(__name__, template_folder="templates")

def arima_plot() -> str:
    arima_predictions=pd.read_csv(r"data/ARIMA_Predictions.csv")
    arima_predictions=arima_predictions.drop(arima_predictions.columns[0], axis=1)
    arima_predictions["Datetime"]=pd.to_datetime(arima_predictions["Datetime"])
    figure=plot_predictions(predictions=arima_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def sarima_plot() -> str:
    sarima_predictions=pd.read_csv(r"data/SARIMA_Predictions.csv")
    sarima_predictions["Datetime"]=pd.to_datetime(sarima_predictions["Datetime"])
    figure=plot_predictions(predictions=sarima_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def ets_plot() -> str:
    ets_predictions=pd.read_csv(r"data/ETS_Predictions.csv")
    ets_predictions["Datetime"]=pd.to_datetime(ets_predictions["Datetime"])
    figure=plot_predictions(predictions=ets_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def lstm_plot() -> str:
    lstm_predictions=pd.read_csv(r"data/LSTM_Predictions.csv")
    lstm_predictions["Datetime"]=pd.to_datetime(lstm_predictions["Datetime"])
    figure=plot_predictions(predictions=lstm_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def prophet_plot() -> str:
    prophet_predictions=pd.read_csv(r"data/Prophet_Predictions.csv")
    prophet_predictions["Datetime"]=pd.to_datetime(prophet_predictions["Datetime"])
    figure=plot_predictions(predictions=prophet_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def svr_plot() -> str:
    svr_predictions=pd.read_csv(r"data/SVR_Predictions.csv")
    svr_predictions["Datetime"]=pd.to_datetime(svr_predictions["Datetime"])
    figure=plot_predictions(predictions=svr_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def hybrid_plot() -> str:
    hybrid_predictions=pd.read_csv(r"data/Hybrid_Predictions.csv")
    hybrid_predictions["Datetime"]=pd.to_datetime(hybrid_predictions["Datetime"])
    figure=plot_predictions(predictions=hybrid_predictions)
    graphJSON=json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@application.route("/")
def home() -> str:
    return render_template(
        template_name_or_list="home.html"
    )

@application.route("/chart", methods=["GET", "POST"])
def chart() -> str:
    if request.method == "POST":
        model=request.form["model"]
        if model=="ARIMA":
            arima_json=arima_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Autoregressive Integrated Moving Average (ARIMA)",
                graphJSON=arima_json
            )
        if model=="SARIMA":
            sarima_json=sarima_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Seasonal Autoregressive Integrated Moving Average (SARIMA)",
                graphJSON=sarima_json
            )
        if model=="ETS":
            ets_json=ets_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Error-Trend-Seasonality (ETS)",
                graphJSON=ets_json
            )
        if model=="LSTM":
            lstm_json=lstm_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Long Short-Term Memory (LSTM)",
                graphJSON=lstm_json
            )
        if model=="Prophet":
            prophet_json=prophet_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Prophet",
                graphJSON=prophet_json
            )
        if model=="SVR":
            svr_json=svr_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Support Vector Regression (SVR)",
                graphJSON=svr_json
            )
        if model=="Hybrid":
            hybrid_json=hybrid_plot()
            return render_template(
                template_name_or_list="chart.html",
                heading="Hybrid",
                graphJSON=hybrid_json
            )
    return render_template(
        template_name_or_list="chart.html"
    )

if __name__=="__main__":
    application.run(
        debug=True,
        port=5001
    )