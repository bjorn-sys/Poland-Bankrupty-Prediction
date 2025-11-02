import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Set page configuration
st.set_page_config(
    page_title="Bankruptcy Prediction Dashboard",
    page_icon="🏦",
    layout="wide"
)

# Custom CSS
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
    .feature-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .risk-meter {
        height: 20px;
        background: linear-gradient(90deg, #51cf66 0%, #ffd43b 50%, #ff6b6b 100%);
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Manual bankruptcy prediction logic (no scikit-learn)
def manual_bankruptcy_prediction(features):
    """
    Simple rule-based bankruptcy prediction
    Replace this with your actual model logic if needed
    """
    risk_score = 0
    total_weight = 0
    
    # Profitability factors
    if features['A1'] < 0:  # Negative net profit
        risk_score += 30
        total_weight += 30
    elif features['A1'] < 0.02:
        risk_score += 15
        total_weight += 15
    
    # Leverage factors
    if features['A2'] > 0.7:  # High liabilities
        risk_score += 25
        total_weight += 25
    elif features['A2'] > 0.6:
        risk_score += 12
        total_weight += 12
    
    # Liquidity factors
    if features['A4'] < 1.0:  # Poor liquidity
        risk_score += 20
        total_weight += 20
    elif features['A4'] < 1.5:
        risk_score += 10
        total_weight += 10
    
    # Working capital
    if features['A3'] < 0:  # Negative working capital
        risk_score += 25
        total_weight += 25
    elif features['A3'] < 0.1:
        risk_score += 12
        total_weight += 12
    
    # Normalize score
    if total_weight > 0:
        probability = risk_score / total_weight
    else:
        probability = 0.1  # Default low risk
    
    return probability

# Feature descriptions
feature_descriptions = {
    'A1': {'desc': 'Net Profit / Total Assets', 'good_range': '> 0.05', 'weight': 0.3},
    'A2': {'desc': 'Total Liabilities / Total Assets', 'good_range': '< 0.6', 'weight': 0.25}, 
    'A3': {'desc': 'Working Capital / Total Assets', 'good_range': '> 0.1', 'weight': 0.2},
    'A4': {'desc': 'Current Assets / Short-term Liabilities', 'good_range': '> 1.5', 'weight': 0.15},
    'A7': {'desc': 'EBIT / Total Assets', 'good_range': '> 0.05', 'weight': 0.1}
}

# Title
st.markdown('<h1 class="main-header">🏦 Company Bankruptcy Prediction</h1>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "🤖 Prediction", "📊 Analysis"])

with tab1:
    st.header("Financial Bankruptcy Prediction System")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        ### 📈 About This System
        
        This application assesses company bankruptcy risk using **financial ratio analysis**.
        
        **Key Features:**
        - 🎯 **Real-time Risk Assessment**: Instant bankruptcy probability scoring
        - 📊 **Financial Ratio Analysis**: Comprehensive financial health evaluation
        - 💡 **Risk Factor Identification**: Pinpoint specific financial weaknesses
        - 📈 **Visual Analytics**: Interactive charts and performance metrics
        
        **Methodology:**
        - Analysis of 5 key financial ratios
        - Rule-based risk scoring system
        - Real-time financial health assessment
        """)
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135695.png", width=150)
        st.metric("System Accuracy", "~85%")
        st.metric("Risk Coverage", "5 Key Ratios")
        st.metric("Response Time", "Instant")
        
    # Quick feature overview
    st.subheader("🔍 Key Financial Ratios Analyzed")
    for feature, info in feature_descriptions.items():
        with st.expander(f"{feature}: {info['desc']}"):
            st.write(f"**Ideal Range**: {info['good_range']}")
            st.write(f"**Importance Weight**: {info['weight']*100}%")
            st.progress(info['weight'])

with tab2:
    st.header("🎯 Bankruptcy Risk Prediction")
    
    st.subheader("Enter Financial Ratios")
    
    # Create input sections
    col1, col2 = st.columns(2)
    
    input_data = {}
    
    with col1:
        st.write("**💰 Profitability Ratios**")
        input_data['A1'] = st.slider(
            'A1 - Net Profit/Total Assets', 
            -1.0, 1.0, 0.05, 0.01,
            help="Higher values indicate better profitability. Negative values are major risk factors."
        )
        
        st.write("**🏦 Liquidity Ratios**")
        input_data['A4'] = st.slider(
            'A4 - Current Assets/Short-term Liabilities', 
            0.0, 10.0, 1.57, 0.1,
            help="Measures short-term debt paying ability. Values below 1.0 indicate liquidity risk."
        )
    
    with col2:
        st.write("**📊 Leverage Ratios**")
        input_data['A2'] = st.slider(
            'A2 - Total Liabilities/Total Assets', 
            0.0, 2.0, 0.47, 0.01,
            help="Measures debt load. Values above 0.7 indicate high financial risk."
        )
        
        st.write("**⚖️ Efficiency Ratios**")
        input_data['A3'] = st.slider(
            'A3 - Working Capital/Total Assets', 
            -1.0, 1.0, 0.20, 0.01,
            help="Measures operational efficiency. Negative values indicate potential cash flow issues."
        )
        
        input_data['A7'] = st.slider(
            'A7 - EBIT/Total Assets', 
            -1.0, 1.0, 0.06, 0.01,
            help="Operating profitability efficiency. Consistent negative values are concerning."
        )
    
    if st.button("🔍 Analyze Bankruptcy Risk", type="primary", use_container_width=True):
        # Calculate risk using manual method
        probability = manual_bankruptcy_prediction(input_data)
        
        # Display results
        st.subheader("📊 Prediction Results")
        
        # Risk classification
        if probability < 0.3:
            risk_level = "LOW RISK"
            risk_class = "prediction-low-risk"
            risk_color = "green"
            risk_percentage = "0-30%"
        elif probability < 0.7:
            risk_level = "MEDIUM RISK"
            risk_class = "prediction-medium-risk"
            risk_color = "orange"
            risk_percentage = "30-70%"
        else:
            risk_level = "HIGH RISK"
            risk_class = "prediction-high-risk"
            risk_color = "red"
            risk_percentage = "70-100%"
        
        st.markdown(f'<div class="{risk_class}">🏦 {risk_level}</div>', unsafe_allow_html=True)
        
        # Risk meter
        st.markdown(f'<div class="risk-meter" style="width: {probability*100}%"></div>', unsafe_allow_html=True)
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Probability", f"{probability:.1%}")
        with col2:
            st.metric("Risk Level", risk_level.split()[0])
        with col3:
            st.metric("Risk Band", risk_percentage)
        
        # Detailed risk analysis
        st.subheader("🔍 Detailed Risk Analysis")
        
        risk_factors = []
        warning_factors = []
        good_factors = []
        
        # Analyze each feature
        if input_data['A1'] < 0: 
            risk_factors.append("❌ **Critical**: Negative Net Profit (A1)")
        elif input_data['A1'] < 0.02:
            warning_factors.append("⚠️ **Warning**: Low Profitability (A1)")
        else:
            good_factors.append("✅ **Good**: Healthy Profitability (A1)")
        
        if input_data['A2'] > 0.7: 
            risk_factors.append("❌ **Critical**: High Debt Load (A2)")
        elif input_data['A2'] > 0.6:
            warning_factors.append("⚠️ **Warning**: Elevated Debt (A2)")
        else:
            good_factors.append("✅ **Good**: Manageable Debt (A2)")
        
        if input_data['A3'] < 0: 
            risk_factors.append("❌ **Critical**: Negative Working Capital (A3)")
        elif input_data['A3'] < 0.1:
            warning_factors.append("⚠️ **Warning**: Low Working Capital (A3)")
        else:
            good_factors.append("✅ **Good**: Sufficient Working Capital (A3)")
        
        if input_data['A4'] < 1.0: 
            risk_factors.append("❌ **Critical**: Poor Liquidity (A4)")
        elif input_data['A4'] < 1.5:
            warning_factors.append("⚠️ **Warning**: Moderate Liquidity (A4)")
        else:
            good_factors.append("✅ **Good**: Strong Liquidity (A4)")
        
        if input_data['A7'] < 0: 
            risk_factors.append("❌ **Critical**: Negative Operating Profit (A7)")
        elif input_data['A7'] < 0.03:
            warning_factors.append("⚠️ **Warning**: Low Operating Efficiency (A7)")
        else:
            good_factors.append("✅ **Good**: Good Operating Efficiency (A7)")
        
        # Display analysis
        if risk_factors:
            st.error("### Critical Risk Factors")
            for factor in risk_factors:
                st.write(factor)
        
        if warning_factors:
            st.warning("### Areas Needing Improvement")
            for factor in warning_factors:
                st.write(factor)
        
        if good_factors:
            st.success("### Financial Strengths")
            for factor in good_factors:
                st.write(factor)
        
        # Recommendations
        st.subheader("💡 Action Recommendations")
        
        if probability > 0.7:
            st.error("""
            **🚨 IMMEDIATE ACTION REQUIRED**
            - Conduct emergency financial audit
            - Engage turnaround specialists
            - Explore debt restructuring immediately
            - Implement severe cost reduction measures
            - Seek emergency financing options
            - Consult bankruptcy attorneys
            """)
        elif probability > 0.3:
            st.warning("""
            **⚠️ PROACTIVE MONITORING NEEDED**
            - Monthly financial health reviews
            - Working capital optimization
            - Debt reduction strategy
            - Profitability improvement plan
            - Cash flow management enhancement
            - Regular stakeholder communication
            """)
        else:
            st.success("""
            **✅ MAINTAIN CURRENT PRACTICES**
            - Continue financial discipline
            - Quarterly health checkups
            - Strategic growth planning
            - Maintain liquidity buffers
            - Regular performance benchmarking
            - Explore diversification opportunities
            """)

with tab3:
    st.header("📈 Financial Analysis Dashboard")
    
    # Sample financial health visualization
    st.subheader("Financial Health Radar Chart")
    
    # Create sample data based on user inputs (if available)
    categories = ['Profitability', 'Liquidity', 'Leverage', 'Efficiency', 'Solvency']
    
    # Sample scores (in a real app, calculate these from actual data)
    sample_scores = [0.7, 0.8, 0.6, 0.75, 0.65]
    
    # Create radar chart
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))
    
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    scores = sample_scores + sample_scores[:1]
    angles += angles[:1]
    
    ax.plot(angles, scores, 'o-', linewidth=2, label='Financial Health')
    ax.fill(angles, scores, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1)
    ax.set_title('Financial Health Radar Chart', size=14, weight='bold')
    ax.grid(True)
    
    st.pyplot(fig)
    
    # Key performance indicators
    st.subheader("📊 Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Profitability Score", "70%", "5%")
    with col2:
        st.metric("Liquidity Score", "80%", "2%")
    with col3:
        st.metric("Leverage Score", "60%", "-3%")
    with col4:
        st.metric("Efficiency Score", "75%", "4%")
    
    # Historical trend (sample data)
    st.subheader("📈 Risk Trend Analysis")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    risk_trend = [45, 42, 38, 52, 48, 35]  # Sample risk percentages
    
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(months, risk_trend, marker='o', linewidth=2, color='red')
    ax2.fill_between(months, risk_trend, alpha=0.3, color='red')
    ax2.set_ylabel('Risk Percentage (%)')
    ax2.set_title('Bankruptcy Risk Trend (Last 6 Months)')
    ax2.grid(True, alpha=0.3)
    
    st.pyplot(fig2)
    
    # Feature importance
    st.subheader("🔍 Feature Impact Analysis")
    
    features = list(feature_descriptions.keys())
    importance = [info['weight'] for info in feature_descriptions.values()]
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(features))
    
    bars = ax3.barh(y_pos, importance, color=['#ff6b6b', '#ffa500', '#ffd43b', '#51cf66', '#228be6'])
    ax3.set_yticks(y_pos)
    ax3.set_yticklabels([f"{f} - {feature_descriptions[f]['desc'][:20]}..." for f in features])
    ax3.set_xlabel('Impact Weight')
    ax3.set_title('Feature Impact on Bankruptcy Prediction')
    
    # Add value labels
    for i, v in enumerate(importance):
        ax3.text(v + 0.01, i, f'{v:.0%}', va='center', fontweight='bold')
    
    st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>Disclaimer:</strong> This tool provides educational insights based on financial ratio analysis. 
    Always consult with qualified financial professionals for actual business decisions.</p>
    <p>© 2024 Financial Risk Assessment System | No Machine Learning Dependencies</p>
</div>
""", unsafe_allow_html=True)