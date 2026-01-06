import streamlit as st
import pandas as pd
from datetime import datetime
from utils.excel_handler import ExcelHandler

# Import fungsi dari management_sss karena fungsinya sama
from modules.management_sss import (
    show_input_invoice,
    show_update_invoice,
    show_status_invoice,
    show_rekap_invoice
)

def show():
    """Dashboard Management Non SSS - Invoice Manual"""
    
    st.title("📝 Invoice Manual Dashboard")
    st.markdown("### Management Non SSS - Pengelolaan Invoice Manual")
    
    excel = ExcelHandler()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Input Invoice", "✏️ Update Invoice", 
        "📊 Status Invoice", "📈 Rekap"
    ])
    
    with tab1:
        show_input_invoice(excel, 'Non-SSS')
    
    with tab2:
        show_update_invoice(excel, 'Non-SSS')
    
    with tab3:
        show_status_invoice(excel, 'Non-SSS')
    
    with tab4:
        show_rekap_invoice(excel, 'Non-SSS')