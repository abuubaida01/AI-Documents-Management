from documents.models import Document
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

@tool
def list_documents(config: RunnableConfig)->list:
  """
    list a user's recents 5 documents for the current user
  """

  metadata = config.get("metadata")
  configurable = config.get('configurable')
  limit = 5
  user_id = configurable.get("user_id") or metadata.get("user_id")
  response_list = []

  qs = Document.objects.filter(owner_id = user_id, active=True).order_by('-created_at')

  for obj in qs[:limit]: 
    response_list.append(
      {
        "id":  obj.id, 
        "title": obj.title
      }
    )

  return response_list


@tool
def get_documents(document_id: int, config:RunnableConfig): 
  """
    get the document detail of the user with doc id
  """
  metadata = config.get("metadata")
  configurable = config.get('configurable')

  user_id = configurable.get("user_id") or metadata.get("user_id") 


  obj = Document.objects.filter(owner_id = user_id, id=document_id, active=True).first()
  if not obj: 
    return {}
  
  response_data = {
    'id': obj.id,
    'title': obj.title
  }
  return response_data


documents_tools = [
  list_documents,
  get_documents
]