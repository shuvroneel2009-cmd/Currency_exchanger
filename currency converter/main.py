import requests
import functions
import just_clearing_main


user_history_path = "user_history.json"
offline_req = "n"

user_history = functions.file_manager(user_history_path,"r")

try:
    api_request = requests.get("https://v6.exchangerate-api.com/v6/0b2b8d19bd255c8cf3b136eb/latest/USD",)
    status_code = api_request.status_code
except:
    status_code = 1000
    pass

if status_code == 200:
        data = api_request.json()
        currencies = list(data["conversion_rates"].keys())

else:

    just_clearing_main.stasco_feedback(status_code)


    if not user_history == {}:

        offline_req = functions.btext_inputer_v("Do you wanna use offline value? (example: y/n)",["y",'n'])
        currencies = user_history["currencies"]
        data = user_history["data"]

if offline_req == "y" or status_code == 200:

    while True:

        from_cur = functions.btext_inputer_v("Please enter the base currency: (Example: EUR)", currencies,str.upper)
        amount = functions.btext_inputer_t("Please enter the desired amount: (Example: 30)", float)
        to_cur = functions.btext_inputer_v("Please enter the target currency: (Example: BDT)", currencies,str.upper)

        this_info = {
            "base_cur": from_cur,
            "amount": amount,
            "to_cur": to_cur,
            "result": functions.converter(data, from_cur, to_cur, amount)
        }
        print(this_info)


        if user_history == {}:

            user_history["history"] = [this_info]
        else:
            user_history["history"].append(this_info)

        user_history["currencies"] = currencies
        user_history["data"] = data

        functions.file_manager(user_history_path, 'w', user_history)

        user_again_req = functions.btext_inputer_v("Do you wanna convert again? (example: y/n)", ["y", 'n'])
        if user_again_req == "y":
            pass
        else:
            print("Thank you for using this program")
            break

else:
    print("Thank you for using this program")

