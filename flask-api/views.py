from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/make_post', methods=['POST'])
def make_post():
    return 'Done', 201


@api.route('/get_req', methods=['GET'])
def get_req():

    posts = [
        {
            "Title":"Blow Me",
            "Location":"UMass Amherst",
            "Description":"Data Structures project 7. Implement Linked List from scratch in Java."
        },
        {
            "Title":"Macroeconomics Exam Study Group",
            "Location":"Boston University",
            "Description":"Introduction to Macroeconomics Midterm. We will study 2-3 nights this week before the exam."
        },
        {
            "Title":"College Writing Peer Review",
            "Location":"UMass Amherst",
            "Description":"College Writing second essay on persuasive. Looking for a partner/s to peer review and edit our rough drafts."
        }
    ]

    return jsonify(posts)
