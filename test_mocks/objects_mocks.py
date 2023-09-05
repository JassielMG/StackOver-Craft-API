from pandas import Timestamp

get_response_mock = """{
  "items": [
    {
      "tags": [
        "perl",
        "hash"
      ],
      "owner": {
        "reputation": 541,
        "user_id": 7978784,
        "user_type": "registered",
        "accept_rate": 67,
        "profile_image": "https://www.gravatar.com/avatar/0f221919d235c6f34f9343e1b2201c7f?s=256&d=identicon&r=PG&f=y&so-version=2",
        "display_name": "Biswajit Maharana",
        "link": "https://stackoverflow.com/users/7978784/biswajit-maharana"
      },
      "is_answered": false,
      "view_count": 32,
      "answer_count": 1,
      "score": 1,
      "last_activity_date": 1693881704,
      "creation_date": 1693847464,
      "question_id": 77039567,
      "content_license": "CC BY-SA 4.0",
      "link": "https://stackoverflow.com/questions/77039567/how-to-delete-hash-elements-inside-a-function-using-scalar-variable-in-perl",
      "title": "How to delete hash elements inside a function using scalar variable in perl"
    }],
    "has_more": true,
    "quota_max": 300,
    "quota_remaining": 295
    }
    """

preprocessing_data_mock = {
        "reputation": [541],
        "user_id": [7978784],
        "user_type": ["registered"],
        "accept_rate": [67],
        "profile_image": ["https://www.gravatar.com/avatar/0f221919d235c6f34f9343e1b2201c7f?s=256&d=identicon&r=PG&f=y&so-version=2"],
        "display_name": ["Biswajit Maharana"],
        "user_link": ["https://stackoverflow.com/users/7978784/biswajit-maharana"],
        "tags": [["perl", "hash"]],
        "is_answered": [False],
        "view_count": [32],
        "answer_count": [1],
        "score": [1],
        "last_activity_date": [1693881704],
        "creation_date": [1693847464],
        "question_id": [77039567],
        "content_license": ["CC BY-SA 4.0"],
        "link": ["https://stackoverflow.com/questions/77039567/how-to-delete-hash-elements-inside-a-function-using-scalar-variable-in-perl"],
        "title": ["How to delete hash elements inside a function using scalar variable in perl"],
    }

answer_questions_mock = {1: 1.0}

less_viewed_question_mock = {'title': {0: 'How to delete hash elements inside a function using scalar variable in perl'}, 'view_count': {0: 32}}

newest_oldest_question_mock = {'created_date': {0: Timestamp('2023-09-04 17:11:04')}, 'title': {0: 'How to delete hash elements inside a function using scalar variable in perl'}}

most_reputation_owner_question_mock = {'reputation': {0: 541}, 'title': {0: 'How to delete hash elements inside a function using scalar variable in perl'}}