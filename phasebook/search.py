from flask import Blueprint, request,jsonify    

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    priority_order = ["id", "name", "age", "occupation"]
    
    # Sorting keys based on priority_order
    keys = list(args.keys())
    sorted_keys = [key for key in priority_order if key in keys]
    final_keys = sorted_keys + [key for key in keys if key not in sorted_keys]

    if final_keys:
        result = []
        for key in final_keys:
            for user in USERS:
                if key == "age":
                    # Check if age is within range age - 1 to age + 1
                    user_age = user["age"]
                    search_age = int(args["age"])
                    if user_age >= search_age - 1 and user_age <= search_age + 1:
                        if user not in result:
                            result.append(user)
                elif str(args[key]).lower() in str(user[key]).lower() and user not in result:
                    result.append(user)

        return result