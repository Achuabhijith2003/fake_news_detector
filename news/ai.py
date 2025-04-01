from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import generative_models
from .Config.config import Gemini_key
from langchain.prompts.prompt import PromptTemplate
from langchain_community.embeddings import HuggingFaceBgeEmbeddings #import the correct model.
import datetime


class AI:
    def __init__(self, path_db, query):
        self.db_dir = path_db
        self.query = query
        
    def load_db(self):
        self.db =FAISS.load_local(self.db_dir,HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),allow_dangerous_deserialization=True)
        
        print("vector_db_loaded_successfully")
        
        
    def Search_document(self):
        retrive=self.db.as_retriever(search_type="similarity",search_kwarg={"k":6})
        retrivered_doc=retrive.invoke(self.query)
        # print(f"Result from DB{retrivered_doc[0].page_content}")
        self.retrivered_doc_content=" ".join([doc.page_content for doc in retrivered_doc ])
        
        
    def Promt(self):
        
        self.promt_template = PromptTemplate(
            template="""
            You are an a AI Agent to detect the fake news in our college KMCT IETM. Remember in any chage in data ,time meaning of the paragraph 
            you must replay accordingly, the give paragraph is the correct news, Question may have mistakes in data, time, meanning , don't take outside data of analyis 
            the given paragraph
            Read this paragraph carefully: {retrivered_doc}
            
            today date : {date_time}

            Question: {query}

            Respond with a JSON object in the following format:
            {{'news_text': {query} ,'is_real': True/False, 'explanation': 'your explanation here','confidence': 'in int type ,'factors': 'in list of str''}}
            """
        )
    # using llm
    def model(self):
        date_time=datetime.datetime.now()
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",verbose=True,temperature=0.1,api_key=Gemini_key)
        promt= self.promt_template.format(
            retrivered_doc=self.retrivered_doc_content,
            query=self.query,
            date_time=date_time
        )
        respones=llm.invoke(input=promt)
        print (respones.content)
        return respones.content

# path_data = "D:/KMCT/miniproject/fakdec/Datasets"
path_db = "news/models"
# query = "is Central Economic Problems in 5 th module "

obj = AI( path_db, query=None)
# obj.load_documents()
# obj.Text_Splitter()
# obj.get_embeddings()
# obj.embedding_to_DB()
# obj.load_db()
# obj.Search_document()


    

# while True:
#     promt=input("enter the query: ")
#     obj.query=promt
#     obj.Search_document()
#     obj.Promt()
#     obj.model()
