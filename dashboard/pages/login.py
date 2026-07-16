import dash
from dash import html, dcc

dash.register_page(__name__, path="/", name="Login")

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(src="/assets/Bank Logo.png", className="login-logo"),
                        html.H1("Ceylon Trust Bank PLC", className="login-title"),
                        html.P("Executive Banking Intelligence", className="login-subtitle"),
                    ],
                    className="login-left",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Secure Demo Access", className="demo-title"),
                                html.Div([html.Span("👤 Username"), html.Strong("admin")], className="demo-row"),
                                html.Div([html.Span("🔒 Password"), html.Strong("admin123")], className="demo-row"),
                                html.P("For Academic Demonstration Only", className="demo-note"),
                            ],
                            className="demo-card",
                        ),
                        dcc.Input(id="username", type="text", placeholder="Username", className="login-input"),
                        dcc.Input(id="password", type="password", placeholder="Password", className="login-input"),
                        html.Button("Login", id="login-btn", className="login-btn"),
                        html.Div("", id="login-message", className="login-message"),
                        html.Div("© 2026 Ceylon Trust Bank PLC • Developed by Sasvi Ranasinghe", className="login-footer"),
                    ],
                    className="login-right",
                ),
            ],
            className="login-wrapper",
        )
    ],
    className="login-page",
)
