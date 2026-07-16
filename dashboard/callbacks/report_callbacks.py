from dash import Input, Output, dcc
import pandas as pd
from io import BytesIO
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from utils.data_loader import load_data

data=load_data()

def register_report_callbacks(app):

    @app.callback(Output("download-csv","data"),
                  Input("download-csv-btn","n_clicks"),
                  prevent_initial_call=True)
    def download_csv(_):
        customers=data["customers"]; accounts=data["accounts"]
        transactions=data["transactions"]; loans=data["loans"]
        report=pd.DataFrame({
            "Metric":["Customers","Accounts","Transactions","Loans","Total Deposits","Loan Portfolio"],
            "Value":[len(customers),len(accounts),len(transactions),len(loans),
                     f"LKR {accounts['Balance'].sum():,.0f}",
                     f"LKR {loans['LoanAmount'].sum():,.0f}"]
        })
        return dcc.send_data_frame(report.to_csv,"Executive_Banking_Report.csv",index=False)

    @app.callback(Output("download-pdf","data"),
                  Input("download-pdf-btn","n_clicks"),
                  prevent_initial_call=True)
    def download_pdf(_):
        customers=data["customers"]; accounts=data["accounts"]
        transactions=data["transactions"]; loans=data["loans"]
        buffer=BytesIO()
        doc=SimpleDocTemplate(buffer)
        styles=getSampleStyleSheet()
        styles["Title"].alignment=TA_CENTER
        elements=[
            Paragraph("Ceylon Trust Bank PLC",styles["Title"]),
            Paragraph("Executive Banking Report",styles["Heading2"]),
            Paragraph(f"Generated: {datetime.now().strftime('%d %B %Y %H:%M')}",styles["BodyText"]),
            Spacer(1,15)
        ]
        tbl=Table([
            ["Metric","Value"],
            ["Customers",f"{len(customers):,}"],
            ["Accounts",f"{len(accounts):,}"],
            ["Transactions",f"{len(transactions):,}"],
            ["Loans",f"{len(loans):,}"],
            ["Total Deposits",f"LKR {accounts['Balance'].sum():,.0f}"],
            ["Loan Portfolio",f"LKR {loans['LoanAmount'].sum():,.0f}"]
        ],colWidths=[220,180])
        tbl.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1F3557")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("GRID",(0,0),(-1,-1),0.5,colors.grey),
            ("BACKGROUND",(0,1),(-1,-1),colors.beige),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("ALIGN",(0,0),(-1,-1),"CENTER")
        ]))
        elements.append(tbl)
        elements.append(Spacer(1,15))
        elements.append(Paragraph("Executive Insights",styles["Heading2"]))
        for t in [
            "Savings Accounts remain the dominant banking product.",
            "Western Province contributes the largest customer base.",
            "Digital banking usage continues to increase.",
            "Personal Loans remain the largest lending category.",
            "Overall financial performance remains healthy."
        ]:
            elements.append(Paragraph("• "+t,styles["BodyText"]))
        doc.build(elements)
        pdf=buffer.getvalue(); buffer.close()
        return dcc.send_bytes(pdf,"Executive_Banking_Report.pdf")
