import pandas as pd
import numpy as np
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
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import sentence_transformers
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser








st.title("CYBER-GUARD")

loader=PyPDFLoader("guide-to-the-general-data-protection-regulation-gdpr-1-1.pdf")
data = loader.load()
#split the extracted data into text chunks using the text_splitter, which splits the text based on the specified number of characters and overlap
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_chunks = text_splitter.split_documents(data)
#download the embeddings to use to represent text chunks in a vector space, using the pre-trained model "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# # create embeddings for each text chunk using the FAISS class, which creates a vector index using FAISS and allows efficient searches between vectors
vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)
# Retrieve and generate using the relevant snippets of the blog.
retriever = vector_store.as_retriever()

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
colorama.init()
def type(words: str):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    # print()

url = r'https://www.virustotal.com/vtapi/v2/file/scan'
api= os.getenv("VT_API_KEY")
#######################################################################




selection=st.sidebar.selectbox("Select",("Cyber Awareness Chatbot","Malicious File Scanner"))

if selection=="Cyber Awareness Chatbot":
    st.subheader("Cyber Awareness Chatbot")
    query=st.text_input("Write Query Here")
    if st.button("Submit"):
        st.write(rag_chain.invoke(query))
if selection=="Malicious File Scanner":
    st.subheader("Malicious File Scanner")
    file=st.file_uploader("Select a File")
    if file!=None and st.button("Analyze"):     
        with open(file.name, mode='wb') as w:
                w.write(file.getvalue())
        
        file_to_upload = {"file": open(file.name, "rb")}
        
        response = requests.post(url,files = file_to_upload , params=params)
        file_url = f"https://www.virustotal.com/api/v3/files/{(response.json())['sha1']}"
        
        headers = {"accept": "application/json", "x-apikey": api}
        type(colorama.Fore.YELLOW + "Analysing....")
        
        response = requests.get(file_url,headers=headers)
        
        report = response.text
        report = json.loads(report)
        # json_string = json.dumps(report)
        
        st.write(response)
