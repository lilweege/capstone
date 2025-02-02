from flask import Flask, request, jsonify
from controller.compute import compute_similarities_from_zip

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    """
    Expects a POST request with a ZIP file containing Python files.
    The ZIP file can be sent either as a multipart/form-data file (with key "file")
    or as raw binary data.
    
    Optionally, a query parameter "model" can override the default model.
    """
    # Retrieve optional model override from query parameters
    model_name = request.args.get("model", "microsoft/codebert-base")

    # Check if the client sent the file as multipart/form-data
    if "file" in request.files:
        zip_bytes = request.files["file"].read()
    else:
        # Otherwise, assume the ZIP is sent as raw binary data
        zip_bytes = request.get_data()

    if not zip_bytes:
        return jsonify({"error": "No zip file data provided"}), 400

    try:
        # Process the ZIP bytes and compute similarity results
        results = compute_similarities_from_zip(zip_bytes, model_name)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode for easier local testing.
    app.run(debug=True)
