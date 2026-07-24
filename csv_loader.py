from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='ACLBSL_subset.csv')

docs = loader.load()

print(docs[1])
print(len(docs))