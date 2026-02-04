from flask import Flask, render_template, request, jsonify
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

def parse_number(value, name):
    """
    Parses a query parameter into a float.

    Args:
        value (str): The query parameter value.
        name (str): The parameter name (used for error messages).

    Returns:
        float: The parsed numeric value.

    Raises:
        ValueError: If the parameter is missing or not a valid number.
    """
    if value is None or value == "":
        raise ValueError(f"Missing parameter: {name}")
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid number for '{name}': {value}")

def format_result(result):
    """
    Formats a numeric result for output.

    If the number is a whole float, it is converted to an integer string.

    Args:
        result (int or float): The calculation result.

    Returns:
        str: The formatted result as a string.
    """
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)

@app.route("/sum")
def sum_route():
    """
    Handles addition requests.

    Reads `num1` and `num2` from query parameters, performs summation,
    and returns the formatted result.

    Returns:
        str: The sum result if successful.
        Response: JSON error message with HTTP 400 if input is invalid.
    """
    try:
        num1 = parse_number(request.args.get("num1"), "num1")
        num2 = parse_number(request.args.get("num2"), "num2")
        result = summation(num1, num2)
        return format_result(result)
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route("/sub")
def sub_route():
    """
    Handles subtraction requests.

    Reads `num1` and `num2` from query parameters, performs subtraction,
    and returns the formatted result.

    Returns:
        str: The subtraction result if successful.
        Response: JSON error message with HTTP 400 if input is invalid.
    """
    try:
        num1 = parse_number(request.args.get("num1"), "num1")
        num2 = parse_number(request.args.get("num2"), "num2")
        result = subtraction(num1, num2)
        return format_result(result)
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route("/mul")
def mul_route():
    """
    Handles multiplication requests.

    Reads `num1` and `num2` from query parameters, performs multiplication,
    and returns the formatted result.

    Returns:
        str: The multiplication result if successful.
        Response: JSON error message with HTTP 400 if input is invalid.
    """
    try:
        num1 = parse_number(request.args.get("num1"), "num1")
        num2 = parse_number(request.args.get("num2"), "num2")
        result = multiplication(num1, num2)
        return format_result(result)
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route("/")
def render_index_page():
    """
    Renders the main index page.

    Returns:
        Response: The rendered HTML template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
