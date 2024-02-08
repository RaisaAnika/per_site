from google.oauth2 import service_account
from googleapiclient.discovery import build


def fetch_content_from_google_doc(service_account_file, document_id):
    """
    Fetches content from a Google Doc using Google Docs API.

    Args:
        service_account_file (str): Path to the service account key file.
        document_id (str): ID of the Google Doc to access.

    Returns:
        dict: Content of the Google Doc.
    """
    try:
        # Initialize credentials
        credentials = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=['https://www.googleapis.com/auth/documents.readonly']
        )

        # Build the Google Docs API service
        service = build('docs', 'v1', credentials=credentials)

        # Call the API to get the content of the Google Doc
        document = service.documents().get(documentId=document_id).execute()

        # Extract and return the content of the document
        content = document.get('body').get('content')
        return content
    except Exception as e:
        print(f"Error fetching content from Google Doc: {e}")
        return None
