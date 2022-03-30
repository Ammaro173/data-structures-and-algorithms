from stack_queue_animal_shelter.stack_queue_animal_shelter import (
    Dog,
    Cat,
    AnimalShelter,
)


def test_creating_empty_animal_shelter():
    assert AnimalShelter().front == None


def test_creating_dog_object():
    assert Dog().name == "WOOOFFF"


def test_creating_cat_object():
    assert Cat().name == "Meaowwww"


def test_enqueue_one_to_animal_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    assert new_shelter.front.name == "WOOOFFF"


def test_enqueue_many_to_animal_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("Dog")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("Cat")
    new_shelter.enqueue("cat")
    assert new_shelter.front.name == "WOOOFFF"


def test_dequeue_one_animal_from_shelter():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    assert new_shelter.dequeue("dog").name == "WOOOFFF"
    assert new_shelter.front == None


def test_dequeue_dog_from_shelter_of_many():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("Cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("Dog")
    assert new_shelter.dequeue("dog").name == "WOOOFFF"


def test_dequeue_cat_from_shelter_of_many():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    new_shelter.enqueue("Cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("Cat")
    new_shelter.enqueue("Dog")
    assert new_shelter.dequeue("cat").name == "Meaowwww"


def test_dequeue_from_empty_shelter():
    new_shelter = AnimalShelter()
    assert new_shelter.dequeue("dog") == None


def test_dequeue_first_from_shelter_no_preference():
    new_shelter = AnimalShelter()
    new_shelter.enqueue("dog")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("cat")
    new_shelter.enqueue("dog")
    assert new_shelter.dequeue().name == "WOOOFFF"
    assert new_shelter.front.name == "Meaowwww"
