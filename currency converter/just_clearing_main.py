#just_cleaning_main.py


def stasco_feedback(status_code):
    if status_code == 400:
        print("The server cannot process the request due to a client-side error, like mangled data payload syntax.")

    elif status_code == 401:
        print("401 Unauthorized: Access is blocked because the client lacks valid authentication credentials.")

    elif status_code == 403:
        print("403 Forbidden")
    elif status_code == 404:
        print("404 Not Found")
    elif status_code == 429:
        print("429 Too Many Requests")
    elif status_code == 1000:
        print("You are not connected to the internet")
    else:
        print("Something went wrong in the online system")