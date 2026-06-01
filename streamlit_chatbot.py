"""
TechOps Knowledge Base - Streamlit Chatbot
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
    layout="wide"
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
# GENERIC RESPONSES
# ============================================================

GREETINGS = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "howdy", "sup", "what's up", "yo"]
HELP_WORDS = ["help", "what can you do", "how to use", "commands", "guide", "instructions"]
THANKS_WORDS = ["thanks", "thank you", "thx", "ty", "appreciate"]

ALL_TOPICS = sorted(set(entry["topic"] for entry in KNOWLEDGE_BASE))
ALL_SECTIONS = sorted(set(entry["section"] for entry in KNOWLEDGE_BASE))


def get_generic_response(query):
    """Handle generic/conversational messages."""
    q = query.strip().lower()

    if any(g in q for g in GREETINGS):
        topics_list = "\n".join(f"  - {t}" for t in ALL_TOPICS)
        return (
            "👋 **Hello! Welcome to TechOps Knowledge Base.**\n\n"
            "I can help you find documents, procedures, links, and resources.\n\n"
            "**Try searching for:**\n"
            "- A topic: `SCCM`, `Splunk`, `Ansible`, `POS`\n"
            "- A procedure: `Troubleshooting`, `Deploy`, `Onboarding`\n"
            "- A document: `Lab Network`, `VLAN`, `Package Repo`\n\n"
            f"**Available topics:**\n{topics_list}"
        )

    if any(h in q for h in HELP_WORDS):
        return (
            "ℹ️ **How to use TechOps Knowledge Base:**\n\n"
            "1. Type a **keyword** in the search box below (e.g., `SCCM`, `Splunk`, `PRP`)\n"
            "2. I'll find matching documents, procedures, and links\n"
            "3. Click any 🔗 link to open the resource directly\n\n"
            "**Tips:**\n"
            "- Partial words work: `trouble` finds `Troubleshooting`\n"
            "- Try section names: `POS Infrastructure`, `Retail Operations`\n"
            "- Try tool names: `Ansible`, `SCCM`, `Splunk`\n\n"
            f"**Sections available:** {', '.join(ALL_SECTIONS)}"
        )

    if any(t in q for t in THANKS_WORDS):
        return "You're welcome! Let me know if you need anything else. 👍"

    if q in ["list all", "show all", "all topics", "topics", "list"]:
        topics_list = "\n".join(f"  - **{t}**" for t in ALL_TOPICS)
        return f"📋 **All available topics:**\n\n{topics_list}\n\n_Type any topic name to search._"

    return None


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

        if query_lower in entry["topic"].lower():
            score = 1.0
        if query_lower in entry["content"].lower():
            score = max(score, 1.0)
        if query_lower in entry["section"].lower():
            score = max(score, 0.9)

        for link in entry.get("links", []):
            if query_lower in link["text"].lower():
                score = max(score, 1.0)
                matched_links.append(link)

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
                result["links"] = relevant if relevant else entry["links"]
            results.append({"entry": result, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)
    if results and results[0]["score"] == 1.0:
        results = [r for r in results if r["score"] >= 0.8]
    return results[:5]


# ============================================================
# UI LAYOUT
# ============================================================

# Header
st.markdown("""
<div style="text-align:center; padding:10px 0 20px 0; border-bottom:2px solid #1e3a5f; margin-bottom:20px;">
    <h1 style="color:#e94560; margin:0;">🔍 TechOps Knowledge Base</h1>
    <p style="color:#8892b0; margin-top:8px; font-size:1.1em;">
        Search documents, procedures, links, and resources
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar with quick links
with st.sidebar:
    st.markdown("### 📂 Quick Navigation")
    st.markdown("---")
    for section in ALL_SECTIONS:
        st.markdown(f"**{section}**")
        section_topics = [e["topic"] for e in KNOWLEDGE_BASE if e["section"] == section]
        for topic in section_topics:
            st.markdown(f"- {topic}")
        st.markdown("")

    st.markdown("---")
    st.markdown("### 💡 Search Tips")
    st.markdown("""
    - Type keywords: `SCCM`, `Splunk`
    - Partial match: `trouble`, `deploy`
    - Type `help` for instructions
    - Type `list` to see all topics
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": (
            "👋 **Welcome to TechOps Knowledge Base!**\n\n"
            "I can help you find documents, procedures, and links.\n\n"
            "**Try searching for:** `SCCM`, `Splunk`, `Ansible`, `POS`, `Troubleshooting`, `Deploy`, `Onboarding`, `PRP`\n\n"
            "_Type a keyword below to get started._"
        )}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🔍" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type a keyword to search (e.g., SCCM, Splunk, Deploy, PRP)..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Check for generic responses first
    generic = get_generic_response(prompt)
    if generic:
        response = generic
    else:
        # Search knowledge base
        results = search(prompt)

        if not results:
            response = (
                f"❌ No results found for **\"{prompt}\"**.\n\n"
                "**Suggestions:**\n"
                "- Try shorter keywords (e.g., `SCCM` instead of `SCCM Basics`)\n"
                "- Check spelling\n"
                "- Type `list` to see all available topics\n"
                "- Type `help` for usage tips"
            )
        else:
            response = f"✅ **Found {len(results)} result(s) for \"{prompt}\":**\n\n"
            for r in results:
                entry = r["entry"]
                response += f"---\n"
                response += f"### 📂 {entry['topic']}\n"
                response += f"**Section:** {entry['section']}\n\n"
                response += f"{entry['content']}\n\n"
                if entry.get("links"):
                    response += "**Links:**\n"
                    for link in entry["links"]:
                        response += f"- 🔗 [{link['text']}]({link['url']})\n"
                    response += "\n"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="🔍"):
        st.markdown(response)

