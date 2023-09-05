from fastapi import FastAPI
from stackoverflow_service import fetch_data_from_api
from stackoverflow_service import preprocessing_data
from stackoverflow_service import answer_questions
from stackoverflow_service import less_viewed_question
from stackoverflow_service import newest_oldest_question
from stackoverflow_service import most_reputation_owner_question
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get("/")
def read_root():
    data = fetch_data_from_api()
    df = preprocessing_data(data)
    return {
        "answer_questions": answer_questions(df).to_dict(),
        "less_viewed_question": less_viewed_question(df).to_dict("list"),
        "newest_oldest_question": newest_oldest_question(df).to_dict("list"),
        "most_reputation_owner_question": most_reputation_owner_question(df).to_dict("list"),
    }
