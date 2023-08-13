class Master:

    def findOnObj(arr, search_key, search_value, multiple):
        new_dictionary = []

        for obj in arr:
            sk = [obj.get(key) for key in search_key]

            if sk == search_value:

                if not multiple:
                    return obj

                new_dictionary.append(obj)

        return new_dictionary
