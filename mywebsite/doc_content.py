
from .google_api import fetch_content_from_google_doc

# Define the service account file path and document ID
service_account_file = '/Users/raisaanika/Documents/Portfolio/mywebsite/jsons/portfolio-413604-764fc57b7ff0.json'
document_id = '1y1hgg-0750X-1ygsIUwOjD9Zx5E81F_Y8nQqHvcMxgE'

# Fetch content from Google Doc
content = fetch_content_from_google_doc(service_account_file, document_id)
