from dash import Dash, html, page_container, dcc, Input, Output

from components.sidebar import create_sidebar

from callbacks.dashboard_callbacks import register_dashboard_callbacks
from callbacks.report_callbacks import register_report_callbacks
from callbacks.login_callbacks import register_login_callbacks
from callbacks.navbar_callbacks import register_navbar_callbacks

app = Dash(

    __name__,

    use_pages=True,

    title="Ceylon Trust Bank PLC",

    suppress_callback_exceptions=True

)

server = app.server

# Register Callbacks
register_dashboard_callbacks(app)
register_report_callbacks(app)
register_login_callbacks(app)
register_navbar_callbacks(app)

# Layout
app.layout = html.Div(

    [

        dcc.Location(
            id="url"
        ),

        html.Div(
            id="sidebar-container"
        ),

        html.Div(

            page_container,

            className="content"

        )

    ]

)

# Show / Hide Sidebar
@app.callback(

    Output("sidebar-container", "children"),

    Input("url", "pathname")

)
def toggle_sidebar(pathname):

    if pathname == "/":

        return html.Div()

    return create_sidebar()


if __name__ == "__main__":

    app.run(debug=False)