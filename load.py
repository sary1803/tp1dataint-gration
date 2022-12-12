from pathlib import Path	        
        
from azure.storage.blob import BlobServiceClient	        
        
import os	        
        
def list_of_files(directory):
    names=[i for i in os.listdir(directory)]
    paths=list(map(lambda x:os.path.join(directory,x),names))
    return names,paths

def upload(directory,conn_str,container_name):
    #liste des fichiers
    names,paths=list_of_files(directory)
    
    #connexion
    service_client=BlobServiceClient.from_connection_string(conn_str)	        
    container_client = service_client.get_container_client(container_name)

    #upload
    for n,p in zip(names,paths):
        file_path_on_azure = n        
        file_path_on_local = p       
        blob_client = container_client.get_blob_client(file_path_on_azure)	        

        with open(file_path_on_local,'rb') as data:	        

            blob_client.upload_blob(data)	 



        
        

        
        
if __name__ == '__main__':	        
        
    upload("directory","conn_str"",container_name")	        
        
