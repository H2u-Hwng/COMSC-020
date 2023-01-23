/*
 * Huu Hung Nguyen
 * 11/16/2022
 * Assignment 9
 * The code implements a revised MyLinkedList class. Next, it has a driver
 * program that initializes a linked list with 10 names. Then, it completely
 * tests every one of its methods of ensure that the class meets all its
 * requirements.
 */

import java.util.*;

public class TestMyLinkedList {
    /** Main method */
    public static void main(String[] args) {
        // Create a list for strings
        MyLinkedList<String> list = new MyLinkedList<>();
    
        // Add elements to the list
        list.add("America"); // Add it to the list
        System.out.println("(1) " + list);
    
        list.add(0, "Canada"); // Add it to the beginning of the list
        System.out.println("(2) " + list);
    
        list.add("Russia"); // Add it to the end of the list
        System.out.println("(3) " + list);
        
        list.addFirst("Chicago"); // Add it to the beginning of the list
        System.out.println("(4) " + list);

        list.addLast("France"); // Add it to the end of the list
        System.out.println("(5) " + list);
    
        list.add(2, "Germany"); // Add it to the list at index 2
        System.out.println("(6) " + list);
    
        list.add(5, "Norway"); // Add it to the list at index 5
        System.out.println("(7) " + list);
    
        list.add(0, "Poland"); // Same as list.addFirst("Poland")
        System.out.println("(8) " + list);
    
        list.add("Denver"); // Same as list.addLast("Denver")
        System.out.println("(9) " + list);

        list.add(8, "Dallas"); // Add it to the list at index 8
        System.out.println("(10) " + list);

        list.add(9, "America"); // Add it to the list at index 9
        System.out.println("(11) " + list);

        // Set elements in the list
        list.set(3, "Thailand"); // set it to the list at index 3
        System.out.println("(12) " + list);

        // Remove elements from the list
        list.removeFirst(); // Remove the first element
        System.out.println("(13) " + list);
    
        list.remove(2); // Remove the element at index 2
        System.out.println("(14) " + list);
    
        list.removeLast(); // Remove the last element
        System.out.print("(15) " + list + "\n(16) ");

        for (String s: list)
            System.out.print(s.toUpperCase() + " ");
        System.out.println(); // new line
        System.out.println(); // new line
        
        // Check whether elements are in the list
        System.out.println("List has Chicago: " + list.contains("Chicago"));
        System.out.println("List has Vietnam: " + list.contains("Vietnam"));
        System.out.println(); // new line

        // Get elements from the list
        System.out.println("The first element: " + list.getFirst());
        System.out.println("The element at index 5: " + list.get(5));
        System.out.println("The last element: " + list.getLast());
        System.out.println(); // new line

        // Get index of elements from the list
        System.out.println("Index of Chicago: " + list.indexOf("Chicago"));
        System.out.println("Index of America: " + list.indexOf("America"));
        System.out.println(); // new line
        
        // Get last index of elements from the list
        System.out.println("The last index of Dallas: " + 
                            list.lastIndexOf("Dallas"));
        System.out.println("The last index of America: " + 
                            list.lastIndexOf("America"));
        System.out.println(); // new line
        
        list.clear();
        System.out.println("After clearing the list, the list size is "
                           + list.size());
    }
}

class MyLinkedList<E> implements MyList<E> {
    private Node<E> head, tail;
    private int size = 0; // Number of elements in the list
  
    /** Create an empty list */
    public MyLinkedList() {
    }

    /** Create a list from an array of objects */
    public MyLinkedList(E[] objects) {
        for (int i = 0; i < objects.length; i++)
            add(objects[i]); 
    }

    /** Return the head element in the list */
    public E getFirst() {
        if (size == 0) {
            return null;
        } else {
            return head.element;
        }
    }

    /** Return the last element in the list */
    public E getLast() {
        if (size == 0) {
            return null;
        } else {
            return tail.element;
        }
    }

    /** Add an element to the beginning of the list */
    public void addFirst(E e) {
        Node<E> newNode = new Node<>(e); // Create a new node
        newNode.next = head; // link the new node with the head
        head = newNode; // head points to the new node
        size++; // Increase list size

        if (tail == null) // the new node is the only node in list
            tail = head;
    }

    /** Add an element to the end of the list */
    public void addLast(E e) {
        Node<E> newNode = new Node<>(e); // Create a new for element e

        if (tail == null) {
            head = tail = newNode; // The new node is the only node in list
        } else {
            tail.next = newNode; // Link the new with the last node
            tail = newNode; // tail now points to the last node
        }
        size++; // Increase size
    }

    @Override /** Add a new element at the specified index 
    * in this list. The index of the head element is 0 */
    public void add(int index, E e) {
        if (index == 0) {
            addFirst(e);
        } else if (index >= size) {
            addLast(e);
        } else {
            Node<E> current = head;

            for (int i = 1; i < index; i++) {
                current = current.next;
            }

            Node<E> temp = current.next;
            current.next = new Node<>(e);
            (current.next).next = temp;
            size++;
        }
    }

    /** Remove the head node and
     *  return the object that is contained in the removed node. */
    public E removeFirst() {
        if (size == 0) {
            return null;
        } else {
            E temp = head.element;
            head = head.next;
            size--;

            if (head == null) {
                tail = null;
            }

            return temp;
        }
    }

    /** Remove the last node and
     * return the object that is contained in the removed node. */
    public E removeLast() {
        if (size == 0) {
            return null;
        } else if (size == 1) {
            E temp = head.element;
            head = tail = null;
            size = 0;

            return temp;
        } else {
            Node<E> current = head;

            for (int i = 0; i < size - 2; i++) {
                current = current.next;
            }

            E temp = tail.element;
            tail = current;
            tail.next = null;
            size--;

            return temp;
        }
    }

    @Override /** Remove the element at the specified position in this 
    *  list. Return the element that was removed from the list. */
    public E remove(int index) {   
        if (index < 0 || index >= size) {
            return null;
        } else if (index == 0) {
            return removeFirst();
        } else if (index == size - 1) {
            return removeLast();
        } else {
            Node<E> previous = head;

            for (int i = 1; i < index; i++) {
                previous = previous.next;
            }

            Node<E> current = previous.next;
            previous.next = current.next;
            size--;

            return current.element;
        }
    }

    @Override /** Override toString() to return elements in the list */
    public String toString() {
        StringBuilder result = new StringBuilder("[");
        Node<E> current = head;

        for (int i = 0; i < size; i++) {
            result.append(current.element);
            current = current.next;

            if (current != null) {
                result.append(", "); // Separate two elements with a comma
            } else {
                result.append("]"); // Insert the closing ] in the string
            }
        }
        return result.toString();
    }

    @Override /** Clear the list */
    public void clear() {
        size = 0;
        head = tail = null;
    }

    @Override /** Return true if this list contains the element e */
    public boolean contains(Object e) {
        if (size == 0) {
            return false;
        } else {
            Node<E> current = head;

            while (current != null) {
                if (current.element.equals(e))
                    return true;

                current = current.next;
            }
        }
        return false;
    }

    @Override /** Return the element at the specified index */
    public E get(int index) {
        if (index < 0 || index >= size) {
            return null;
        } else {
            Node<E> current = head;

            for (int i = 0; i < size; i++) {
                if (i == index)
                    return current.element;

                current = current.next;
            }
        }
        return null;
    }

    @Override /** Return the index of the head matching element in 
    *  this list. Return -1 if no match. */
    public int indexOf(Object e) {
        if (size == 0) {
            return -1;
        } else {
            Node<E> current = head;
            int index = 0;

            while (current != null) {
                if (current.element.equals(e))
                    return index;

                current = current.next;
                index++;
            }
        }
        return -1;
    }

    @Override /** Return the index of the last matching element in 
    *  this list. Return -1 if no match. */
    public int lastIndexOf(E e) {
        if (size == 0) {
            return -1;
        } else {
            Node<E> current = head;
            int index = 0;
            int lastIndex = -1;

            while (current != null) {
                if (current.element.equals(e))
                    lastIndex = index;

                current = current.next;
                index++;
            }

            return lastIndex;
        }
    }

    @Override /** Replace the element at the specified position 
    *  in this list with the specified element. */
    public E set(int index, E e) {
        if (index < 0 || index >= size) {
            return null;
        } else {
            Node<E> current = head;
            for (int i = 0; i < size; i++) {
                if (i == index) {
                    E old = current.element;
                    current.element = e;
                    return old;
                }

                current = current.next;
            }
        }
        return null;
    }

    @Override /** Override iterator() defined in Iterable */
    public Iterator<E> iterator() {
        return new LinkedListIterator();
    }

    private class LinkedListIterator implements Iterator<E> {
        private Node<E> current = head; // Current index 
        
        @Override
        public boolean hasNext() {
            return (current != null);
        }

        @Override
        public E next() {
            E e = current.element;
            current = current.next;
            return e;
        }

        @Override
        public void remove() {
            current = current.next;
        }
    }
  
    private static class Node<E> {
        E element;
        Node<E> next;

        public Node(E element) {
            this.element = element;
        }
    }
  
    @Override /** Return the number of elements in this list */
    public int size() {
        return size;
    }
}

interface MyList<E> extends Collection<E> {
    /** Add a new element at the specified index in this list */
    public void add(int index, E e);

    /** Return the element from this list at the specified index */
    public E get(int index);

    /** Return the index of the first matching element in this list.
     *  Return -1 if no match. */
    public int indexOf(Object e);

    /** Return the index of the last matching element in this list
     *  Return -1 if no match. */
    public int lastIndexOf(E e);

    /** Remove the element at the specified position in this list
     *  Shift any subsequent elements to the left.
     *  Return the element that was removed from the list. */
    public E remove(int index);

    /** Replace the element at the specified position in this list
     *  with the specified element and returns the new set. */
    public E set(int index, E e);
    
    @Override /** Add a new element at the end of this list */
    public default boolean add(E e) {
        add(size(), e);
        return true;
    }

    @Override /** Return true if this list contains no elements */
    public default boolean isEmpty() {
        return size() == 0;
    }

    @Override /** Remove the first occurrence of the element e 
    *  from this list. Shift any subsequent elements to the left.
    *  Return true if the element is removed. */
    public default boolean remove(Object e) {
        if (indexOf(e) >= 0) {
            remove(indexOf(e));
            return true;
        } else {
            return false;
        }
    }
}