from dash import html, dcc
from dash_iconify import DashIconify
from datetime import datetime


def create_navbar():

    today = datetime.now().strftime("%d %B %Y")
    last_login = datetime.now().strftime("%d %B %Y | %I:%M %p")

    return html.Div(

        [

            # ======================================
            # LEFT SIDE
            # ======================================

            html.Div(

                [

                    html.H2(
                        "Executive Banking Dashboard",
                        className="page-title"
                    ),

                    html.P(
                        "Business Intelligence & Analytics Platform",
                        className="page-subtitle"
                    )

                ]

            ),

            # ======================================
            # RIGHT SIDE
            # ======================================

            html.Div(

                [

                    # -------------------
                    # Notification Button
                    # -------------------

                    html.Div(

                        DashIconify(
                            icon="mdi:bell-outline",
                            width=24
                        ),

                        id="notification-btn",

                        className="nav-icon"

                    ),

                    # -------------------
                    # Settings Button
                    # -------------------

                    html.Div(

                        DashIconify(
                            icon="mdi:cog-outline",
                            width=24
                        ),

                        id="settings-btn",

                        className="nav-icon"

                    ),

                    # -------------------
                    # Admin Button
                    # -------------------

                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:account-circle-outline",
                                width=22
                            ),

                            html.Span("Admin")

                        ],

                        id="admin-btn",

                        className="profile"

                    ),

                    html.Div(

                        today,

                        className="today"

                    )

                ],

                className="nav-right"

            ),

            # ======================================
            # Notification Panel
            # ======================================

            html.Div(

                [

                    html.H4("Notifications"),

                    html.Hr(),

                    html.P("• New customer registered"),

                    html.P("• Loan application approved"),

                    html.P("• Daily report generated"),

                    html.P("• Database backup completed")

                ],

                id="notification-panel",

                className="notification-panel",

                style={"display": "none"}

            ),

            # ======================================
            # Settings Panel
            # ======================================

            html.Div(

                [

                    html.H4("Settings"),

                    html.Hr(),

                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:theme-light-dark",
                                width=18
                            ),

                            html.Span("Dark Mode")

                        ],
                        id="dark-mode-btn",
                        className="settings-item"

                    ),

                    html.Div(

                        [

                            html.H2("🌙 Dark Mode"),

                            html.Hr(),

                            html.H4("Coming Soon"),

                            html.P(

                                "Dark / Light Theme switching will be available in Version 2.0.",

                                className="coming-text"

                            ),

                            html.Button(

                                "Close",

                                id="dark-close",

                                className="download-btn"

                            )

                        ],

                        id="dark-panel",

                        className="about-panel",

                        style={"display": "none"}

                    ),


                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:information-outline",
                                width=18
                            ),

                            html.Span("About System")

                        ],

                        id="about-btn",
                        className="settings-item"

                    ),

                ],

                id="settings-panel",

                className="settings-panel",

                style={"display": "none"}

            ),

            html.Div(

                [

                    html.H3("Ceylon Trust Bank PLC"),

                    html.Hr(),

                    html.P("Executive Banking Dashboard"),

                    html.P("Version : 1.0"),

                    html.P("Developer : Sasvi Ranasinghe"),

                    html.Button(
                        "Close",
                        id="about-close",
                        className="download-btn"
                    )

                ],

                id="about-panel",

                className="about-panel",

                style={"display": "none"}

            ),

            # ======================================
            # Admin Dropdown
            # ======================================

            html.Div(

                [

                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:account",
                                width=18
                            ),

                            html.Span("My Profile")

                        ],
                        id="profile-btn",
                        className="dropdown-item"

                    ),

                    html.Div(

                        [

                            html.H3("Administrator Profile"),

                            html.Hr(),

                            html.P("👤 Username : admin"),

                            html.P("🛡 Role : System Administrator"),

                            html.P("🏦 Department : Executive Banking"),

                            html.P("📧 Email : admin@ceylontrustbank.com"),

                            html.P(

                                f"🕒 Session Started : {last_login}"

                            ),

                            html.Br(),

                            html.Button(

                                "Close",

                                id="profile-close",

                                className="download-btn"

                            )

                        ],

                        id="profile-panel",

                        className="about-panel",

                        style={"display": "none"}

                    ),

                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:lock-reset",
                                width=18
                            ),

                            html.Span("Change Password")

                        ],

                        id="password-btn",
                        className="dropdown-item"

                    ),

                    html.Div(

                        [

                            html.H3("Change Password"),

                            html.Hr(),

                            dcc.Input(

                                id="current-password",

                                type="password",

                                placeholder="Current Password",

                                className="login-input"

                            ),

                            dcc.Input(

                                id="new-password",

                                type="password",

                                placeholder="New Password",

                                className="login-input"

                            ),

                            dcc.Input(

                                id="confirm-password",

                                type="password",

                                placeholder="Confirm New Password",

                                className="login-input"

                            ),

                            html.Div(

                                "",

                                id="password-message",

                                className="login-message"

                            ),

                            html.Br(),

                            html.Button(

                                "Save Password",

                                id="save-password",

                                className="download-btn"

                            ),

                            html.Button(

                                "Close",

                                id="password-close",

                                className="download-btn",

                                style={"marginLeft": "10px"}

                            )

                        ],

                        id="password-panel",

                        className="about-panel",

                        style={"display": "none"}

                    ),


                    html.Hr(),

                    html.Div(

                        [

                            DashIconify(
                                icon="mdi:logout",
                                width=18
                            ),

                            html.Span("Logout")

                        ],

                        id="logout-btn",
                        className="dropdown-item logout"

                    )

                ],

                id="admin-dropdown",

                className="admin-dropdown",

                style={"display": "none"}

            ),

# ======================================
# Logout Panel
# ======================================

html.Div(

    [

        html.H3("Confirm Logout"),

        html.Hr(),

        html.P(

            "Are you sure you want to logout from the Banking Dashboard?"

        ),

        html.Br(),

        html.Button(

            "Yes, Logout",

            id="confirm-logout",

            className="download-btn"

        ),

        html.Button(

            "Cancel",

            id="cancel-logout",

            className="download-btn",

            style={"marginLeft":"10px"}

        )

    ],

    id="logout-panel",

    className="about-panel",

    style={"display":"none"}

),

dcc.Location(

    id="logout-url",

    refresh=True

)
    ],

    className = "navbar"

)