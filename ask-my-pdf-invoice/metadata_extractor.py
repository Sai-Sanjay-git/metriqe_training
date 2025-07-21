from meadataschema import InvoiceMetaData
from llm_utils import llm

def extract_metadata_from_document(doc_content:str,llm_model)->dict:
    """use metadata to extract data form the documents"""

    parser_llm = llm_model.with_structure_output(InvoiceMetaData)

    prompt = f"""
    extract the following invoice details from the document content provided
    ensure the 'invoice_date'is in format 'DD-MM-YYYY', 'invoice_number' and 'customer_name' are in string and 'total_value' is in float
    
    Document content : {doc_content}

    Extracted invoice details:

    """

    extracted_data = parser_llm.invoke(prompt)
    return extracted_data.dict()

print(extract_metadata_from_document("""""",llm))