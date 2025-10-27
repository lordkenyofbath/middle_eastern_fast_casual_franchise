import streamlit as st
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Sahtein's Strategic Partnership Proposal",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        color: #2C3E50;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.8rem;
        text-align: center;
        color: #7F8C8D;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .gold-accent {
        color: #D4AF37;
        font-weight: bold;
    }
    .metric-box {
        background-color: #F8F9FA;
        border: 2px solid #D4AF37;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 10px;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C3E50;
    }
    .metric-label {
        font-size: 1rem;
        color: #7F8C8D;
        margin-top: 5px;
    }
    .quote-box {
        background-color: #FFFEF7;
        border-left: 5px solid #D4AF37;
        padding: 20px;
        margin: 20px 0;
        font-style: italic;
        font-size: 1.2rem;
        text-align: center;
    }
    .section-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C3E50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #D4AF37;
        padding-bottom: 10px;
    }
    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    .comparison-table th, .comparison-table td {
        border: 1px solid #DDD;
        padding: 12px;
        text-align: left;
    }
    .comparison-table th {
        background-color: #D4AF37;
        color: white;
        font-weight: bold;
    }
    .icon-box {
        text-align: center;
        padding: 15px;
        margin: 10px;
        background-color: #F8F9FA;
        border-radius: 10px;
    }
    .timeline-item {
        padding: 10px;
        margin: 5px 0;
        background-color: #F8F9FA;
        border-left: 4px solid #D4AF37;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to page:", [
    "Cover Page",
    "Table of Contents", 
    "Executive Summary",
    "Strategic Context",
    "Research & Validation",
    "Deliverables",
    "Investment Structure",
    "Implementation Roadmap",
    "Partnership Terms",
    "Next Steps",
    "Signature Page"
])

# Cover Page
if page == "Cover Page":
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        st.markdown('<h1 class="main-header">SAHTEIN\'S</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="sub-header">FAST-CASUAL DEVELOPMENT</h2>', unsafe_allow_html=True)
        st.markdown('<h3 style="text-align: center; color: #2C3E50; margin-bottom: 2rem;">Strategic Partnership Proposal</h3>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <p><strong>Prepared for:</strong> <span class='gold-accent'>Angeles Herrero | Kazbar</span></p>
            <p><strong>Prepared by:</strong> <span class='gold-accent'>MBBB Capital Consulting</span></p>
            <p><strong>Date:</strong> <span class='gold-accent'>October 2025</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="position: fixed; bottom: 20px; right: 20px; color: #D4AF37; font-size: 1.5rem;">◆</div>', unsafe_allow_html=True)

# Table of Contents
elif page == "Table of Contents":
    st.markdown('<h1 class="section-header">CONTENTS</h1>', unsafe_allow_html=True)
    
    contents = [
        ("1. Executive Summary", 3),
        ("2. Strategic Context", 5),
        ("3. Research & Validation", 8),
        ("4. Deliverables", 12),
        ("5. Investment Structure", 16),
        ("6. Implementation Roadmap", 18),
        ("7. Partnership Terms", 21),
        ("8. Next Steps", 23)
    ]
    
    for item, page_num in contents:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{item}**")
        with col2:
            st.markdown(f".......... {page_num}")

# Executive Summary
elif page == "Executive Summary":
    st.markdown('<h1 class="section-header">EXECUTIVE SUMMARY</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: justify; margin: 2rem 0;'>
    In September 2024, you requested support for "a fast food option for Kazbar, like a Subway style but Middle Eastern." Following comprehensive research, we propose Sahtein's—a modern Lebanese fast-casual brand designed to transform Kazbar's 23-year legacy into a scalable, franchise-ready system.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>8 WEEKS</div>
            <div class='metric-label'>Duration</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>SGD 10,000</div>
            <div class='metric-label'>Investment</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>25-30</div>
            <div class='metric-label'>SG Stores</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### THE OPPORTUNITY")
    st.markdown("Singapore's foodservice market is experiencing unprecedented growth, with the fast-casual segment showing 9% annual growth. Middle Eastern cuisine is gaining significant traction among health-conscious millennials, representing a 70% market preference for healthy fast-casual options.")
    
    st.markdown("### THE CHALLENGE")
    st.markdown("Kazbar's single-location model, while successful, faces increasing vulnerability to landlord leverage and market changes. The brand's 23-year legacy remains trapped in a non-scalable format, limiting growth potential and asset value creation.")
    
    st.markdown("### THE SOLUTION")
    st.markdown("Sahtein's leverages Kazbar's proven recipes and brand equity to create a modern Lebanese fast-casual concept. With projected break-even in 5-6 months and 15% net profit margins, this franchise-ready system can unlock trapped value across 25-30 Singapore locations.")

# Strategic Context
elif page == "Strategic Context":
    st.markdown('<h1 class="section-header">STRATEGIC CONTEXT</h1>', unsafe_allow_html=True)
    
    st.markdown("### Project Origin")
    st.markdown("""
    <div class='quote-box'>
    "I might need some help from you. I am looking at a fast food option for Kazbar, like a Subway style but Middle Eastern."
    <br><br>
    — Angeles Herrero, September 2024
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Kazbar's Vulnerability")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### TODAY'S REALITY")
        st.markdown("""
        ✓ 23 years of excellence<br>
        ✓ Award-winning cuisine<br>
        ✓ Strong brand equity<br>
        ✓ Cash-generating
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### STRATEGIC RISKS")
        st.markdown("""
        ✗ Single location<br>
        ✗ Landlord leverage<br>
        ✗ No scalability<br>
        ✗ Trapped value
        """, unsafe_allow_html=True)
    
    st.markdown("### Strategic Objective")
    st.markdown("#### Transform vulnerability into sustainable value")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""
        <div class='icon-box'>
        <div style='font-size: 2rem;'>💰</div>
        <strong>STABILITY</strong><br>
        Multiple revenue streams
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='icon-box'>
        <div style='font-size: 2rem;'>📈</div>
        <strong>INCOME</strong><br>
        Recurring franchise royalties
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='icon-box'>
        <div style='font-size: 2rem;'>🏆</div>
        <strong>VALUE</strong><br>
        Transferable brand system
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class='icon-box'>
        <div style='font-size: 2rem;'>🌏</div>
        <strong>SCALE</strong><br>
        Regional expansion potential
        </div>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown("""
        <div class='icon-box'>
        <div style='font-size: 2rem;'>🛡️</div>
        <strong>PROTECTION</strong><br>
        Diversified asset base
        </div>
        """, unsafe_allow_html=True)

# Research & Validation
elif page == "Research & Validation":
    st.markdown('<h1 class="section-header">RESEARCH & VALIDATION</h1>', unsafe_allow_html=True)
    
    st.markdown("### Market Opportunity")
    st.markdown("#### Singapore Foodservice Market")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(90deg, #2C3E50, #D4AF37); padding: 20px; border-radius: 10px; color: white; text-align: center;'>
        <h3>2025: USD 28.92B ────────────▶ 2030: USD 68.14B</h3>
        <p style='font-size: 1.2rem;'>18.7% CAGR</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>39.4%</div>
            <div class='metric-label'>QSR Share of Market</div>
        </div>
        <div class='metric-box'>
            <div class='metric-value'>9%</div>
            <div class='metric-label'>Fast-Casual Growth</div>
        </div>
        <div class='metric-box'>
            <div class='metric-value'>70%</div>
            <div class='metric-label'>Millennials Want Health</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Competitive White Space")
    st.markdown("#### Gap Identified")
    st.markdown("""
    ✗ No modern Lebanese fast-casual brand in Singapore<br>
    ✗ No "Chipotle for Shawarma" equivalent<br>
    ✗ Traditional sit-down only
    """, unsafe_allow_html=True)
    
    st.markdown("#### Opportunity")
    st.markdown("""
    ✓ First-mover advantage in premium convenience<br>
    ✓ Proven demand for healthy fast-casual<br>
    ✓ Middle Eastern cuisine gaining traction
    """, unsafe_allow_html=True)
    
    st.markdown("### Financial Viability")
    st.markdown("#### Store-Level Economics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>SGD 400-500K</div>
            <div class='metric-label'>Investment</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>SGD 120,000</div>
            <div class='metric-label'>Monthly Revenue</div>
            <small>(200 customers/day)</small>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>SGD 18,000</div>
            <div class='metric-label'>Net Profit</div>
            <small>(15% margin)</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin: 2rem 0;'>
    <strong>BREAK-EVEN: 5-6 MONTHS</strong><br>
    <strong>MARKET CAPACITY: 25-30 STORES (Singapore)</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ✓ CONCLUSION")
    st.success("**Project Validated — Proceed to Full Development**")

# Deliverables
elif page == "Deliverables":
    st.markdown('<h1 class="section-header">DELIVERABLES</h1>', unsafe_allow_html=True)
    
    deliverables = [
        {
            "title": "COMPONENT 1",
            "subtitle": "Market Research & Strategic Foundation",
            "weeks": "WEEKS 1-2",
            "items": [
                "Complete Singapore F&B market analysis with data models",
                "Competitive intelligence & positioning strategy",
                "Target audience personas & psychographics",
                "Financial feasibility study & unit economics",
                "Site selection criteria & location analysis"
            ]
        },
        {
            "title": "COMPONENT 2",
            "subtitle": "Brand Development & Prototype Design",
            "weeks": "WEEKS 3-4",
            "items": [
                "Brand identity & visual system creation",
                "Menu engineering & cost optimization",
                "Store layout & kitchen workflow design",
                "Technology stack & POS integration plan",
                "Supplier identification & partnership framework"
            ]
        },
        {
            "title": "COMPONENT 3",
            "subtitle": "Operations Manual & Training System",
            "weeks": "WEEKS 5-6",
            "items": [
                "Standard operating procedures documentation",
                "Staff training curriculum & materials",
                "Quality control systems & checklists",
                "Inventory management protocols",
                "Customer service standards & scripts"
            ]
        },
        {
            "title": "COMPONENT 4",
            "subtitle": "Franchise System & Legal Framework",
            "weeks": "WEEKS 7-8",
            "items": [
                "Franchise disclosure document (FDD)",
                "Franchise agreement template",
                "Territory development strategy",
                "Marketing & sales toolkit",
                "Growth roadmap & expansion plan"
            ]
        }
    ]
    
    for deliverable in deliverables:
        st.markdown(f"### {deliverable['title']}")
        st.markdown(f"#### {deliverable['subtitle']}")
        st.markdown(f"*{deliverable['weeks']}*")
        
        for item in deliverable['items']:
            st.markdown(f"• {item}")
        
        st.markdown("---")

# Investment Structure
elif page == "Investment Structure":
    st.markdown('<h1 class="section-header">INVESTMENT STRUCTURE</h1>', unsafe_allow_html=True)
    
    st.markdown("### Fee Structure")
    st.markdown("""
    <div style='text-align: center; margin: 3rem 0;'>
        <h1 style='font-size: 4rem; color: #D4AF37;'>SGD 10,000</h1>
        <h3 style='color: #7F8C8D;'>Professional Fee</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <table style='width: 100%; border-collapse: collapse; margin: 2rem 0;'>
        <tr style='background-color: #F8F9FA;'>
            <td style='padding: 15px; border: 1px solid #DDD;'><strong>Gross Professional Fee</strong></td>
            <td style='padding: 15px; border: 1px solid #DDD; text-align: right;'><strong>SGD 10,000</strong></td>
        </tr>
        <tr>
            <td style='padding: 15px; border: 1px solid #DDD;'>Less: Personal Debt Offset</td>
            <td style='padding: 15px; border: 1px solid #DDD; text-align: right;'>-SGD 2,000</td>
        </tr>
        <tr style='background-color: #D4AF37; color: white;'>
            <td style='padding: 15px; border: 1px solid #DDD;'><strong>NET PAYMENT REQUIRED</strong></td>
            <td style='padding: 15px; border: 1px solid #DDD; text-align: right;'><strong>SGD 8,000</strong></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
    
    st.markdown("### Market Context")
    st.markdown("Singapore firms: **SGD 25-40K** | Your savings: **60-70%**")
    
    st.markdown("### Payment Schedule")
    st.markdown("#### 8-Week Payment Schedule")
    
    payment_data = [
        {"Week": 1, "Milestone": "Component 1 Start", "Payment": "SGD 1,000", "Cumulative": "SGD 1,000"},
        {"Week": 2, "Milestone": "Component 1 Done", "Payment": "SGD 1,000", "Cumulative": "SGD 2,000"},
        {"Week": 3, "Milestone": "Component 2 Start", "Payment": "SGD 1,000", "Cumulative": "SGD 3,000"},
        {"Week": 4, "Milestone": "Component 2 Done", "Payment": "SGD 1,000", "Cumulative": "SGD 4,000"},
        {"Week": 5, "Milestone": "Component 3 Start", "Payment": "SGD 1,000", "Cumulative": "SGD 5,000"},
        {"Week": 6, "Milestone": "Component 3 Done", "Payment": "SGD 1,000", "Cumulative": "SGD 6,000"},
        {"Week": 7, "Milestone": "Component 4 Start", "Payment": "SGD 1,000", "Cumulative": "SGD 7,000"},
        {"Week": 8, "Milestone": "Component 4 Done", "Payment": "SGD 1,000", "Cumulative": "SGD 8,000"}
    ]
    
    st.markdown("""
    <table style='width: 100%; border-collapse: collapse; margin: 2rem 0;'>
        <tr style='background-color: #D4AF37; color: white;'>
            <th style='padding: 12px; border: 1px solid #DDD;'>WEEK</th>
            <th style='padding: 12px; border: 1px solid #DDD;'>MILESTONE</th>
            <th style='padding: 12px; border: 1px solid #DDD;'>PAYMENT</th>
            <th style='padding: 12px; border: 1px solid #DDD;'>CUMULATIVE</th>
        </tr>
    """, unsafe_allow_html=True)
    
    for i, row in enumerate(payment_data):
        bg_color = "#F8F9FA" if i % 2 == 0 else "white"
        st.markdown(f"""
        <tr style='background-color: {bg_color};'>
            <td style='padding: 12px; border: 1px solid #DDD;'>{row['Week']}</td>
            <td style='padding: 12px; border: 1px solid #DDD;'>{row['Milestone']}</td>
            <td style='padding: 12px; border: 1px solid #DDD;'>{row['Payment']}</td>
            <td style='padding: 12px; border: 1px solid #DDD;'>{row['Cumulative']}</td>
        </tr>
        """, unsafe_allow_html=True)
    
    st.markdown("</table>", unsafe_allow_html=True)
    
    st.markdown("*50% upfront / 50% upon component approval*")

# Implementation Roadmap
elif page == "Implementation Roadmap":
    st.markdown('<h1 class="section-header">IMPLEMENTATION ROADMAP</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #2C3E50, #34495E, #7F8C8D, #BDC3C7); padding: 30px; border-radius: 10px; color: white; text-align: center; margin: 2rem 0;'>
        <h3>PHASE 2 → YEAR 1 → YEAR 2 → YEAR 3+</h3>
        <p>Development → Validation → Franchise → Expansion</p>
        <p>Weeks 1-8 → 1 Store → Launch System → Regional</p>
    </div>
    """, unsafe_allow_html=True)
    
    phases = [
        {
            "title": "PHASE 2: DEVELOPMENT",
            "duration": "Weeks 1-8",
            "description": "Strategic foundation and franchise system creation",
            "activities": [
                "Complete market research and validation",
                "Develop brand identity and prototype",
                "Create operations manual and training systems",
                "Build franchise legal framework",
                "Prepare for pilot launch"
            ]
        },
        {
            "title": "YEAR 1: VALIDATION",
            "duration": "Pilot Store Launch",
            "description": "Prove concept with first location",
            "activities": [
                "Site selection and lease negotiation",
                "Store construction and setup",
                "Staff recruitment and training",
                "Soft opening and operations refinement",
                "Performance optimization"
            ]
        },
        {
            "title": "YEAR 2: FRANCHISE LAUNCH",
            "duration": "System Rollout",
            "description": "Scale through franchise partnerships",
            "activities": [
                "Franchise marketing and recruitment",
                "Franchisee selection and training",
                "Multi-unit development agreements",
                "Support infrastructure development",
                "Brand building campaigns"
            ]
        },
        {
            "title": "YEAR 3+: EXPANSION",
            "duration": "Regional Growth",
            "description": "Geographic and market expansion",
            "activities": [
                "International market entry",
                "Corporate store development",
                "Supply chain optimization",
                "Technology platform enhancement",
                "Strategic partnerships"
            ]
        }
    ]
    
    for phase in phases:
        st.markdown(f"### {phase['title']}")
        st.markdown(f"*{phase['duration']}*")
        st.markdown(f"**{phase['description']}**")
        
        for activity in phase['activities']:
            st.markdown(f"• {activity}")
        
        st.markdown("---")

# Partnership Terms
elif page == "Partnership Terms":
    st.markdown('<h1 class="section-header">PARTNERSHIP TERMS</h1>', unsafe_allow_html=True)
    
    st.markdown("### Scope & Future Collaboration")
    st.markdown("**Scope:** 8-week strategic development")
    st.markdown("**Future collaboration:** TBD after Store #1 success")
    
    st.markdown("### Client Protection")
    st.markdown("""
    ✓ **2 revision rounds per component**<br>
    ✓ **Exit option after any component**<br>
    ✓ **All work remains your property**
    """, unsafe_allow_html=True)
    
    st.markdown("### Deliverables Timeline")
    st.markdown("All components delivered within 8 weeks of project commencement")

# Next Steps
elif page == "Next Steps":
    st.markdown('<h1 class="section-header">NEXT STEPS</h1>', unsafe_allow_html=True)
    
    steps = [
        "1. Review and approve proposal",
        "2. Sign acceptance agreement", 
        "3. Initial payment (SGD 1,000)",
        "4. Kick-off meeting (Week 1)",
        "5. Begin Component 1 delivery"
    ]
    
    for step in steps:
        st.markdown(f"<div class='timeline-item'><strong>{step}</strong></div>", unsafe_allow_html=True)
    
    st.markdown("### PROPOSED START: **Next Week**")

# Signature Page
elif page == "Signature Page":
    st.markdown('<h1 class="section-header">ACCEPTANCE & AGREEMENT</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### CLIENT")
        st.markdown("_____________________")
        st.markdown("**Angeles Herrero**")
        st.markdown("Kazbar")
        st.markdown("Date: _________________")
    
    with col2:
        st.markdown("### CONSULTANT")
        st.markdown("_____________________")
        st.markdown("**Ken Holden**")
        st.markdown("MBBB Capital Consulting")
        st.markdown("Date: _________________")
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; margin-top: 3rem;'>
        <strong>Ken Holden</strong><br>
        MBBB Capital Consulting<br>
        Strategic Franchise Development<br>
        October 2025
    </div>
    """, unsafe_allow_html=True)
