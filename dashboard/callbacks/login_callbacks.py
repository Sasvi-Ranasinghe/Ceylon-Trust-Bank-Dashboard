from dash import Input, Output, State, no_update

def register_login_callbacks(app):

    @app.callback(

        Output("login-message", "children"),
        Output("login-message", "style"),
        Output("url", "pathname"),

        Input("login-btn", "n_clicks"),

        State("username", "value"),
        State("password", "value"),

        prevent_initial_call=True

    )
    def login(n_clicks, username, password):

        if n_clicks is None:

            return "", {"display":"none"}, no_update

        if username == "admin" and password == "admin123":

            return "", {"display":"none"}, "/dashboard"

        return (

            "❌ Invalid Username or Password",

            {
                "display":"block",
                "color":"#FF5B6E",
                "marginTop":"15px",
                "fontWeight":"600",
                "textAlign":"center"
            },

            no_update

        )