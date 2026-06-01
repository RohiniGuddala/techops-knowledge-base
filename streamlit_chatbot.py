"""
RODL Knowledge Chatbot - Streamlit Version
Deploy to Streamlit Community Cloud for free one-link access.

To run locally: streamlit run streamlit_chatbot.py
"""
import streamlit as st
from difflib import SequenceMatcher

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="TechOps Knowledge Base",
    page_icon="🔍",
    layout="centered"
)

# ============================================================
# KNOWLEDGE BASE - Add/edit your team's data here
# ============================================================

KNOWLEDGE_BASE = [
    {
        "section": "Retail Operations DL",
        "topic": "Lab Web Resource Links",
        "content": "Ansible site, SITAD iron foundation, QTest login, Replace new lanes with commas, WFM Store-Search, TechOps Onboarding",
        "links": [
            {"text": "qTest - Login", "url": "https://wfm.qtestnet.com/portal/loginform?redirect=https%3A%2F%2Fwfm.qtestnet.com%2Fportal%2Fproject"},
            {"text": "Replace new lines with commas Online", "url": "https://convert.town/replace-new-lines-with-commas"},
            {"text": "Retail Infrastructure - TechOps Onboarding", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/TechOps%20Onboarding.aspx"}
        ]
    },
    {
        "section": "Retail Operations DL",
        "topic": "Lab Env & Networking Documents",
        "content": "Lab Touchpoint Standard List, East Block Building Lab Network Information, Las Cimas Tech Lab Switchport VLAN Assignments, Tech Arch Environment Summary",
        "links": [
            {"text": "Lab Touchpoint Standard List.xlsx", "url": "https://wholefoods.sharepoint.com/:x:/r/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/_layouts/15/Doc.aspx?sourcedoc=%7B99BB44DE-1B98-4E1F-A701-6E7D8163DE97%7D&file=New%20Lab%20Standard%20-%20Rebuild%20List.xlsx&action=default&mobileredirect=true&web=1"},
            {"text": "East Block Building - Lab Network Information.xlsx", "url": "https://wholefoods.sharepoint.com/:x:/s/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/EUpkhmidsztDqGe1Kjcw9KkBwTxaAgFbDNrl_hCoKUZIOg"},
            {"text": "Las Cimas Tech Lab - Switchport VLAN Assignments.xlsx", "url": "https://wholefoods.sharepoint.com/:x:/r/sites/TechRetailMerchSC/_layouts/15/Doc.aspx?sourcedoc=%7B80CEB941-DBFE-4CF3-9D2F-6271A21A104F%7D&file=Las%20Cimas%20Tech%20Lab%20-%20Switchport%20VLAN%20Assignments.xlsx"},
            {"text": "Tech Arch Environment Summary.xlsx", "url": "https://wholefoods.sharepoint.com/:x:/r/sites/TechRetailMerchSC/_layouts/15/Doc.aspx?sourcedoc=%7BDB050026-33F7-4B55-90D8-2151A9A6F661%7D&file=Tech%20Arch%20Environment%20Summary.xlsx"}
        ]
    },
    {
        "section": "Retail Operations DL",
        "topic": "Service Request Portals",
        "content": "Orchard now - Retail Infrastructure Service Request portal for submitting service requests",
        "links": [
            {"text": "Retail Infrastructure Service Request - Employee Center", "url": "https://wfmprod.service-now.com/wfm?id=sc_cat_item&sys_id=196c15f81b478190453c97d8b04bcbc1"}
        ]
    },
    {
        "section": "Retail Operations DL",
        "topic": "Office Client Quick Links",
        "content": "QA1 office client, QA2 office client, QA8 office client, SBI office client, T22 office client, T56 office client",
        "links": []
    },
    {
        "section": "Retail Operations DL",
        "topic": "Lab Procedures",
        "content": "ECO Carts, AWS Troubleshooting and Resources, Change or Disable ESB Config for HQ, Create a Direct Membership Rule, Deploy an IMG TS for WDP SFS KRS Devices, Evaluation Cycles after a Deployment, Lab Badge Audit, Lab Environment Structure, Log Review for Lanes and Servers, New Computer On-Boarding, OnePOS Updates Windows Updates, Promoting IMG Task Sequences and Applications, PRP Deployment Process, Requesting Engineering Engagement, Reset SN/PN with DMI USB Tool, R10 and SCO Upgrade/Downgrade Ansible Playbook Commands, SCCM Basics, Spooky Troubleshooting, Stage Collections and Deployments, Troubleshooting Lanes and Servers",
        "links": [
            {"text": "ECO Carts", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/ECO-Carts.aspx?web=1"},
            {"text": "AWS Troubleshooting and Resources", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/AWS.aspx"},
            {"text": "Change or Disable ESB Config for HQ", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Change-ESB-Config-for-HQ.aspx"},
            {"text": "Create a Direct Membership Rule", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Create-a-Direct-Membership-Rule.aspx"},
            {"text": "Deploy an IMG TS for WDP - SFS - KRS Devices", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Deploy-IMG-TS-for-WDP---SFS---KRS-Devices.aspx"},
            {"text": "Evaluation Cycles after a Deployment", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Evaluation-Cycles-after-a-Deployment.aspx"},
            {"text": "Lab Badge Audit", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Lab-Badge-Audit.aspx"},
            {"text": "Lab Environment Structure", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Lab-Environment-Structure.aspx"},
            {"text": "Log Review for Lanes and Servers", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Log-Review-for-Lanes-and-Servers.aspx"},
            {"text": "New Computer On-Boarding", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/New-Computer-On-Boarding.aspx"},
            {"text": "OnePOS Updates (Windows Updates)", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/OnePOS-Updates.aspx"},
            {"text": "Promoting IMG Task Sequences and Applications", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Promoting-IMG-Task-Sequences-and-Applications.aspx"},
            {"text": "PRP Deployment Process", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/PRP.aspx"},
            {"text": "Requesting Engineering Engagement", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Requesting-Engineering-Engagement.aspx"},
            {"text": "Reset SN/PN with DMI USB Tool", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Reset-SN-PN-with-DMI-USB-Tool.aspx"},
            {"text": "R10 and SCO Upgrade/Downgrade (Ansible Playbook Commands)", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Upgrade-Downgrade-R10-%26-SCO.aspx"},
            {"text": "SCCM Basics", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/SCCM-Basics.aspx"},
            {"text": "Spooky Troubleshooting", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Spooky.aspx"},
            {"text": "Stage Collections and Deployments", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Stage%20Collections%20and%20Deployments.aspx"},
            {"text": "Troubleshooting Lanes and Servers", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Troubleshooting-Lanes-and-Servers.aspx"}
        ]
    },
    {
        "section": "Retail Operations DL",
        "topic": "Package Repo Directory",
        "content": "ATCI Physical Lanes (Ansible): \\\\idcwp6202\\Packages | ATX Physical Lanes (Ansible): \\\\cewd6208\\packages | AWS Virtual Lanes (Ansible): \\\\aldue1asgs301.retail-npe.wfm.global\\ris-packagesrepo-npe | SCCM: \\\\awdue1aCMCONTENT.wfm.pvt\\CM_DML\\PCI\\Prod\\Software | Ansible Tools: \\\\Awdrisjmp001\\d$\\AnsibleTools\\Package Lists",
        "links": []
    },
    {
        "section": "Retail Operations DL",
        "topic": "Retail Infrastructure",
        "content": "Retail Infrastructure Home, Environment Plan, RI Technical Architecture Networking, RI New Store Onboarding, Account lockout Report, Retail splunk PRD, Retail splunk Dev",
        "links": [
            {"text": "Retail Infrastructure Home", "url": "https://wholefoods.sharepoint.com/:u:/r/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/Retail%20Infrastructure%20Home%20Page.aspx?csf=1&web=1&e=JVs6Aq"},
            {"text": "Environment Plan - All Documents", "url": "https://wholefoods.sharepoint.com/sites/TechRetailMerchSC/Technical%20Architecture/Forms/AllItems.aspx?as=json&FolderCTID=0x012000766787390FC1CB408FA9FD4441CA4820&id=%2Fsites%2FTechRetailMerchSC%2FTechnical%20Architecture%2FEnvironment%20Plan"},
            {"text": "RI Technical Architecture - Networking", "url": "https://wholefoods.sharepoint.com/sites/TechRetailMerchSC/Technical%20Architecture/Forms/AllItems.aspx?as=json&FolderCTID=0x012000766787390FC1CB408FA9FD4441CA4820&id=%2Fsites%2FTechRetailMerchSC%2FTechnical%20Architecture%2FNetworking"},
            {"text": "RI New Store Onboarding - Filter Out Completed", "url": "https://wholefoods.sharepoint.com/sites/TechRetailMerchSC/Lists/New%20Store%20Onboarding/Filter%20Out%20Completed.aspx"},
            {"text": "Retail Infrastructure", "url": "https://wholefoods.sharepoint.com/sites/TechRetailMerchSC/SitePages/RetailInfra.aspx"}
        ]
    },
    {
        "section": "POS Infrastructure",
        "topic": "POSInfra Knowledge Docs",
        "content": "POS Infrastructure knowledge documentation and articles",
        "links": [
            {"text": "POS Infra Knowledge Docs", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/POS-Infra-KBAs.aspx?csf=1&web=1&e=pySTjQ"}
        ]
    },
    {
        "section": "POS Infrastructure",
        "topic": "POS Infrastructure Lab",
        "content": "Lab environment for POS Infrastructure testing",
        "links": [
            {"text": "POS Infrastructure Lab", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/POS-Infrastructure-Lab.aspx"}
        ]
    },
    {
        "section": "POS Infrastructure",
        "topic": "Splunk Views",
        "content": "POS Infrastructure Splunk monitoring reports and dashboards",
        "links": [
            {"text": "Splunk Views", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/POSInfra-Splunk-Reports.aspx"}
        ]
    },
    {
        "section": "POS Infrastructure",
        "topic": "Windows Server 2019 SVR Rebuild Project",
        "content": "Server rebuild project documentation for Windows Server 2019",
        "links": [
            {"text": "Windows Server 2019 SVR Rebuild Project", "url": "https://wholefoods.sharepoint.com/sites/6ff0f6a5-b205-4cc5-b489-6c8af38d51c5/SitePages/2019-SVR-Rebuild-Project.aspx"}
        ]
    }
]


# ============================================================
# SEARCH ENGINE
# ============================================================

def fuzzy_match(query, text, threshold=0.5):
    query_lower = query.lower()
    text_lower = text.lower()
    if query_lower in text_lower:
        return 1.0
    for qword in query_lower.split():
        for tword in text_lower.split():
            ratio = SequenceMatcher(None, qword, tword).ratio()
            if ratio >= threshold:
                return ratio
    return 0.0


def search(query):
    if not query.strip():
        return []

    query_lower = query.strip().lower()
    results = []

    for entry in KNOWLEDGE_BASE:
        score = 0.0
        matched_links = []

        # Check topic, content, section
        if query_lower in entry["topic"].lower():
            score = 1.0
        if query_lower in entry["content"].lower():
            score = max(score, 1.0)
        if query_lower in entry["section"].lower():
            score = max(score, 0.9)

        # Check links
        for link in entry.get("links", []):
            if query_lower in link["text"].lower():
                score = max(score, 1.0)
                matched_links.append(link)

        # Fuzzy fallback
        if score == 0:
            fs = fuzzy_match(query, entry["content"])
            ts = fuzzy_match(query, entry["topic"])
            score = max(fs, ts) * 0.7

        if score > 0.4:
            result = dict(entry)
            if matched_links:
                result["links"] = matched_links
            elif entry.get("links"):
                relevant = [l for l in entry["links"] if query_lower in l["text"].lower()]
                result["links"] = relevant if relevant else []
            results.append({"entry": result, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    if results and results[0]["score"] == 1.0:
        results = [r for r in results if r["score"] >= 0.8]
    return results[:5]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .chat-header {
        text-align: center;
        padding: 20px 0;
        border-bottom: 2px solid #1e3a5f;
        margin-bottom: 20px;
    }
    .chat-header h1 {
        color: #e94560;
        font-size: 2em;
        margin: 0;
    }
    .chat-header p {
        color: #8892b0;
        margin-top: 5px;
    }
    .result-card {
        background: #1a2332;
        border: 1px solid #1e3a5f;
        border-radius: 12px;
        padding: 16px;
        margin: 10px 0;
    }
    .result-card .section-tag {
        background: #e94560;
        color: white;
        padding: 3px 10px;
        border-radius: 4px;
        font-size: 0.75em;
        font-weight: bold;
    }
    .result-card .topic {
        color: #ccd6f6;
        font-size: 1.1em;
        font-weight: bold;
        margin: 10px 0 5px 0;
    }
    .result-card .content {
        color: #8892b0;
        font-size: 0.9em;
        margin: 5px 0;
    }
    .result-card .link-item {
        color: #4fc3f7;
        text-decoration: none;
        display: block;
        padding: 4px 0;
        font-size: 0.9em;
    }
    .result-card .link-item:hover {
        text-decoration: underline;
    }
    div[data-testid="stChatMessage"] {
        background: #1a2332;
        border: 1px solid #1e3a5f;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# CHAT UI
# ============================================================

st.markdown("""
<div class="chat-header">
    <h1>🔍 TechOps Knowledge Base</h1>
    <p>Search documents, procedures, links, and resources — powered by your team's knowledge</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Search for documents, links, or topics... (e.g., SCCM, Splunk, Deploy, PRP)"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Search and respond
    results = search(prompt)

    response_html = ""
    if not results:
        response_html = f"❌ No results found for **\"{prompt}\"**. Try different keywords or check spelling."
    else:
        response_html = f"**Found {len(results)} result(s):**\n\n"
        for r in results:
            entry = r["entry"]
            response_html += f"---\n"
            response_html += f"📂 `{entry['section']}` → **{entry['topic']}**\n\n"
            response_html += f"{entry['content']}\n\n"
            if entry.get("links"):
                for link in entry["links"]:
                    response_html += f"🔗 [{link['text']}]({link['url']})\n\n"

    st.session_state.messages.append({"role": "assistant", "content": response_html})
    with st.chat_message("assistant"):
        st.markdown(response_html, unsafe_allow_html=True)
