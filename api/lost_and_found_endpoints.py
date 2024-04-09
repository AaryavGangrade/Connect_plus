from flask import Flask, jsonify, request
from firebase.lost_and_found import add_found_item, delete_all_found_items_from_database, delete_item,add_lost_item, mark_item_as_returned2, retrieve_all_found_items,retrieve_all_lost_items, retrieve_found_item


app = Flask(__name__)

# Add a found item
@app.route('/add_found_item', methods=['POST'])
def add_found():
    req_data = request.get_json()
    name = req_data['name']
    image_url = req_data['image_url']
    place = req_data['place']
    contact = req_data['contact']
    user_id = req_data['user_id']
    date_found = req_data['date_found']
    
    found_id = add_found_item(name, image_url, place, contact, user_id, date_found)
    return jsonify({'message': 'Found item added successfully', 'found_id': found_id})

# Retrieve all found items
@app.route('/retrieve_all_found_items', methods=['GET'])
def retrieve_items():
    found_items_list = retrieve_all_found_items()
    return jsonify(found_items_list)

# Retrieve found items for a specific user
@app.route('/retrieve_found_items_user', methods=['POST'])
def retrieve_found_user():
    user_id = request.get_json()['user_id']
    found_items_list = retrieve_found_item(user_id)
    return jsonify(found_items_list)

# Delete a specific found item
@app.route('/delete_found_item', methods=['POST'])
def delete_found():
    req_data = request.get_json()
    found_id = req_data['found_id']
    delete_item(found_id)
    return jsonify({'message': 'Item deleted successfully'})


# Add a lost item
@app.route('/add_lost_item', methods=['POST'])
def add_lost():
    req_data = request.get_json()
    name = req_data['name']
    image_url = req_data['image_url']
    place = req_data['place']
    contact = req_data['contact']
    user_id = req_data['user_id']
    
    lost_id = add_lost_item(name, image_url, place, contact, user_id)
    return jsonify({'message': 'Lost item added successfully', 'lost_id': lost_id})

# Retrieve all lost items
@app.route('/retrieve_all_lost_items', methods=['GET'])
def retrieve_all_lost():
    lost_items_list = retrieve_all_lost_items()
    return jsonify(lost_items_list)

# Retrieve lost items for a specific user
@app.route('/retrieve_lost_items_user', methods=['POST'])
def retrieve_lost_user():
    user_id = request.get_json()['user_id']
    lost_items_list = retrieve_all_lost_items(user_id)
    return jsonify(lost_items_list)

# Mark an item as returned
@app.route('/mark_returned', methods=['POST'])
def mark_item_as_returned():
    item_id = request.json.get('item_id')
    success = mark_item_as_returned2(item_id)
    return jsonify({'success': success})

# Delete all found items from the database
@app.route('/delete_all_found_items', methods=['GET'])
def delete_all_found_items_route():
    success = delete_all_found_items_from_database()
    return jsonify({'success': success})

