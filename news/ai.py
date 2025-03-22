from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import generative_models
from .Config.config import Gemini_key
from langchain.prompts.prompt import PromptTemplate
from langchain_community.embeddings import HuggingFaceBgeEmbeddings #import the correct model.


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
        
        
    # promt template
    def Promt(self):
        self.promt_template=PromptTemplate(template="Read this para carefully {retrivered_doc} and Question: {query} , responed with true or false ")
        
    # using llm
    def model(self):
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",verbose=True,temperature=0.1,api_key=Gemini_key)
        promt= self.promt_template.format(
            retrivered_doc=self.retrivered_doc_content,
            query=self.query
        )
        respones=llm.invoke(input=promt)
        print (respones.content)

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
