# Data-Structures-and-Algorithms - Challenge Ten

## Step-by-Step: Insertion Sort

Say that you are given a list of integers in no perticular order and you would like them to be sorted. Without using any built-in functions, how would you do it?

One method would be to use what is called the "insertion sort" method (or algorithm) to sort the list of integers.

Insertion sort is best thought of like how one would sort playing cards in poker. Starting with one card in hand you pick-up your second card and, based on wither or not the second card's value is lower or higher, you put the second card to the right or left of the first card. You would continue to do this - "inserting" your newest card into the mix of sorted cards until every card was included.

```markdown
      _____   _____   _____    _____    _____   UNSORTED CARDS
     |6    | |9    | |5    |  |3    |  |4    |  [6,9,5,3,4]
     |  x  | |  x  | |  x  |  |  x  |  |  x  |
     |    6| |    9| |    5|  |    3|  |    4|
      ¯¯¯¯¯   ¯¯¯¯¯   ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯
```

```markdown
      _____     ↑      _____    _____    _____   SORTED CARDS
     |3    |    ↑     |5    |  |6    |  |9    |  [3,4,5,6,9]
     |  x  |  _____   |  x  |  |  x  |  |  x  |
     |    3| |4    |  |    5|  |    6|  |    9|
      ¯¯¯¯¯  |  x  |   ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯
             |    4|
              ¯¯¯¯¯
```

In this blog post, it is my goal to walk you through formulating an insertion sort algorithm of your own.

It can be helpful to use a deck of cards to visualize your sorting algorithm. For this walkthrough we will be using this input array: <b> [8, 4, 23, 42, 16, 15] </b> Lets get started.

1. The first playing card given to you will always be your reference point for 'greater' or 'lesser' value. If we are talking about a list or array of integers it is no different than sorting cards. Except that instead of using the first 'card' as the reference point, we are going to always be using the first <b>index</b> of the list/array.
   <br>
2. We will want to keep track of the sorted items in our list/array. For now the first index is considered sorted. In this case, <b>8 is the first index.</b>
   <br>
3. Now it is our goal to have every integer become sorted. We will want to iterate through the remaining elements in our list/array. For each <u>unsorted integer</u> we will want to find where it will be inserted in the <u>sorted integers</u>. Lets use two loops to iterate first through all of the unsorted integers then to loop through the sorted integers with the unsorted value to find where it needs to be inserted...

```q
Lets break that down further:
starting array: [8,4,23,42,16,15]
sorted value(s): 8
unsorted value(s): 4,23,42,16,15

FIRST LOOP:

> iterates through unsorted values: 4,23,42,16,15
> SECOND LOOP:
> will iterate "backwards" through sorted values: 8

As more values become sorted, there will be more sorted values
to iterate through and less unsorted values

PSEUDO CODE -
def insertion_sort(list_of_ints):
(loop#1)for unsorted_int in range(1,len(list_of_ints)): # keep track of unsorted_int value and index
(loop#2)while [there are sorted indexes to iterate through] and [the unsorted_int is less than the last sorted value]:
#update the last sorted value in sequence
#increment index towards the 0 index
```

<br>
4. Lets look at our example list of integers: [<span style="color: green;">8, </span><span style="color: red;">4, 23, 42, 16, 15</span>]. The number 8 is shown in green because when we are trying to use an insertion sort algorithim, and the <u>first index</u> is always considered to be sorted. Let's use this to visualize <span style="color: green;">green integers</span> as being the sorted values and <span style="color: red;">red integers</span> being unsorted values.
<br>
<br>
5. So as we iterate through our <u>unsorted integers</u> we will want to compare to the "last" sorted value. Meaning the sorted value with the highest index in the array. As we start our first loop notice that <span style="color: green;">8</span> is the "last" sorted value in the array and that <span style="color: red;">4</span> is the first unsorted integer that we encounter in our first loop. [<span style="color: green;">8, </span><span style="color: red;">4, 23, 42, 16, 15</span>] When we compare <span style="color: red;">4</span> to <span style="color: green;">8</span> we can tell that <span style="color: red;">4</span> is less than <span style="color: green;">8</span> and should be moved to the left. How do we do that?<br><br>We know that when we start our outer loop that we are starting at index 1 (not index 0 - that is our sorted value). We know that for each index along the way we will want to save the value of the first unsorted_integer. Let's start by assigning the value of the <b>list_of_ints[ i ]</b> (in this case: <span style="color: red;">4</span>) to a variable 'int_to_insert'.

```python
def insertion_sort(list_of_ints):

    for i in range(1, len(list_of_ints)): # starting outer loop at index 1
        int_to_insert = list_of_ints[i]
```

<br>
6. Great! So we have our outer loop started. We start at the first index and intend to iterate through all the unsorted integers <span style="color: red;">4, 23, 42, 16, 15</span> while keeping track of the unsorted value.<br><br>So now we need to iterate "backwards" through the sorted values in order to <u>insert</u> into our unsorted value "int_to_insert". Looking at a bit of the pseudo from earlier:
````

(loop#2) while [there are sorted indexes to iterate through] and [the unsorted_int is less than the last sorted value]:

<br>
The first part we need to define is <span style="color: blue;"> while [there are sorted indexes to iterate through] </span>. When iterating backwards, this by definition is your first index. <b>Index Zero</b>. So we need to say "while we are not past index zero". It is common to use the letter <b>j</b> to denote index in an inner loop. In this case j will represent the iteration through the sorted values.<br><br>We know that <b>i</b> is the starting index of our unsorted values. So we want <b>j</b> to be the "starting" index of our sorted values (going backwards). I'll give you an example:
```

array: [1, 2, 3, 6, 5, 40, 11]

say that we are half way sorted...
sorted values: [1, 2, 3, 6...
unsorted values: ...5, 40, 11]

starting index of unsorted values ( i ): index 4 (integer 5)
starting index of sorted values ( j ): index 3 (integer 6)

The index <b>j</b> is always going to be one index less than <b>i</b>. Just to the left. Let's define j and start our inner loop:

```python
def insertion_sort(list_of_ints):

    for i in range(1, len(list_of_ints)): # starting outer loop at index 1
        j = (i - 1)
        int_to_insert = list_of_ints[i]
        while j >= 0 #while there are still sorted values
```

Ok now we need to define the second part of our inner while-loop; <span style="color: blue;">while [the unsorted_int is less than the last sorted value]</span>.<br><br>We know what the "unsorted_int" is from earlier! We saved it as "int_to_insert".
`int_to_insert = list_of_ints[i]`

We also already know what the "last sorted value" would be! Because we have already defined j as the "start" of the sorted values - <b>that</b> is the <u>index</u> of "last sorted value".

`list_of_ints[j] = the "last sorted value"`

So let's put it all together and write our inner loop:

```python

def insertion_sort(list_of_ints):

    for i in range(1, len(list_of_ints)): # starting outer loop at index 1
        j = (i - 1)
        int_to_insert = list_of_ints[i]

        while j >= 0 and int_to_insert < list_of_ints[j]:
            # while there are still sorted values
            # and
            # while the integer to insert is less than the 'last' or largest sorted value


```

7. So we have an outer for-loop that will iterate the length of the list/array starting at index one. For each iteration it saves the value of that index as int_to_insert AND assigns (i - 1) to the variable j.<br><br>We now have the logic for our inner while-loop. While the int_to_insert is less than the 'last' sorted value and there are still sorted values in the list, we will... do something.<br><br>Remember back to the hand of cards in poker. If you started from the right and went left, you would <b>replace</b> the card to the left with the card coming from the right - IF it was smaller. We want to do the same thing here. If the conditional of our inner-loop is True, then we want to replace the two integers - i.e swap indexes. The value at index (j+1) will become the value at index j.
   `list_of_ints[j + 1] = list_of_ints[j]`
   For our inner loop to iterate we will need to incriment j by -1 each iteration.
   `j = (j - 1) or j -= 1`
   Lets put this in our function and see what it looks like so far.

```python

def insertion_sort(list_of_ints):

    for i in range(1, len(list_of_ints)): # starting outer loop at index 1
        j = (i - 1)
        int_to_insert = list_of_ints[i]

        while j >= 0 and int_to_insert < list_of_ints[j]:
            list_of_ints[j + 1] = list_of_ints[j]
            j -= 1


```

Perfect. Let's see if that works with the example we started this walkthrough with. [<span style="color: green;">8, </span><span style="color: red;">4, 23, 42, 16, 15</span>]

```python

4 is index 1 ( i )
8 is index 0 ( j ) #remember, j = (i - 1)

def insertion_sort(list_of_ints):

## we start our outer loop at 1 to length of list/array --> range(1, len(list_of_ints))

    for i in range(1, len(list_of_ints)):
        j = 0  ##(i - 1)
        int_to_insert = 4   ##list_of_ints[1]

        while (0) >= 0 and (4) < (8): ##TRUE
            list_of_ints[1] = (8)  ##[8, 8, 23, 42, 16, 15]
            (0) -= 1

## 0 -=1 --> j becomes -1. while-loop conditional j >= 0 fails • False

## inner loop ends and moves onto i = 2

## We never assigned list_of_ints[0] to be 4

## our list/array looks like [8, 8, 23, 42, 16, 15]

```

<br>
8. We need to add another line before the next iteration of the outer loop. Remember that we assigned the value at index i to <b>int_to_insert</b>? We need to use it!<br><br>Right above we saw that when j increments to -1 the inner loop ends. That is when we are at index -1, which is past the sorted integers in the list. At that point, (j + 1) would be 0. Index 0 is the first index in the list/array. So outside our inner loop we just need to add one line.
``` list_of_ints[j + 1] = int_to_insert ```

When we leave the inner while-loop either we have reached index -1 or we have reached a point where the int_to_insert is greater than the integer at the new index j. After j -= 1. Either way we want the integer at j + 1 to be the int_to_insert that we assigned earlier.<br><br>Let's take a final look:

```python
def insertion_sort(list_of_ints):

    for i in range(1, len(list_of_ints)): # starting outer loop at index 1
        j = (i - 1)
        int_to_insert = list_of_ints[i]

        while j >= 0 and int_to_insert < list_of_ints[j]:
            list_of_ints[j + 1] = list_of_ints[j]
            j -= 1
        list_of_ints[j + 1] = int_to_insert
```

<br>
9. Let's test it out.<br><br>[<span style="color: green;">8, </span><span style="color: red;">4, 23, 42, 16, 15</span>]<br>The int[ j ] starts here as <span style="color: green;">8</span> and int_to_insert being <span style="color: red;">4</span>. While-loop passes, True, index 1 becomes <span style="color: green;">8</span>, j becomes -1, then index 0 becomes <span style="color: red;">4</span>.<br><br>So far so good.[4, <span style="color: green;">8, </span><span style="color: red;">23, 42, 16, 15</span>]The int[ j ] starts here as <span style="color: green;">8</span> and int_to_insert being <span style="color: red;">23</span>. While-loop fails, False, index 2 stays <span style="color: red;">23</span>.<br><br>[4, 8, <span style="color: green;">23, </span><span style="color: red;">42, 16, 15</span>]The int[ j ] starts here as <span style="color: green;">23</span> and int_to_insert being <span style="color: red;">42</span>. While-loop fails, False, index 3 stays <span style="color: red;">42</span>.<br><br>[4, 8, 23, <span style="color: green;">42, </span><span style="color: red;">16, 15</span>]The int[ j ] starts here as <span style="color: green;">42</span> and int_to_insert being <span style="color: red;">16</span>. While-loop passes, True, index 4 becomes <span style="color: green;">42, </span>, j becomes 2. While-loop passes again, True (16 < 23), index 3 becomes 23, j becomes 1. While-loop fails, False (16 is not less than 8), index 2 becomes <span style="color: red;">16</span>.<br><br>[4, 8, 16, 23, <span style="color: green;">42, </span><span style="color: red;">15</span>] The int[ j ] starts here as <span style="color: green;">42</span> and int_to_insert being <span style="color: red;">15</span>. While-loop passes, True, index 5 becomes <span style="color: green;">42, </span>, j becomes 3. While-loop passes again, True (15 < 23), index 4 becomes 23, j becomes 2. While-loop passes again, True (15 < 16), index 3 becomes 16, j becomes 1. While-loop fails, False (15 is not less than 8), index 2 becomes <span style="color: red;">15</span>.<br><br>The final list/array looks as expected: [4, 8, 15, 16, 23, 42]
