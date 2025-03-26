from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd
import json
import plotly

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    chart_type = request.form.get("chart_type", "box")

    # Load real coffee export data
    df = pd.read_csv("coffee_exports.csv")

    # Clean and prepare data
    df = df.dropna()  # Remove any rows with missing values
    df['Year'] = df['Year'].astype(str)  # Convert year to string for categorical treatment

    # Select chart type using real data
    if chart_type == "bar":
        fig = px.bar(df,
                     x="Country",
                     y="Export_Tons",
                     color="Region",
                     title="Global Coffee Exports by Country (Tons)",
                     hover_data=["Export_Value_USD", "Year"])
    elif chart_type == "scatter":
        fig = px.scatter(df,
                         x="Year",
                         y="Export_Tons",
                         color="Country",
                         size="Export_Value_USD",
                         hover_name="Country",
                         title="Coffee Export Trends Over Time",
                         labels={"Export_Tons": "Export Quantity (Tons)"},
                         custom_data=["Export_Value_USD"])




    else:
        fig = px.box(df,
                     x="Country",
                     y="Export_Tons",
                     color="Region",
                     title="Distribution of Coffee Exports",
                     hover_data=["Country"])

    # Apply dark layout with improved styling
    fig.update_layout(
        plot_bgcolor='#1a1c23',
        paper_bgcolor='#1a1c23',
        font_color='#ffffff',
        autosize=True,
        margin=dict(t=80, l=80, r=80, b=80),
        height=700,
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Customize axes and hover
    fig.update_xaxes(
        showgrid=False,
        color='#cccccc',
        title_font=dict(size=14)
    )
    fig.update_yaxes(
        showgrid=False,
        color='#cccccc',
        title_font=dict(size=14)
    )

    # Format hover tooltip
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>" +
                      "Exports: %{y:,.0f} tons<br>" +
                      "Value: $%{customdata[0]:,.0f}<extra></extra>"
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", graphJSON=graphJSON, chart_type=chart_type)


if __name__ == "__main__":
    app.run(debug=True)