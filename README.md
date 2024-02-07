# ChEMBLchat

## Project Overview

This project is a web-based chat interface that allows users to query the ChEMBL database for chemical compounds using either a ChEMBL ID or a SMILES string. It's designed to be a simple and intuitive tool for researchers, students, and anyone interested in chemical data. 

**Status:** Work in Progress

We are currently developing Natural Language Processing (NLP) capabilities to enhance user interactions and provide a more seamless query experience. This will allow users to input their queries in conversational language.

## Features

- Query chemical compounds by ChEMBL ID or SMILES string
- Display compound information in a user-friendly chat interface
- Visualize chemical structure images by clicking on SMILES strings
- Planned implementation of NLP for improved user queries

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/CrytecFusion101/ChEMBLchat/
2. Navigate to the project directory:
   cd ChEMBLchat
3. Install the necessary dependencies:
   pip install -r requirements.txt
4. Run the Flask application:
   python app.py

## Running the Application

Once the Flask server is running, you can access the chat interface by navigating to `http://localhost:5000` in your web browser. Enter a ChEMBL ID or SMILES string into the chat input and press Enter or click the "Send" button to retrieve compound information.

## Contributions

This project is in the alpha stage, and contributions are welcome. If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
