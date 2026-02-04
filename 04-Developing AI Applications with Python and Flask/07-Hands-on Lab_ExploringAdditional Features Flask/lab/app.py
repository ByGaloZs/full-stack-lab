# Import libraries
from flask import Flask, redirect, render_template, request, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {"id": 1, "date": "2023-06-01", "amount": 100},
    {"id": 2, "date": "2023-06-02", "amount": -200},
    {"id": 3, "date": "2023-06-03", "amount": 300},
]


# Read operation: List all transactions
# Route to handle the Read of a new transaction
@app.route("/", methods=["GET"])
def get_transactions():
    """Render the transactions list page.

    Args:
        None

    Returns:
        flask.Response: Rendered HTML page containing all transactions.
    """
    # Render the transactions list template with current data.
    return render_template("transactions.html", transactions=transactions)


# Create operation: Display add transaction form
# Route to handle the creation of a new transaction
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    """Handle creation of a new transaction or render the add form.

    Args:
        None

    Returns:
        flask.Response: Redirects to the transactions list after creation, or
            renders the add transaction form for GET requests.
    """
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Create a new transaction object using form field values
        transaction = {
            "id": len(transactions) + 1,
            "date": request.form["date"],
            "amount": float(request.form["amount"]),
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))

    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")


# Update operation: Display edit transaction form
# Route to handle the editing of an existing transaction
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    """Edit an existing transaction or render the edit form.

    Args:
        transaction_id (int): Identifier of the transaction to edit.

    Returns:
        flask.Response: Redirects to the transactions list after a successful
            update, renders the edit form for GET requests, or returns a 404
            response if the transaction is not found.
    """
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Extract the updated values from the form fields
        date = request.form["date"]  # Get the 'date' field value from the form
        amount = float(request.form["amount"])  # Get the 'amount' field value from the form and convert it to a float

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = date  # Update the 'date' field of the transaction
                transaction["amount"] = amount  # Update the 'amount' field of the transaction
                break  # Exit the loop once the transaction is found and updated

        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))

    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404


# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    """Delete a transaction by ID and redirect to the list.

    Args:
        transaction_id (int): Identifier of the transaction to delete.

    Returns:
        flask.Response: Redirects to the transactions list after deletion.
    """
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))


# Search operation: Search transactions by amount range
# Route to handle searching transactions within a specified amount range
@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    """Search transactions by amount range or render the search form.

    Args:
        None

    Returns:
        flask.Response: Renders the filtered transactions list for a POST
            request or the search form for a GET request.
    """
    # Handle form submission to filter transactions by amount range.
    if request.method == "POST":
        min_amount = float(request.form["min_amount"])
        max_amount = float(request.form["max_amount"])
        filtered_transactions = []
        for transaction in transactions:
            if min_amount <= transaction["amount"] <= max_amount:
                filtered_transactions.append(transaction)
                return render_template("transactions.html", transactions=filtered_transactions)
    # Render the search form for GET requests.
    return render_template("search.html")


# Additional Feature: Calculate total balance
# Route to calculate and display the total balance of all transactions
@app.route("/balance")
def total_balance():
    """Calculate the total balance and render the transactions list.

    Args:
        None

    Returns:
        flask.Response: Rendered HTML page including all transactions and the
            computed total balance.
    """
    # Compute the total balance across all transactions.
    total = sum(transaction["amount"] for transaction in transactions)
    # Render the list with the computed total balance.
    return render_template("transactions.html", transactions=transactions, total_balance=total)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
