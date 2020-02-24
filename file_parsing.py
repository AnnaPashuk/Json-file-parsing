from twitter2 import twitter_accounts


def find_given_key(element, given_key):
    """
    (dict or list, string) -> list
    this function is for parsing a Json file
    it finds all values of given key in Json file
    """
    res = []
    if type(element) == dict:
        for key in element:
            if key == given_key:
                res += [element[key]]
            elif type(element[key]) == dict or type(element[key]) == list:
                res += find_given_key(element[key], given_key)
    elif type(element) == list:
        for key in element:
            if key:
                res += find_given_key(key, given_key)
    return res


if __name__ == "__main__":
    name = input("Please enter user name:", )
    key_name = input("Please enter a key:", )
    print(find_given_key(twitter_accounts(name), key_name))
