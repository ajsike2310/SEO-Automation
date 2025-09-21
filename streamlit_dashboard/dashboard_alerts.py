import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configure the page
st.set_page_config(
    page_title="ASIS SEO Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .alert-box {
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .alert-success {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
    }
    .alert-warning {
        background-color: #fff3cd;
        border-color: #ffeaa7;
        color: #856404;
    }
    .alert-danger {
        background-color: #f8d7da;
        border-color: #f5c6cb;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 ASIS SEO Automation Dashboard</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📋 Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["Overview", "Keyword Tracking", "Backlink Monitor", "SEO Audit", "Reports"]
)

# Generate sample data for demo
@st.cache_data
def generate_sample_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    # Keyword data
    keywords_data = {
        'keyword': ['SEO automation', 'digital marketing', 'website optimization', 'keyword tracking', 'backlink analysis'],
        'position': [3, 7, 12, 5, 9],
        'search_volume': [1200, 8500, 3200, 890, 1500],
        'difficulty': [65, 78, 45, 52, 71],
        'trend': ['↗️', '↘️', '↗️', '→', '↗️']
    }
    
    # Traffic data
    traffic_data = pd.DataFrame({
        'date': np.random.choice(dates, 100),
        'organic_traffic': np.random.randint(100, 1000, 100),
        'page_views': np.random.randint(500, 5000, 100),
        'bounce_rate': np.random.uniform(0.2, 0.8, 100)
    })
    
    return keywords_data, traffic_data

keywords_data, traffic_data = generate_sample_data()

if page == "Overview":
    st.subheader("📊 SEO Performance Overview")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🔍 Total Keywords Tracked",
            value="147",
            delta="12"
        )
    
    with col2:
        st.metric(
            label="🔗 Total Backlinks",
            value="2,847",
            delta="45"
        )
    
    with col3:
        st.metric(
            label="📈 Avg. Position",
            value="8.3",
            delta="-1.2"
        )
    
    with col4:
        st.metric(
            label="🚨 SEO Alerts",
            value="3",
            delta="1"
        )
    
    # Alerts Section
    st.subheader("🚨 Recent Alerts")
    
    alerts = [
        ("🟢 Success", "New backlink detected from high-authority domain", "alert-success"),
        ("🟡 Warning", "Keyword 'SEO automation' dropped 3 positions", "alert-warning"),
        ("🔴 Critical", "Site speed score decreased below 70", "alert-danger")
    ]
    
    for alert_type, message, css_class in alerts:
        st.markdown(f'<div class="alert-box {css_class}"><strong>{alert_type}:</strong> {message}</div>', 
                   unsafe_allow_html=True)
    
    # Traffic Chart
    st.subheader("📈 Organic Traffic Trend")
    
    # Aggregate traffic data by date
    daily_traffic = traffic_data.groupby('date')['organic_traffic'].sum().reset_index()
    daily_traffic = daily_traffic.sort_values('date')
    
    fig_traffic = px.line(
        daily_traffic, 
        x='date', 
        y='organic_traffic',
        title="Daily Organic Traffic",
        labels={'organic_traffic': 'Organic Traffic', 'date': 'Date'}
    )
    fig_traffic.update_layout(height=400)
    st.plotly_chart(fig_traffic, use_container_width=True)

elif page == "Keyword Tracking":
    st.subheader("🔍 Keyword Performance")
    
    # Keywords table
    df_keywords = pd.DataFrame(keywords_data)
    
    st.dataframe(
        df_keywords,
        column_config={
            "keyword": "Keyword",
            "position": st.column_config.NumberColumn("Position", format="%d"),
            "search_volume": st.column_config.NumberColumn("Search Volume", format="%d"),
            "difficulty": st.column_config.NumberColumn("Difficulty", format="%d"),
            "trend": "Trend"
        },
        hide_index=True,
        use_container_width=True
    )
    
    # Position distribution chart
    fig_pos = px.histogram(
        df_keywords, 
        x='position', 
        title="Keyword Position Distribution",
        nbins=10
    )
    st.plotly_chart(fig_pos, use_container_width=True)

elif page == "Backlink Monitor":
    st.subheader("🔗 Backlink Analysis")
    
    # Sample backlink data
    backlink_data = {
        'domain': ['example.com', 'testsite.org', 'samplepage.net', 'demo.co', 'trial.info'],
        'domain_authority': [65, 45, 72, 38, 58],
        'link_type': ['Follow', 'NoFollow', 'Follow', 'Follow', 'NoFollow'],
        'status': ['Active', 'Active', 'Lost', 'Active', 'Active']
    }
    
    df_backlinks = pd.DataFrame(backlink_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Backlinks by status
        status_counts = df_backlinks['status'].value_counts()
        fig_status = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Backlink Status Distribution"
        )
        st.plotly_chart(fig_status, use_container_width=True)
    
    with col2:
        # Domain Authority distribution
        fig_da = px.histogram(
            df_backlinks,
            x='domain_authority',
            title="Domain Authority Distribution",
            nbins=10
        )
        st.plotly_chart(fig_da, use_container_width=True)
    
    # Backlinks table
    st.dataframe(df_backlinks, use_container_width=True)

elif page == "SEO Audit":
    st.subheader("🔍 SEO Audit Results")
    
    # Audit scores
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🏃‍♂️ Page Speed", "85", "5")
    
    with col2:
        st.metric("📱 Mobile Friendly", "92", "2")
    
    with col3:
        st.metric("🔒 Security Score", "88", "-3")
    
    # Audit details
    audit_items = [
        ("✅ Title Tags", "All pages have unique title tags", "success"),
        ("⚠️ Meta Descriptions", "5 pages missing meta descriptions", "warning"),
        ("✅ Image Alt Text", "All images have alt text", "success"),
        ("❌ Broken Links", "3 broken internal links found", "danger"),
        ("✅ SSL Certificate", "Valid SSL certificate installed", "success")
    ]
    
    st.subheader("📋 Audit Details")
    for status, description, alert_type in audit_items:
        st.markdown(f'<div class="alert-box alert-{alert_type}">{status} {description}</div>', 
                   unsafe_allow_html=True)

elif page == "Reports":
    st.subheader("📊 SEO Reports")
    
    # Report generation
    st.write("Generate comprehensive SEO reports:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📈 Generate Traffic Report", type="primary"):
            st.success("Traffic report generated successfully!")
            st.download_button(
                label="⬇️ Download Traffic Report",
                data="Sample traffic report data...",
                file_name="traffic_report.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("🔍 Generate Keyword Report", type="primary"):
            st.success("Keyword report generated successfully!")
            st.download_button(
                label="⬇️ Download Keyword Report",
                data="Sample keyword report data...",
                file_name="keyword_report.csv",
                mime="text/csv"
            )
    
    # Recent reports
    st.subheader("📁 Recent Reports")
    recent_reports = [
        ("Traffic Analysis", "2024-12-15", "CSV"),
        ("Keyword Performance", "2024-12-14", "PDF"),
        ("Backlink Audit", "2024-12-13", "Excel"),
        ("Technical SEO", "2024-12-12", "PDF")
    ]
    
    for report_name, date, format_type in recent_reports:
        col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
        with col1:
            st.write(f"📄 {report_name}")
        with col2:
            st.write(date)
        with col3:
            st.write(format_type)
        with col4:
            st.button("⬇️", key=f"download_{report_name}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        🚀 ASIS SEO Automation Dashboard | Built with Streamlit | 
        Last updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M") + """
    </div>
    """, 
    unsafe_allow_html=True
)