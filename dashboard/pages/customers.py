import dash
from dash import html
from components.charts import (
    gender_chart,
    province_chart,
    occupation_chart
)

from components.layout import chart_row


from utils.data_loader import load_data

dash.register_page(
    __name__,
    path="/customers",
    name="Customers"
)

data = load_data()

customers = data["customers"]

layout = html.Div(

    [

        html.H1(
            "👥 Customer Analytics",
            className="page-title"
        ),

        html.P(
            "Customer demographics and distribution",
            className="page-subtitle"
        ),

        html.Div(

            [

                html.Div(

                    [

                        html.H3("Total Customers"),

                        html.H1(f"{len(customers):,}")

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Male"),

                        html.H1(

                            len(customers[
                                customers["Gender"]=="Male"
                            ])

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Female"),

                        html.H1(

                            len(customers[
                                customers["Gender"]=="Female"
                            ])

                        )

                    ],

                    className="dashboard-card"

                )

            ],

            className="card-container"

        ),

chart_row(

            province_chart(),

            gender_chart()

        ),

        html.Div(

            [

                occupation_chart()

            ],

            className="chart-card"

        )

    ]

)

