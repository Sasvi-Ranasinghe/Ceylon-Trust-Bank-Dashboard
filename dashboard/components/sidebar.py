from dash import html
from dash_iconify import DashIconify


def create_sidebar():

    return html.Div(

        [

            # =====================
            # Header
            # =====================

            html.Div(

                [

                    html.Img(
                        src="/assets/Bank Logo.png",
                        className="sidebar-logo"
                    ),

                    html.H3(
                        "Ceylon Trust Bank PLC",
                        className="sidebar-title"
                    ),

                    html.P(
                        "Executive Banking Intelligence",
                        className="logo-subtitle"
                    ),

                ],

                className="sidebar-header"

            ),


            # =====================
            # Menu
            # =====================

            html.Div(

                [

                    html.A(
                        [
                            DashIconify(icon="mdi:view-dashboard", width=22, className="sidebar-icon"),
                            html.Span("Dashboard")
                        ],
                        href="/dashboard",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:account-group", width=22, className="sidebar-icon"),
                            html.Span("Customers")
                        ],
                        href="/customers",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:credit-card-outline", width=22, className="sidebar-icon"),
                            html.Span("Accounts")
                        ],
                        href="/accounts",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:swap-horizontal-bold", width=22, className="sidebar-icon"),
                            html.Span("Transactions")
                        ],
                        href="/transactions",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:bank-outline", width=22, className="sidebar-icon"),
                            html.Span("Loans")
                        ],
                        href="/loans",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:office-building-outline", width=22, className="sidebar-icon"),
                            html.Span("Branches")
                        ],
                        href="/branches",
                        className="menu-item"
                    ),

                    html.A(
                        [
                            DashIconify(icon="mdi:file-chart-outline", width=22, className="sidebar-icon"),
                            html.Span("Reports")
                        ],
                        href="/reports",
                        className="menu-item"
                    ),

                ],

                className="menu"

            ),

            # =====================
            # Footer
            # =====================

            html.Div(

                [

                    html.Hr(className="menu-divider"),

                    html.A(

                        [

                            DashIconify(
                                icon="mdi:logout",
                                width=22,
                                className="sidebar-icon"
                            ),

                            html.Span("Logout")

                        ],

                        href="/",

                        className="logout-item"

                    ),

                    html.P(
                        "Version 1.0",
                        className="version"
                    ),

                    html.P(
                        "Developed by Sasvi Ranasinghe",
                        className="developer"
                    )

                ],

                className="sidebar-footer"

            )

        ],

        className="sidebar"

    )