from langchain_community.document_loaders import WebBaseLoader
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(model="command-r-plus-08-2024")

prompt = PromptTemplate(
    template = 'Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://www.amazon.com/Project-Hail-Mary-Andy-Weir/dp/0593135229/?_encoding=UTF8&pd_rd_w=LSymz&content-id=amzn1.sym.9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_p=9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_r=SWGM1NKCP1Q8QD3S1ETF&pd_rd_wg=X7htT&pd_rd_r=c2e8e10b-3d79-41db-b4af-64f6287fff16&ref_=pd_hp_d_btf_crs_zg_bs_283155"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'What is the name of Porduct ?', 'text': docs[0].page_content})

print(result)

