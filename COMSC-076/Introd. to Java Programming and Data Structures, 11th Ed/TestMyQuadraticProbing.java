/*
 * Huu Hung Nguyen
 * 12/09/2022
 * Assignment 11
 * Create a new concrete class that implements MyMap using open addressing
 * with quadratic probing. For simplicity, use f(key) = key % size as the hash
 * function, where size is the hash-table size. Initially, the hash-table size
 * is 4. The table size is doubled whenever the load factor exceeds
 * the threshold (0.5). The program has a driver program to test the class.
 */

import java.util.*;

public class TestMyQuadraticProbing {
    /** Main method */
    public static void main(String[] args) {
        // Create a map
        MyMap<String, Integer> map = new MyQuadraticProbing<>();
        map.put("Smith", 30);
        map.put("Anderson", 31);
        map.put("Lewis", 29);
        map.put("Cook", 29);
        map.put("Smith", 65);
        map.put("Huu", 22);
        map.put("Jay", 25);
        map.put("Jay", 24);

        System.out.println("Entries in map: " + map);

        System.out.println("\nThe age for Lewis is " + map.get("Lewis"));

        System.out.println("\nIs Smith in the map? " +
                map.containsKey("Smith"));
        System.out.println("Is Nguyen in the map? " +
                map.containsKey("Nguyen"));

        System.out.println("\nIs age 22 in the map? " +
                map.containsValue(22));
        System.out.println("Is age 33 in the map? " + map.containsValue(33));

        System.out.print("\nKeys in map: ");
        for (String key : map.keySet()) {
            System.out.print(key + " ");
        }
        System.out.println(); // new line

        System.out.print("\nValues in map: ");
        for (int value : map.values()) {
            System.out.print(value + " ");
        }
        System.out.println(); // new line

        map.remove("Smith");
        System.out.println("\nAfter remove Smith\nEntries in map: " + map);

        map.clear();
        System.out.println("\nAfter clear\nEntries in map: " + map);
    }
}

class MyQuadraticProbing<K, V> implements MyMap<K, V> {
    // Define the default hash table size. Must be a power of 2
    private static int DEFAULT_INITIAL_CAPACITY = 4;

    // Define the maximum hash table size. 1 << 30 is same as 2^30
    private static int MAXIMUM_CAPACITY = 1 << 30;

    // Current hash table capacity. Capacity is a power of 2
    private int capacity;

    // Define default load factor
    private static float DEFAULT_MAX_LOAD_FACTOR = 0.5f;

    // Specify a load factor used in the hash table
    private float loadFactorThreshold;

    // The number of entries in the map
    private int size = 0;

    // Hash table is an array list
    ArrayList<MyMap.Entry<K, V>> table;

    /** Construct a map with the default capacity and load factor */
    public MyQuadraticProbing() {
        this(DEFAULT_INITIAL_CAPACITY, DEFAULT_MAX_LOAD_FACTOR);
    }

    /**
     * Construct a map with the specified initial capacity and
     * default load factor
     */
    public MyQuadraticProbing(int initialCapacity) {
        this(initialCapacity, DEFAULT_MAX_LOAD_FACTOR);
    }

    /**
     * Construct a map with the specified initial capacity
     * and load factor
     */
    public MyQuadraticProbing(int initialCapacity,
            float loadFactorThreshold) {
        if (initialCapacity > MAXIMUM_CAPACITY)
            this.capacity = MAXIMUM_CAPACITY;
        else
            this.capacity = trimToPowerOf2(initialCapacity);

        this.loadFactorThreshold = loadFactorThreshold;
        table = new ArrayList<>();
        for (int i = 0; i < capacity; i++) {
            table.add(null);
        }
    }

    @Override /** Remove all of the entries from this map */
    public void clear() {
        size = 0;
        removeEntries();
    }

    @Override /** Return true if the specified key is in the map */
    public boolean containsKey(K key) {
        if (get(key) != null)
            return true;
        else
            return false;
    }

    @Override /** Return true if this map contains the value */
    public boolean containsValue(V value) {
        for (int i = 0; i < capacity; i++) {
            if (table.get(i) != null) {
                if (table.get(i).getValue() == value)
                    return true;
            }
        }

        return false;
    }

    @Override /** Return a set of entries in the map */
    public Set<MyMap.Entry<K, V>> entrySet() {
        Set<MyMap.Entry<K, V>> set = new HashSet<>();

        for (int i = 0; i < capacity; i++) {
            if (table.get(i) != null) {
                set.add(table.get(i));
            }
        }

        return set;
    }

    @Override /** Return the value that matches the specified key */
    public V get(K key) {
        int i = hash(key.hashCode());
        int startI = i;
        int j = 1;

        while (table.get(i) != null) {
            if (table.get(i).getKey().equals(key)) {
                return table.get(i).getValue();
            }

            i = (startI + j * j) % capacity;
            j++;
        }

        return null;
    }

    @Override /** Return true if this map contains no entries */
    public boolean isEmpty() {
        return size == 0;
    }

    @Override /** Return a set consisting of the keys in this map */
    public Set<K> keySet() {
        Set<K> set = new HashSet<>();

        for (int i = 0; i < capacity; i++) {
            if (table.get(i) != null) {
                set.add(table.get(i).getKey());
            }
        }

        return set;
    }

    @Override /** Add an entry (key, value) into the map */
    public V put(K key, V value) {
        int i = hash(key.hashCode());
        int startI = i;
        int j = 1;

        while (table.get(i) != null) {
            // The key is already in the map
            if (table.get(i).getKey().equals(key)) {
                Entry<K, V> entry = table.get(i);
                V oldValue = entry.getValue();
                // Replace old value with new value
                entry.value = value;
                table.set(i, entry);
                // Return the old value for the key
                return oldValue;
            }

            i = (startI + j * j) % capacity;
            j++;
        }

        // Check load factor
        if (size >= capacity * loadFactorThreshold) {
            if (capacity == MAXIMUM_CAPACITY)
                throw new RuntimeException("Exceeding maximum capacity");

            rehash();
        }

        // Add a new entry (key, value) to hashTable[index]
        table.set(i, new MyMap.Entry<K, V>(key, value));

        size++; // Increase size

        return value;
    }

    @Override /** Remove the entries for the specified key */
    public void remove(K key) {
        int i = hash(key.hashCode());
        int startI = i;
        int j = 1;

        // Remove the first entry that matches the key from the map
        while (table.get(i) != null) {
            if (table.get(i).getKey().equals(key)) {
                table.remove(i);
                size--; // Decrease size
                break; // Remove just one entry that matches key
            }

            i = (startI + j * j) % capacity;
            j++;
        }
    }

    @Override /** Return the number of entries in this map */
    public int size() {
        return size;
    }

    @Override /** Return a set consisting of the values in this map */
    public Set<V> values() {
        Set<V> set = new HashSet<>();

        for (int i = 0; i < capacity; i++) {
            if (table.get(i) != null)
                set.add(table.get(i).getValue());
        }

        return set;
    }

    /** Hash function */
    private int hash(int hashCode) {
        return supplementalHash(hashCode) & (capacity - 1);
    }

    /** Ensure the hashing is evenly distributed */
    private static int supplementalHash(int h) {
        h ^= (h >>> 20) ^ (h >>> 12);
        return h ^ (h >>> 7) ^ (h >>> 4);
    }

    /** Return a power of 2 for initialCapacity */
    private int trimToPowerOf2(int initialCapacity) {
        int capacity = 1;
        while (capacity < initialCapacity) {
            capacity <<= 1;
        }

        return capacity;
    }

    /** Remove all entries from each bucket */
    private void removeEntries() {
        table.clear();
    }

    /** Rehash the map */
    private void rehash() {
        Set<Entry<K, V>> set = entrySet(); // Get entries
        capacity <<= 1; // Double capacity
        table = new ArrayList<>(); // Create a new hash table
        for (int i = 0; i < capacity; i++)
            table.add(null);
        size = 0; // Reset size to 0

        for (Entry<K, V> entry : set) {
            put(entry.getKey(), entry.getValue()); // Store to new table
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder("[");

        for (Entry<K, V> entry : table) {
            if (entry != null && table.size() > 0)
                builder.append(entry);
        }

        builder.append("]");
        return builder.toString();
    }
}

interface MyMap<K, V> {
    /** Remove all of the entries from this map */
    public void clear();

    /** Return true if the specified key is in the map */
    public boolean containsKey(K key);

    /** Return true if this map contains the specified value */
    public boolean containsValue(V value);

    /** Return a set of entries in the map */
    public Set<Entry<K, V>> entrySet();

    /** Return the first value that matches the specified key */
    public V get(K key);

    /** Return true if this map contains no entries */
    public boolean isEmpty();

    /** Return a set consisting of the keys in this map */
    public Set<K> keySet();

    /** Add an entry (key, value) into the map */
    public V put(K key, V value);

    /** Remove the entries for the specified key */
    public void remove(K key);

    /** Return the number of mappings in this map */
    public int size();

    /** Return a set consisting of the values in this map */
    public Set<V> values();

    /** Define inner class for Entry */
    public static class Entry<K, V> {
        K key;
        V value;

        public Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        @Override
        public String toString() {
            return "[" + key + ", " + value + "]";
        }
    }
}