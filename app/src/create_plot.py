import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_predictions(predictions) -> go.Figure:

    figure=make_subplots(specs=[[{"secondary_y": True}]])

    figure.add_trace(
        go.Scatter(
            x=predictions["Datetime"],
            y=predictions["COMED_MW_scaled"],
            mode="lines",
            name="Actual",
            line=dict(color="blue", width=2)
        ),
        secondary_y=False
    )

    figure.add_trace(
        go.Scatter(
                x=predictions["Datetime"],
                y=predictions["Predictions"],
                mode="lines",
                name="Predicted",
                line=dict(color="red", dash="dot", width=2)
        ),
        secondary_y=False
    )

    holiday_dates=predictions[predictions["Holiday_encoded"]==1]["Datetime"]
    figure.add_trace(
        go.Scatter(
            x=holiday_dates,
            y=[predictions["COMED_MW_scaled"].max()]*len(holiday_dates),
            mode="markers", 
            marker=dict(color="green", size=10, symbol="star"),
            name="Holiday"
        ),
        secondary_y=False
    )

    season_changes=predictions[predictions["Season_encoded"].diff().abs()>0]["Datetime"]

    for season_change in season_changes:
        figure.add_shape(
            type="line",
            x0=season_change,
            x1=season_change,
            y0=0,
            y1=1,
            xref="x",
            yref="paper",
            line=dict(color="purple", dash="dash")
        )

    figure.update_layout(
        title="Time Series Forecasting of Electricity Demand",
        xaxis_title="Datetime",
        yaxis_title="Scaled Electricity Demand (MW)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255, 255, 255, 0.5)"
        ),
        template="plotly_white",
        title_font=dict(size=24, family="Arial"),
        font=dict(size=12, family="Arial"),
        hovermode="x unified"
    )

    figure.update_xaxes(
        rangeslider_visible=True,
        tickformat="%b %d\n%Y",
        title_font=dict(size=18, family="Arial"),
        tickfont=dict(size=12, family="Arial")
    )

    figure.update_yaxes(
        title_font=dict(size=18, family="Arial"),
        tickfont=dict(size=12, family="Arial")
    )

    return figure