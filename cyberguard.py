import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import requests
import json
import sys
import os
import colorama
from time import sleep 
import json
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import sentence_transformers
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser








st.title("CYBER-GUARD")

# loader=PyPDFDirectoryLoader("./knowledgebase_for_chatbot/")
# data = loader.load()
# # #split the extracted data into text chunks using the text_splitter, which splits the text based on the specified number of characters and overlap
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# text_chunks = text_splitter.split_documents(data)
# # #download the embeddings to use to represent text chunks in a vector space, using the pre-trained model "sentence-transformers/all-MiniLM-L6-v2"
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# # # # # create embeddings for each text chunk using the FAISS class, which creates a vector index using FAISS and allows efficient searches between vectors
# vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)

# vector_store.save_local("faiss_index")

# new_vector_store = FAISS.load_local(
#     "faiss_index", embeddings, allow_dangerous_deserialization=True
# )



# Retrieve and generate using the relevant snippets of the blog.
retriever = new_vector_store.as_retriever()

from langchain_groq import ChatGroq
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY
)

prompt = hub.pull("rlm/rag-prompt")
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY
)

prompt = hub.pull("rlm/rag-prompt")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


#######################################################################
# colorama.init()
# def type(words: str):
#     for char in words:
#         sleep(0.015)
#         sys.stdout.write(char)
#         sys.stdout.flush()
#     # print()

# url = r'https://www.virustotal.com/vtapi/v2/file/scan'
# api= os.getenv("VT_API_KEY")
#######################################################################


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data

selection=st.sidebar.selectbox("Select",("Dashboard","Cyber Awareness Chatbot","Malicious File Scanner","Education Portal"))

if selection=="Dashboard":
    st.subheader("Welcome to Dashboard")
    sheet_name = 'Cyber Quiz (Responses)' # replace with your own sheet name
    sheet_id = '1QE9qW7DxaYp44RvTM0YUtpRFoe4GPt9i0WX-_OruXHM' # replace with your sheet's ID
    
    url=f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    df=pd.read_csv(url,names=["Timestamp","Q1","Q2"])
    # df.values
    # st.write(df.iloc[-1,1:].values)
    responses=df.iloc[-1,1:].values
    correct=[]
    # wrong=[]
    for i,j in zip(responses,["A", "A"]):
        if i==j:
            correct.append(1)
        else:
            correct.append(1)
    
    col1,col2,col3=st.columns(3)
    st.write(correct)
    with col1:
        # Display pie chart
        fig, ax = plt.subplots(figsize=(5, 5))
        # sns.barplot(correct,ax=ax)
        ax.pie(correct, labels=["Correct","Wrong"], autopct="%1.1f%%", startangle=90)
        # ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.write("Cyber Fundamental Score")
        st.pyplot(fig)
        st.write("Improve your Score [Here](https://docs.google.com/forms/d/e/1FAIpQLSeRVC8WVGSqDHN5B9_kX18RbRnS0gOFyMbKYZFqzBSGyP5rLA/viewform?usp=header)")
    with col2:
        # Display pie chart
        fig, ax = plt.subplots(figsize=(5, 5))
        # sns.barplot(correct,ax=ax)
        ax.pie(correct, labels=["Correct","Wrong"], autopct="%1.1f%%", startangle=90)
        # ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.write("Risk Awareness Score")
        st.pyplot(fig)
        st.write("Improve your Score [Here](https://docs.google.com/forms/d/e/1FAIpQLSeRVC8WVGSqDHN5B9_kX18RbRnS0gOFyMbKYZFqzBSGyP5rLA/viewform?usp=header)")
    with col3:
        # Display pie chart
        fig, ax = plt.subplots(figsize=(5, 5))
        # sns.barplot(correct,ax=ax)
        ax.pie(correct, labels=["Correct","Wrong"], autopct="%1.1f%%", startangle=90)
        # ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.
        st.write("Cyber Awareness Score")
        st.pyplot(fig)
        st.write("Improve your Score [Here](https://docs.google.com/forms/d/e/1FAIpQLSeRVC8WVGSqDHN5B9_kX18RbRnS0gOFyMbKYZFqzBSGyP5rLA/viewform?usp=header)")

    st.subheader("Cyber Security Guidelines")

    col1,col2,col3=st.columns(3)
    with col1:
        st.caption("Fundamentals")
        # st.write("The following list won’t indent no matter what I try:")
        st.markdown("- Educate yourself and enhance cyber knowlegdet")
        st.markdown("- Keep system software updated")
        st.markdown("- Use secure internet connections")
        st.markdown("- Secure web browsing and email")
        st.markdown("- Implement data retention, loss recovery capability")
        st.markdown("- Encrypt data and devices")
        st.markdown("- Secure devices that retain data")
        st.markdown("- Do not click on links you do not recognise.")
        st.markdown("- Protect your personal data.")
        st.markdown("- Be aware of where you are sending your data.")
        st.markdown("- Uninstall apps you are not using.")
        st.markdown("- Do not use public/free Wi-Fi – personal hotspots are safer.")
        st.markdown("- Use a strong, well-regarded browser. Google Chrome is the strongest in industry tests.")
        st.markdown("- Ensure that you only use apps from a reputable source.")
    with col2:
        st.caption("Essentials")
        # st.write("The following list won’t indent no matter what I try:")
        st.markdown("- Create complex passwords, protect passwords and change them regularly, do not reuse passwords across multiple systems and do not share passwords with colleagues.")
        st.markdown("- Use multi-factor authentication.")
        st.markdown("- Do not use public/free Wi-Fi – personal hotspots are safer.")
        st.markdown("- Use VPN and dongles (small, removable devices that have secure access to wireless broadband) when travelling.")
        st.markdown("- Put a Firewall")
        st.markdown("- Use Proxies")
        st.markdown("- Analyze Ads Carefully - Don't click it in exctiment")

        
        st.markdown("- Disable Multiple file downloads")
        st.markdown("- Don't Download Zipped/Compressed files")
        st.markdown("- Use Pen/USB drives carefully")
        st.markdown("- Regularly Scan your system for malwares")
        st.markdown("- Run Regular Data Backups")
        st.markdown("- Execute Automatic Security Updates")




    with col3:
        st.caption("Critical")
        # st.write("The following list won’t indent no matter what I try:")
        st.markdown("- Turn on your browser’s popup blocker. A popup blocker should be enabled at all times while browsing the internet.")
        st.markdown("- Do not use public phone chargers to avoid the risk of ‘juice jacking’.")
        st.markdown("- Check for ‘https:’ or a padlock icon on your browser’s URL bar to verify that a site is secure before entering any personal information.")
        st.markdown("- Understand the permissions you are granting to apps (eg, tracking your location and access to your contacts or camera).")
        st.markdown("- Report all phishing/spear phishing to the person designated to deal with cybersecurity concerns, even if the email is sent to your personal account rather than work.")
        st.markdown("- Uninstall apps you are not using.")
        st.markdown("- Do not use public/free Wi-Fi – personal hotspots are safer.")
        st.markdown("- Use VPN and dongles (small, removable devices that have secure access to wireless broadband) when travelling.")
        st.markdown("- Ensure that you only use apps from a reputable source.")
        st.markdown("- Limit login attempts")

    












    
    st.write("Latest Cyber Attacks")
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown('''
        <a href="https://www.securityweek.com/starbucks-grocery-stores-hit-by-blue-yonder-ransomware-attack/">
            <img src="https://www.securityweek.com/wp-content/uploads/2024/01/Supply-Chain-Software-Attack.jpg" width="500" height="200" />
        </a>''',
        unsafe_allow_html=True
        )
        st.caption("Starbucks, Grocery Stores Hit by Blue Yonder Ransomware Attack")
    with col2:
        st.markdown('''
        <a href="https://www.securityweek.com/hackers-stole-1-49-billion-in-cryptocurrency-to-date-in-2024/">
            <img src="https://www.securityweek.com/wp-content/uploads/2024/01/cryptocurrency.jpeg" width="500" height="200" />
        </a>''',
        unsafe_allow_html=True
        )
        st.caption("Hackers Stole $1.49 Billion in Cryptocurrency to Date in 2024")
    with col3:
        st.markdown('''
        <a href="https://www.securityweek.com/new-google-project-aims-to-become-global-clearinghouse-for-scam-fraud-data/">
            <img src="https://www.securityweek.com/wp-content/themes/zoxpress-child/assets/img/posts/security-week-post-0.jpg" width="500" height="200" />
        </a>''',
        unsafe_allow_html=True
        )
        st.caption("New Google Project Aims to Become Global Clearinghouse for Scam, Fraud Data")




if selection=="Cyber Awareness Chatbot":
    st.subheader("Cyber Awareness Chatbot")
    # query=st.text_input("Write Query Here")
    # if st.button("Submit"):
    #     st.write(rag_chain.invoke(query))
# if selection=="Malicious File Scanner":
#     st.subheader("Malicious File Scanner")
#     file=st.file_uploader("Select a File")
#     if file!=None and st.button("Analyze"):     
#         with open(file.name, mode='wb') as w:
#                 w.write(file.getvalue())
        
#         file_to_upload = {"file": open(file.name, "rb")}
        
#         response = requests.post(url,files = file_to_upload , params=params)
#         file_url = f"https://www.virustotal.com/api/v3/files/{(response.json())['sha1']}"
        
#         headers = {"accept": "application/json", "x-apikey": api}
#         type(colorama.Fore.YELLOW + "Analysing....")
        
#         response = requests.get(file_url,headers=headers)
        
#         report = response.text
#         report = json.loads(report)
#         # json_string = json.dumps(report)
        
#         st.write(response)


# https://youtu.be/Yr0xPVFcf-U?si=xNHedIZgSQbUc9f_

if selection=="Education Portal":
    st.subheader("Welcome to Education Portal")

    st.write("")

    st.html(
    "<h4>Fundamentals</h4>")

    col1,col2=st.columns(2)
    with col1:
        st.caption("What is Cybercrime?")
        st.video("https://youtu.be/X7kFAy1E8Jw?si=lKWx-y3Tz1_dsSQP")
    with col2:
        st.caption("What is Cybersecurity?")
        st.video("https://youtu.be/Yr0xPVFcf-U?si=xNHedIZgSQbUc9f_")

    col1,col2=st.columns(2)
    with col1:
        st.caption("Malware and its types")
        st.video("https://youtu.be/n8mbzU0X2nQ?si=rqCjBFgrcmsj3WEw")
    with col2:
        st.caption("Tip for online data security")
        st.video("https://youtu.be/aO858HyFbKI?si=K7mDm_E4WysamUuK")
        
    with st.expander("More"):
        st.write("")

        col1,col2=st.columns(2)
        with col1:
            st.caption("How to Protect yourself against cybercrime?")
            st.video("https://youtu.be/EHqXMxY4_Nk?si=gyIz1gJhS2EfoHMr")
        with col2:
            st.caption("Why do cybercriminals want your computer?")
            st.video("https://youtu.be/NZ21QKzZtcI?si=rgaYN3mGvn-j-jT1")
        
        col1,col2=st.columns(2)
        with col1:
            st.caption("How to protect your accounts?")
            st.video("https://youtu.be/FuAs931mG08?si=hWlGuNgtkgGHryvn")
        with col2:
            st.caption("How you leak your data online?")
            st.video("https://youtu.be/Meh6NtQ-8iA?si=0eyMtMP-vo-IfgiQ")

        col1,col2=st.columns(2)
        with col1:
            st.caption("What is ransomware?")
            st.video("https://youtu.be/Vkjekr6jacg?si=NK_flkc0lXvLdQcy")
        with col2:
            st.caption("What is social engineering?")
            st.video("https://youtu.be/uvKTMgWRPw4?si=mCMtBaddyfM0OTU5")
    
        col1,col2=st.columns(2)
        with col1:
            st.caption("How to protect your privacy online?")
            st.video("https://youtu.be/JO55V34EnK8?si=4GKhg5ZxyHrYa21m")
        with col2:
            st.caption("How to protect your digital vallet?")
            st.video("https://youtu.be/2UMdkiXcMGU?si=1KUITh02f7AU8Ovr")
    
        col1,col2=st.columns(2)
        with col1:
            st.caption("How to configure privacy in Facebook?")
            st.video("https://youtu.be/ht9OmCJnxnA?si=JXf726uxyPtcU-qL")
        with col2:
            st.caption("How to configure privacy in Instagram?")
            st.video("https://youtu.be/ZcQzqdnkKvk?si=g5O2DzZG-Z4HNhCu")


    st.html(
    "<h4>Essentials</h4>")

#How to create a strong password?
# https://youtu.be/TvrFpAFitQ0?si=wiz21Gn_w94sH5F9
# Phishing
# https://youtu.be/00hpRjfbM0A?si=OiQ52JrL0qe6eJ6b
# Top 4 cyber fraud red flags
# https://youtu.be/wHdLB_tHNVo?si=pLAehEzj4zzfZa4e
#spoofing and indentity theft
# https://youtu.be/ULiinB6nMPw?si=7__iJrCQsN7CKsdm
# what is proxy server?
# https://youtu.be/5cPIukqXe5w?si=djHvp2rs3GybcwWO
# what is firewall?
# https://youtu.be/kDEX1HXybrU?si=WnoyRM9_98_MZ3zM
# VPN Explained
# https://youtu.be/R-JUOpCgTZc?si=AVQ0AVVWYpdJtP9E
# Data privacy and GDPR
#https://youtu.be/hk-ZgRIYYXc?si=QPGmg7l0eU6FPvoL
#Physical Security
# https://youtu.be/tYapnGMrzp8?si=bPApRizw6lh4GJmy
# social networks security risk
# https://youtu.be/IVgobw7JFeE?si=UGi6mA0Sat4ihMVY

    col1,col2=st.columns(2)
    with col1:
        st.caption("How to create a strong password?")
        st.video("https://youtu.be/TvrFpAFitQ0?si=wiz21Gn_w94sH5F9")
    with col2:
        st.caption("What is Phishing?")
        st.video("https://youtu.be/00hpRjfbM0A?si=OiQ52JrL0qe6eJ6b")

    col1,col2=st.columns(2)
    with col1:
        st.caption("What is Spoofing and Indentity theft?")
        st.video("https://youtu.be/ULiinB6nMPw?si=7__iJrCQsN7CKsdm")
    with col2:
        st.caption("what is proxy server?")
        st.video("https://youtu.be/5cPIukqXe5w?si=djHvp2rs3GybcwWO")
        
    with st.expander("More"):
        st.write("")

        col1,col2=st.columns(2)
        with col1:
            st.caption("VPN Explained")
            st.video("https://youtu.be/R-JUOpCgTZc?si=AVQ0AVVWYpdJtP9E")
        with col2:
            st.caption("How Social Networks are  Security Risk?")
            st.video("https://youtu.be/IVgobw7JFeE?si=UGi6mA0Sat4ihMVY")

        col1,col2=st.columns(2)
        with col1:
            st.caption("What is firewall?")
            st.video("https://youtu.be/kDEX1HXybrU?si=WnoyRM9_98_MZ3zM")
        with col2:
            st.caption("Top 4 cyber fraud red flags")
            st.video("https://youtu.be/wHdLB_tHNVo?si=pLAehEzj4zzfZa4e")

        col1,col2=st.columns(2)
        with col1:
            
            st.caption("What is Zero day attack?")
            st.video("https://youtu.be/1wul_zBphpY?si=SmMaNlRvto-g_9tI")
        with col2:
            st.caption("Physical Security")
            st.video("https://youtu.be/tYapnGMrzp8?si=bPApRizw6lh4GJmy")


    
        
    st.html("<h4>Critical</h4>")

    col1,col2=st.columns(2)
    with col1:
        st.caption("Different types of AI/ML-powered cybercrimes")
        st.video("https://youtu.be/X7kFAy1E8Jw?si=lKWx-y3Tz1_dsSQP")
    with col2:
        st.caption("How to respond to a network breach?")
        st.video("https://youtu.be/Yr0xPVFcf-U?si=xNHedIZgSQbUc9f_")

    col1,col2=st.columns(2)
    with col1:
        st.caption("Top 5 security checklist for OT devices")
        st.video("https://youtu.be/n8mbzU0X2nQ?si=rqCjBFgrcmsj3WEw")
    with col2:
        st.caption("How to do Secure remote working?")
        st.video("https://youtu.be/aO858HyFbKI?si=K7mDm_E4WysamUuK")
        
    with st.expander("More"):
        st.write("")

        col1,col2=st.columns(2)
        with col1:
            st.caption("Data privacy and GDPR")
            st.video("https://youtu.be/hk-ZgRIYYXc?si=QPGmg7l0eU6FPvoL")
        with col2:
            st.caption("Why do cybercriminals want your computer?")
            st.video("https://youtu.be/NZ21QKzZtcI?si=rgaYN3mGvn-j-jT1")
        
        
#https://youtu.be/hk-ZgRIYYXc?si=QPGmg7l0eU6FPvoL


# Different types of AI/ML-powered cybercrimes
# https://youtu.be/1Z_dh9Xgtq0?si=DZq0Mg2yJM7SHgcJ

# How to respond to a network breach?
# https://youtu.be/0_2P_trzFsQ?si=_iO2hdmGjMNN9iu0


# Top 5 security checklist for OT devices
# https://youtu.be/-aV0ZCRq_0g?si=BFZS4wYZqJ4rlQRp



# Secure remote working
# https://youtu.be/F-U_7CGYiHQ?si=6GWZp6RGeFkxeYaZ

# Zero day attack
# https://youtu.be/1wul_zBphpY?si=SmMaNlRvto-g_9tI



# Top 5 cloud security best practices checklist
# https://youtu.be/ISkw0MwP2UA?si=AMiYkXKGdWTRc2zA
    
#     col1,col2=st.columns(2)
#     with col1:
#         st.markdown('''
#         <a href="https://www.ftc.gov/system/files/attachments/cybersecurity-small-business/cybersecuirty_sb_factsheets_all.pdf">
#             <img src="https://devtorium.com/wp-content/webp-express/webp-images/uploads/2023/01/services_security_illustration.png.webp" width="250" height="200" />
#         </a>''',
#         unsafe_allow_html=True
#         )
#         st.caption("Cyber Security Basics")
#     with col2:
#         st.markdown('''
#         <a href="https://www.ibanet.org/MediaHandler?id=2F9FA5D6-6E9D-413C-AF80-681BAFD300B0">
#             <img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/97/88/76/9788767b-054e-b968-d21a-9180e80c77de/AppIcon-0-0-1x_U007emarketing-0-7-0-0-85-220.png/512x512bb.jpg" width="200" height="200" />
#         </a>''',
#         unsafe_allow_html=True
#         )
#         st.caption("Cyber Security Guidlines")



#         url="https://docs.google.com/forms/d/e/1FAIpQLSeRVC8WVGSqDHN5B9_kX18RbRnS0gOFyMbKYZFqzBSGyP5rLA/viewform?usp=header"
#     st.write("Test Your Cyber Knowledge [Here](https://docs.google.com/forms/d/e/1FAIpQLSeRVC8WVGSqDHN5B9_kX18RbRnS0gOFyMbKYZFqzBSGyP5rLA/viewform?usp=header)")
    
# # st.markdown("Test your Knowledge" %url)
     
