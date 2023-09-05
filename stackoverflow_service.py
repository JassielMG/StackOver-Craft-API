import requests
import json
import pandas as pd


def fetch_data_from_api():
    url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = json.loads(response.text)
        return json_data
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP error: {e.response.status_code}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def create_dataframe(data):
    return pd.DataFrame(data)


def preprocessing_data(json_data):
    df = pd.DataFrame(json_data["items"])  # this part of the data is in the items key
    owner_info = df["owner"]  # this part of the data is in the owner key into the items key ... items->owner
    df_owner = pd.DataFrame([x for x in owner_info])
    df_owner.rename(columns={"link": "user_link"}, inplace=True)
    # once we have the owner info we can merge it with the rest of the data
    df = pd.concat([df_owner, df], axis=1)
    # we dont need the owner column anymore
    df.drop(columns=["owner"], inplace=True)
    return df


def answer_questions(df):
    return df.value_counts("is_answered")


def less_viewed_question(df):
    return df[df["view_count"] == df["view_count"].min()][["title","view_count"]]


def newest_oldest_question(df):
    df["created_date"] = pd.to_datetime(df["creation_date"], unit="s")
    result = df[["title", "created_date"]][(df["created_date"] == max(df["created_date"])) | (df["created_date"] == min(df["created_date"]))]
    return result


def most_reputation_owner_question(df):
    result = df[["title", "reputation"]][df.reputation == df.reputation.max()]
    return result


if __name__ == '__main__':
    data = fetch_data_from_api()
    df = preprocessing_data(data)
    print(answer_questions(df))
    print(less_viewed_question(df))
    print(newest_oldest_question(df))
    print(most_reputation_owner_question(df))