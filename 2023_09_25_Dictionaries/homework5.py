my_list = ["apple", "banana", "orange", "kiwi"]
print("List: ", my_list)
print("First element: ", my_list[0])
print("Last element: ", my_list[-1])
print("Sublist: ", my_list[2:5])
my_list[2] = "grape"
print("Modified list: ", my_list)

my_dict = {"apple": "яблоко", "banana": "банан", "orange": "апельсин"}
print("Dictionary", my_dict)
print("Translation: ", my_dict.get("orange"))
my_dict.update({"kiwi": "киви"})
print("Modified: ", my_dict)
