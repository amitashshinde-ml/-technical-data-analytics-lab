import requests

def  main():
    try:
        while True:
            request_data = requests.get("https://api.kanye.rest")
            request_data.raise_for_status()
            with open("Kanye_quote.txt","a") as fl:
                print(f"Kanye Quote : {request_data.json()['quote']}")
                fl.write(f"{request_data.json()['quote']} \n")

            user_choice= input("Do you want to check next quote? Y/N :")
            if user_choice.lower()=="n":
                break
    except requests.exceptions.RequestException as errex:
        print("Exception request")

if __name__=="__main__":
    main()