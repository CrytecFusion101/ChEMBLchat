from flask import Flask, request, jsonify, render_template
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat_interface.html')

@app.route('/query-chembl', methods=['POST'])
def query_chembl():
    data = request.json
    query = data['message']
    response_data = fetch_chembl_data(query)
    return jsonify({'reply': response_data})

def fetch_chembl_data(query):
    base_url = "https://www.ebi.ac.uk/chembl/api/data/molecule"
    molecule_url = f"{base_url}/{query}.xml"  # Request XML response
    try:
        response = requests.get(molecule_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        # Parse XML response
        root = ET.fromstring(response.content)
        molecule_data = parse_molecule_data(root)
        return molecule_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Other error occurred: {err}"

def parse_molecule_data(root):
    # Basic information
    molecule_chembl_id = root.find('.//molecule_chembl_id').text
    pref_name = root.find('.//pref_name').text if root.find('.//pref_name') is not None else "Not available"
    canonical_smiles = root.find('.//canonical_smiles').text if root.find('.//canonical_smiles') is not None else "Not available"
    standard_inchi_key = root.find('.//standard_inchi_key').text if root.find('.//standard_inchi_key') is not None else "Not available"
    first_approval = root.find('.//first_approval').text if root.find('.//first_approval') is not None else "Not available"
    indication_class = root.find('.//indication_class').text if root.find('.//indication_class') is not None else "Not available"
    
    # Molecule properties
    properties = root.find('.//molecule_properties')
    alogp = properties.find('.//alogp').text if properties.find('.//alogp') is not None else "Not available"
    hba = properties.find('.//hba').text if properties.find('.//hba') is not None else "Not available"
    hbd = properties.find('.//hbd').text if properties.find('.//hbd') is not None else "Not available"
    full_mwt = properties.find('.//full_mwt').text if properties.find('.//full_mwt') is not None else "Not available"

    # Format extracted data into a string for display
    molecule_info = (f"ChEMBL ID: {molecule_chembl_id}\n"
                     f"Name: {pref_name}\n"
                     f"SMILES: {canonical_smiles}\n"
                     f"InChI Key: {standard_inchi_key}\n"
                     f"First Approval: {first_approval}\n"
                     f"Indication Class: {indication_class}\n"
                     f"ALogP: {alogp}\n"
                     f"HBA: {hba}\n"
                     f"HBD: {hbd}\n"
                     f"Full Molecular Weight: {full_mwt}")
    return molecule_info


if __name__ == '__main__':
    app.run(debug=True)
