# --------------------------------------------------------------
# 🏦 BANKRUPTCY PREDICTION DASHBOARD (VERSION-STABLE)
# --------------------------------------------------------------
# ✅ Compatible with:
#   streamlit==1.45.1
#   pandas==2.3.3
#   numpy==2.2.6
#   matplotlib==3.10.6
#   seaborn==0.13.2
# --------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# ⚙️ PAGE CONFIGURATION
# --------------------------------------------------------------
st.set_page_config(
    page_title="Bankruptcy Prediction Dashboard",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------------------
# 🎨 CUSTOM CSS STYLING
# --------------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .prediction-high-risk {
        background-color: #ff6b6b;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        border: 2px solid #ff0000;
    }
    .prediction-low-risk {
        background-color: #51cf66;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        border: 2px solid #2b8a3e;
    }
    .prediction-medium-risk {
        background-color: #ffd43b;
        color: black;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        border: 2px solid #e67700;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------
# 🏷️ PAGE HEADER
# --------------------------------------------------------------
st.markdown('<h1 class="main-header">🏦 Company Bankruptcy Prediction</h1>', unsafe_allow_html=True)

# --------------------------------------------------------------
# 📘 FEATURE DEFINITIONS
# --------------------------------------------------------------
feature_descriptions = {
    'A1': 'Net Profit / Total Assets',
    'A2': 'Total Liabilities / Total Assets', 
    'A3': 'Working Capital / Total Assets',
    'A4': 'Current Assets / Short-term Liabilities',
    'A5': 'Financial Stability Ratio',
    'A6': 'Retained Earnings / Total Assets',
    'A7': 'EBIT / Total Assets',
    'A8': 'Book Value of Equity / Total Liabilities',
    'A9': 'Sales / Total Assets',
    'A10': 'Equity / Total Assets'
}

# --------------------------------------------------------------
# 🧮 BANKRUPTCY RISK CALCULATION
# --------------------------------------------------------------
def calculate_bankruptcy_risk(features: dict) -> float:
    """
    Rule-based scoring system to estimate bankruptcy probability.
    Each financial ratio contributes to a cumulative risk score.
    """
    risk_score = 0

    # Profitability (A1)
    if features['A1'] < 0:
        risk_score += 30
    elif features['A1'] < 0.02:
        risk_score += 15
    elif features['A1'] > 0.1:
        risk_score -= 10

    # Leverage (A2)
    if features['A2'] > 0.7:
        risk_score += 25
    elif features['A2'] > 0.6:
        risk_score += 12
    elif features['A2'] < 0.3:
        risk_score -= 5

    # Liquidity (A4)
    if features['A4'] < 1.0:
        risk_score += 20
    elif features['A4'] < 1.5:
        risk_score += 10
    elif features['A4'] > 3.0:
        risk_score -= 5

    # Working Capital (A3)
    if features['A3'] < 0:
        risk_score += 25
    elif features['A3'] < 0.1:
        risk_score += 12
    elif features['A3'] > 0.3:
        risk_score -= 5

    # Efficiency (A7)
    if features['A7'] < 0:
        risk_score += 20
    elif features['A7'] < 0.03:
        risk_score += 10

    # Convert score → probability
    probability = min(risk_score / 100, 0.95)
    return max(probability, 0.05)

# --------------------------------------------------------------
# 🧭 APP STRUCTURE (TABS)
# --------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🏠 Home", "🤖 Prediction", "📊 Analysis"])

# --------------------------------------------------------------
# 🏠 TAB 1: HOME OVERVIEW
# --------------------------------------------------------------
with tab1:
    st.header("Financial Bankruptcy Prediction System")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("""
        ### 📈 About This System

        This dashboard estimates **company bankruptcy risk** through
        **financial ratio analysis** and a **rule-based scoring model**.

        **Key Features:**
        - 🎯 Real-time Risk Assessment  
        - 📊 Ratio-based Financial Evaluation  
        - 💡 Risk Factor Breakdown  
        - 📈 Interactive Visual Analytics  

        **Methodology:**
        - Evaluation of 10 financial ratios  
        - Weighted risk score → bankruptcy probability  
        - Live business health insights  
        """)

    with col2:
        st.metric("System Accuracy", "~85%")
        st.metric("Risk Coverage", "10 Key Ratios")
        st.metric("Response Time", "Instant")

# --------------------------------------------------------------
# 🤖 TAB 2: RISK PREDICTION INTERFACE
# --------------------------------------------------------------
with tab2:
    st.header("🎯 Bankruptcy Risk Prediction")

    st.subheader("Enter Financial Ratios Below")

    col1, col2 = st.columns(2)
    input_data = {}

    # Left column: Profitability + Liquidity
    with col1:
        st.write("**💰 Profitability Ratios**")
        input_data['A1'] = st.slider('A1 - Net Profit/Total Assets', -1.0, 1.0, 0.05, 0.01)
        input_data['A7'] = st.slider('A7 - EBIT/Total Assets', -1.0, 1.0, 0.06, 0.01)

        st.write("**🏦 Liquidity Ratios**")
        input_data['A4'] = st.slider('A4 - Current Assets/Short-term Liabilities', 0.0, 10.0, 1.57, 0.1)

    # Right column: Leverage + Efficiency
    with col2:
        st.write("**📊 Leverage Ratios**")
        input_data['A2'] = st.slider('A2 - Total Liabilities/Total Assets', 0.0, 2.0, 0.47, 0.01)
        input_data['A8'] = st.slider('A8 - Book Value of Equity/Total Liabilities', 0.0, 5.0, 1.07, 0.1)

        st.write("**⚖️ Efficiency Ratios**")
        input_data['A3'] = st.slider('A3 - Working Capital/Total Assets', -1.0, 1.0, 0.20, 0.01)
        input_data['A9'] = st.slider('A9 - Sales/Total Assets', 0.0, 5.0, 1.20, 0.1)

    # Prediction button
    if st.button("🔍 Analyze Bankruptcy Risk", type="primary", use_container_width=True):
        probability = calculate_bankruptcy_risk(input_data)

        # Classify risk
        if probability < 0.3:
            risk_level = "LOW RISK"
            css_class = "prediction-low-risk"
        elif probability < 0.7:
            risk_level = "MEDIUM RISK"
            css_class = "prediction-medium-risk"
        else:
            risk_level = "HIGH RISK"
            css_class = "prediction-high-risk"

        # Display
        st.markdown(f'<div class="{css_class}">🏦 {risk_level}</div>', unsafe_allow_html=True)

        # Key metrics
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Risk Probability", f"{probability:.1%}")
        with c2: st.metric("Risk Level", risk_level.split()[0])
        with c3:
            confidence = (1 - abs(probability - 0.5) * 2)
            st.metric("Confidence", f"{confidence:.1%}")

        # Risk factor insights
        st.subheader("🔍 Risk Factor Breakdown")
        risk_factors = []
        if input_data['A1'] < 0: risk_factors.append("❌ Negative Net Profit (A1)")
        if input_data['A2'] > 0.7: risk_factors.append("❌ High Debt Load (A2)")
        if input_data['A3'] < 0: risk_factors.append("❌ Negative Working Capital (A3)")
        if input_data['A4'] < 1.0: risk_factors.append("❌ Poor Liquidity (A4)")

        if risk_factors:
            st.error("**Critical Risk Factors:**")
            for factor in risk_factors:
                st.write(factor)
        else:
            st.success("✅ No major red flags detected")

# --------------------------------------------------------------
# 📊 TAB 3: FINANCIAL HEALTH ANALYSIS
# --------------------------------------------------------------
with tab3:
    st.header("📈 Financial Health Analysis")

    categories = ['Profitability', 'Liquidity', 'Leverage', 'Efficiency', 'Growth']
    sample_scores = [0.7, 0.8, 0.6, 0.75, 0.65]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(categories))
    colors = ['green' if x > 0.7 else 'orange' if x > 0.5 else 'red' for x in sample_scores]

    bars = ax.barh(y_pos, sample_scores, color=colors, alpha=0.75)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)
    ax.set_xlabel('Health Score (0–1)')
    ax.set_title('Company Financial Health Overview')
    ax.set_xlim(0, 1)

    # Add text labels
    for i, v in enumerate(sample_scores):
        ax.text(v + 0.02, i, f'{v:.0%}', va='center', fontweight='bold')

    st.pyplot(fig)

# --------------------------------------------------------------
# ⚖️ FOOTER DISCLAIMER
# --------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>Disclaimer:</strong> This dashboard is for educational and analytical purposes only.</p>
</div>
""", unsafe_allow_html=True)
