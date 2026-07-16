from dash import Input, Output, State


def register_navbar_callbacks(app):

    @app.callback(

        Output("notification-panel", "style"),

        Input("notification-btn", "n_clicks"),

        State("notification-panel", "style"),

        prevent_initial_call=True

    )
    def toggle_notifications(n_clicks, current_style):

        if current_style is None:
            current_style = {"display": "none"}

        if current_style.get("display") == "none":

            return {
                "display": "block"
            }

        return {
            "display": "none"
        }

    @app.callback(

        Output("settings-panel", "style"),

        Input("settings-btn", "n_clicks"),

        State("settings-panel", "style"),

        prevent_initial_call=True

    )
    def toggle_settings(n_clicks, style):

        if style is None:
            style = {"display": "none"}

        if style.get("display") == "none":
            return {"display": "block"}

        return {"display": "none"}

    @app.callback(

        Output("dark-panel", "style"),

        Input("dark-mode-btn", "n_clicks"),

        Input("dark-close", "n_clicks"),

        prevent_initial_call=True

    )
    def toggle_dark(open_click, close_click):

        from dash import callback_context

        if not callback_context.triggered:
            return {"display": "none"}

        button = callback_context.triggered[0]["prop_id"].split(".")[0]

        if button == "dark-mode-btn":
            return {"display": "block"}

        return {"display": "none"}

    @app.callback(

        Output("about-panel", "style"),

        Input("about-btn", "n_clicks"),

        Input("about-close", "n_clicks"),

        prevent_initial_call=True

    )
    def toggle_about(open_click, close_click):

        from dash import callback_context

        if not callback_context.triggered:
            return {"display": "none"}

        button = callback_context.triggered[0]["prop_id"].split(".")[0]

        if button == "about-btn":
            return {"display": "block"}

        return {"display": "none"}



    @app.callback(
        Output("admin-dropdown", "style"),
        Input("admin-btn", "n_clicks"),
        State("admin-dropdown", "style"),
        prevent_initial_call=True
    )
    def toggle_admin_dropdown(n, style):

        if style is None:
            style = {"display": "none"}

        if style.get("display") == "none":
            return {"display": "block"}

        return {"display": "none"}

    @app.callback(

        Output("profile-panel", "style"),

        Input("profile-btn", "n_clicks"),

        Input("profile-close", "n_clicks"),

        prevent_initial_call=True

    )
    def toggle_profile(open_click, close_click):

        from dash import callback_context

        if not callback_context.triggered:
            return {"display":"none"}

        button = callback_context.triggered[0]["prop_id"].split(".")[0]

        if button == "profile-btn":
            return {"display":"block"}

        return {"display":"none"}

    @app.callback(

        Output("password-panel","style"),

        Input("password-btn","n_clicks"),

        Input("password-close","n_clicks"),

        prevent_initial_call=True

    )
    def toggle_password(open_click, close_click):

        from dash import callback_context

        if not callback_context.triggered:
            return {"display":"none"}

        button = callback_context.triggered[0]["prop_id"].split(".")[0]

        if button == "password-btn":
            return {"display":"block"}

        return {"display":"none"}

    @app.callback(

        Output("password-message","children"),

        Input("save-password","n_clicks"),

        State("current-password","value"),

        State("new-password","value"),

        State("confirm-password","value"),

        prevent_initial_call=True

    )
    def save_password(n,current,new,confirm):

        if current != "admin123":
            return "❌ Current password is incorrect."

        if new != confirm:
            return "❌ New passwords do not match."

        return "✅ Password updated successfully (Demo Version)."

    @app.callback(

        Output("logout-panel","style"),

        Input("logout-btn","n_clicks"),

        Input("cancel-logout","n_clicks"),

        prevent_initial_call=True

    )
    def logout_popup(open_click, cancel_click):

        from dash import callback_context

        if not callback_context.triggered:
            return {"display":"none"}

        button = callback_context.triggered[0]["prop_id"].split(".")[0]

        if button == "logout-btn":
            return {"display":"block"}

        return {"display":"none"}

    @app.callback(

        Output("logout-url", "pathname"),

        Input("confirm-logout", "n_clicks"),

        prevent_initial_call=True

    )
    def logout(n_clicks):

        if not n_clicks:
            return no_update

        return "/"









