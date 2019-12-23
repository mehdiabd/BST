import logging
import concurrent.futures
from Tree import Tree
from collections import Counter

st = ' the the the quick brown fox jumped over lazy dog over and over again and again bst.py source code is developed '\
     'and tested by mahdi over 3000 times abd abd abd abd abd my name my name my name is mahdi abd my name is ' \
     'mahdi abd lorem issue lorem issue lorem issue lorem issue lorem issue lorem issue '
sp = st.split()
count = Counter(sp)

# i = input('enter your string: ')
i = "11 11 11 11 11 11 11 11 11 11 11 9 9 9 9 9 9 9 9 9 8 8 8 8 8 8 8 8 e e e e e e e e 10 10 10 10 10 10 10 10 10 10 "\
    "13 13 13 13 13 13 13 13 13 13 13 13 13 12 12 12 12 12 12 12 12 12 12 12 12 14 14 14 14 14 14 14 14 14 14 14 14 " \
    "14 14 quick times n brown fox jumped lazy m"
isp = i.split()
iCount = Counter(isp)


def main():

    condition = False
    bst = None
    for key, val in count.items():
        if not condition:
            bst = Tree(key, val)
            condition = True
        else:
            bst.insert(key, val)

    cnd = False
    new = None
    for key, val in iCount.items():
        if not cnd:
            new = Tree(key, val)
            cnd = True
        else:
            new.insert(key, val)

    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Traverse inOrder!")
        print("2. Traverse preOrder!")
        print("3. Insert a word to tree!")
        print("4. Merge the New tree with the BST!")
        print("5. Display max node for each node!")
        print("6. Display each node's linked list!")
        print("7. Remove nodes from tree!")
        print("8. Asynchronous Insertion!")
        print("9. Asynchronous Removal!")
        print("10. Exit!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        option = input('Please choose one option: ')

        if option == '1':
            print("BST inOrder: ")
            bst.in_order()
            print("New Tree inOrder: ")
            new.in_order()

        elif option == '2':
            print("BST preOrder: ", bst.pre_order())
            print("New Tree preOrder: ", new.pre_order())

        elif option == '3':
            tre = input("Enter a valid tree name: ")
            key = input("Enter your word to insert: ")
            val = input("Enter the word's count: ")
            if tre == "bst":
                bst.insert(key, int(val))
                print(bst.pre_order())
                print("#", tre, val, "'s Linked List Is: ")
                bst.show_list(int(val))
            elif tre == "new":
                new.insert(key, int(val))
                print(new.pre_order())
                print("#", tre, val, "'s Linked List Is: ")
                new.show_list(int(val))
            else:
                print("This tree doesn't exist!")

        elif option == '4':
            bst.merge(new)
            print("BST: ", bst.pre_order())
            new.merge(bst)
            print("New: ", new.pre_order())

        elif option == '5':
            print("BST: ")
            bst.nodes_max()
            print("NEW: ")
            new.nodes_max()

        elif option == '6':
            tr = input("Enter the tree name: ")
            nod = input("Enter the node number: ")
            if tr == "bst":
                bst.show_list(int(nod))
            elif tr == "new":
                new.show_list(int(nod))
            else:
                print("This tree doesn't exist!")

        elif option == '7':
            print('Removing 1: ')
            bst.remove(1)
            print('Removing 2: ')
            bst.remove(2)
            print('Removing 3: ')
            bst.remove(3)
            print('Removing 4: ')
            bst.remove(4)
            print('Removing 7: ')
            bst.remove(7)
            print('Removing 8: ')
            bst.remove(8)

        elif option == '8':
            tre = input("Enter A Valid Tree Name: ")
            if tre != "bst" and tre != "new":
                print("This Tree Name Doesn't Exist :(")
                want = input("Do You Want To Retry? (Y/N)")
                if want == "Y":
                    print(" PLEASE ENTER A VALID OPTION ! ")
                    main()
                else:
                    print("See You Soon (^_^)")
                break
            nmb = int(input("Please Enter Number Of Words To Async Insert: "))
            inserts = []
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            while nmb > 0:
                key = input("Enter Your Words List To Insert: ")
                inserts.append(key)
                nmb -= 1
            num = int(input("Please Enter The Count Of Repeating: "))
            maxi = int(input("Please Enter Maximum Number Of Concurrent Threads: "))
            if tre == "bst":
                database = bst
                logging.getLogger().setLevel(logging.DEBUG)
                logging.info("Async Insert Info: Number Of Triggered Threads is %d.", database.value)
                with concurrent.futures.ThreadPoolExecutor(max_workers=maxi) as executor:
                    for each in inserts:
                        executor.submit(database.async_insert, each, num)
                logging.info("Async Insert Info: Number Of Triggered Threads is %d.", database.value)
                print(bst.pre_order())
                print("#", tre, num, "'s Linked List Is: ")
                bst.show_list(num)
            elif tre == "new":
                database = new
                logging.getLogger().setLevel(logging.DEBUG)
                logging.info("Async Insert Info: Number Of Triggered Threads is %d.", database.value)
                with concurrent.futures.ThreadPoolExecutor(max_workers=maxi) as executor:
                    for each in inserts:
                        executor.submit(database.async_insert, each, num)
                logging.info("Async Insert Info: Number Of Triggered Threads is %d.", database.value)
                print(new.pre_order())
                print("#", tre, num, "'s Linked List Is: ")
                new.show_list(num)

        elif option == '9':
            tre = input("Enter A Valid Tree Name: ")
            if tre != "bst" and tre != "new":
                print("This Tree Name Doesn't Exist :(")
                want = input("Do You Want To Retry? (Y/N)")
                if want == "Y":
                    print(" PLEASE ENTER A VALID OPTION ! ")
                    main()
                else:
                    print("See You Soon (^_^)")
                break
            nmb = int(input("Please Enter Number Of Nodes To Async Remove: "))
            removes = []
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            while nmb > 0:
                key = input("Enter Your Nodes To Remove: ")
                removes.append(key)
                nmb -= 1
            maxi = int(input("Please Enter Maximum Number Of Concurrent Threads: "))
            if tre == "bst":
                database = bst
                logging.getLogger().setLevel(logging.DEBUG)
                logging.info("Async Remove Info: Number Of Triggered Threads is %d.", database.value)
                with concurrent.futures.ThreadPoolExecutor(max_workers=maxi) as executor:
                    for each in removes:
                        executor.submit(database.async_remove, each)
                logging.info("Async Remove Info: Number Of Triggered Threads is %d.", database.value)
                print(bst.pre_order())
            elif tre == "new":
                database = new
                logging.getLogger().setLevel(logging.DEBUG)
                logging.info("Async Remove Info: Number Of Triggered Threads is %d.", database.value)
                with concurrent.futures.ThreadPoolExecutor(max_workers=maxi) as executor:
                    for each in removes:
                        executor.submit(database.async_remove, each)
                logging.info("Async Remove Info: Number Of Triggered Threads is %d.", database.value)
                print(new.pre_order())

        elif option == '10':
            print("See You Soon (^_^)")
            break

        else:
            print(" PLEASE ENTER A VALID OPTION ! ")


main()
