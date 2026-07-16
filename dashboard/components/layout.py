from dash import html

def chart_row(left_chart, right_chart):

    return html.Div(

        [

            html.Div(

                left_chart,

                className="chart-card"

            ),

            html.Div(

                right_chart,

                className="chart-card"

            )

        ],

        className="chart-row"

    )