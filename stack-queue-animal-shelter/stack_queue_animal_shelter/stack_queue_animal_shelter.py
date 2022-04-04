# from .stacks_and_queues import Queue


class Dog:
    """Creates an instance of a Dog with animal sound when you call his name + has next properties"""

    def __init__(self):
        self.name = "WOOOFFF"
        self.next = None


class Cat:
    def __init__(self):
        """Creates an instance of a Cat with animal sound when you call his name + has next properties"""
        self.name = "Meaowwww"
        self.next = None


class AnimalShelter:
    """
    Class constructor for a queue of 'animals'
    Takes no parameters. Creates an instance of an AnimalShelter with front and end properties.
    Has two methods, enqueue and dequeue.
    Enqueue('cat'/'dog') - Adds a dog or cat to the 'end' of the queue
    Dequeue(['cat'/'dog']) - Removes the cat or dog closest to the front of the queue. Takes an optional parameter, cat or dog, that will return the first in the queue.
    """

    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, animal=None):
        """enqueue('cat'/'dog') - Adds a dog or cat to the 'end' of the queue"""
        if animal.lower() == "dog":
            new_dog = Dog()
            if self.end:
                self.end.next = new_dog
                self.end = new_dog
            elif self.front:
                self.front.next = new_dog
                self.end = new_dog
            else:
                self.front = new_dog

        elif animal.lower() == "cat":
            new_cat = Cat()
            if self.end:
                self.end.next = new_cat
                self.end = new_cat
            elif self.front:
                self.front.next = new_cat
                self.end = new_cat
            else:
                self.front = new_cat

        else:
            return print("Dogs and Cats only please.")

    def dequeue(self, pref=""):
        """dequeue(['cat'/'dog']) - Removes the cat or dog closest to the front of the queue. Takes an optional parameter, cat or dog, that will return the first in the queue.

        new function idea:
        Checks if  Object is one of the types described in the type parameter
        https://www.w3schools.com/python/ref_func_isinstance.asp
        """

        new_queue, front, looking, first = AnimalShelter(), self.front, True, None
        # new_queue.__str__()
        if self.front:
            self.front = front.next
        while front:
            if pref.lower() == "cat" and looking:
                if isinstance(front, Cat):
                    first = front
                    looking = False
                else:
                    # return print("No cats in the shelter")
                    new_queue.enqueue("dog")
                    # print("i was in cat pref")
                    # new_queue.__str__()
                    front = self.front
                    print("im new front in cats", str(front))
                    # looking = False

            elif pref.lower() == "dog" and looking:
                if isinstance(front, Dog):
                    first = front
                    looking = False
                else:
                    # return print("No dogs in the shelter")
                    new_queue.enqueue("cat")
                    # print("i was in dog pref")
                    # new_queue.__str__()
                    front = self.front
                    print("im new front in dogs", str(front))
                    # looking = False
                    # return print("im in ininfinte loop")

            else:
                # print("i was in else pref")
                # new_queue.__str__()
                return front.name  ## streatch goal
        # new_queue.__str__()
        return first.name

    def __str__(self):
        """
        A method to print the animal shelter queue
        Input: nothing
        Output: string
        """
        output = ""
        if self.front is None:
            return print("The shelter queue is empty")
        else:
            current = self.front
            while current is not None:
                output += "{ " f"{current.name}" " } -> "
                current = current.next
            output += "Null"
        return print(output)


if __name__ == "__main__":
    new_shelter = AnimalShelter()
    # new_shelter.enqueue("dog")
    new_shelter.enqueue("dog")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("dog")
    # print(new_shelter.__str__())
    # print(new_shelter.dequeue("dog"))
    print("l128", new_shelter.__str__())
    # print(new_shelter.dequeue("dog"))
    # print(new_shelter.dequeue("cata"))
    # print(new_shelter.dequeue("cat"))
    # print(new_shelter.dequeue("cat"))
    # print(new_shelter.dequeue("dog"))
    # print(new_shelter.dequeue("dog"))
    print(new_shelter.dequeue("dog"))
    # print(new_shelter.dequeue("cat"))
    print(new_shelter.dequeue("cat"))
    print(new_shelter.dequeue("cat"))
    # print(new_shelter.dequeue("dog"))
    print(new_shelter.dequeue("cat"))
    print(new_shelter.dequeue("dog"))
    # print(new_shelter.dequeue("cat"))
    # print(new_shelter.dequeue("dog").name)
    print("l41", new_shelter.__str__())
