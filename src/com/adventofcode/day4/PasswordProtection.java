package com.adventofcode.day4;

import java.util.ArrayList;
import java.util.HashMap;

public class PasswordProtection {
/*   You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the
    password on a sticky note, but someone threw it out.

    However, they do remember a few key facts about the password:

    - It is a six-digit number.
    - The value is within the range given in your puzzle input. (147981-691423)
    - Two adjacent digits are the same (like 22 in 122345).
    - Going from left to right, the digits never decrease; they only ever increase or stay the same.*/

    /**
     * Check whether there is a group of at least two adjacent digits that are the same
     * @param number: the number for which we are checking the requirement
     * @return whether the number satisfies the requirement
     */
    private static boolean checkAdjacent(int number) {
        int lastSeen = 10; // always greater than any digit
        int current;

        while (number > 0) {
            current = number % 10;
            if (lastSeen == current)
                return true;
            lastSeen = current;
            number /= 10;
        }
        return false;
    }

    /* Additional requirement for part two: An Elf just remembered one more important detail: the two adjacent matching
    digits are not part of a larger group of matching digits. (Note that checkAdjacentStrict only works for this
    requirement in combination with the requirement that all digits have to be increasing of equal from left to right)
    */

    /**
     * Check whether there exists at least one group of exactly two adjacent digits that are the same
     * @param number: the number for which we are checking the requirement
     * @return whether the number satisfies the requirement
     */
    private static boolean checkAdjacentStrict(int number) {
        int lastSeen = 10; // always greater than any digit
        int current;
        HashMap<Integer, Boolean> adjacent = new HashMap<>();

        while (number > 0) {
            current = number % 10;
            if (lastSeen == current)
                if (adjacent.containsKey(current)) {
                    adjacent.put(current, false);
                } else {
                    adjacent.put(current,true);
                }
            lastSeen = current;
            number /= 10;
        }
        return adjacent.containsValue(true);
    }

    /**
     * Check whether all digits in a number are increasing or equal (from left to right)
     * @param number: the number for which we are checking the requirement
     * @return whether the number satisfies the requirement
     */
    private static boolean checkIncreasing(int number) {
        int lastSeen = 10; // always greater than any digit
        int current;

        // Return false if lastSeen (digit behind current digit) < current digit
        while (number > 0) {
            current = number % 10;
            if (lastSeen < current)
                return false;
            lastSeen = current;
            number /= 10;
        }
        return true;
    }

    /**
     * First start with a brute force method by checking whether a number satisfies all requirements for all numbers
     * between the two values in the input
     *
     * @param start:
     * @param end:
     * @return The amount of passwords that meet the requirements
     */
    public int generatePasswords(int start, int end) {
        ArrayList<Integer> passwords = new ArrayList<>();
        for (int i = start + 1; i < end; i++) {
            if (checkAdjacent(i) && checkIncreasing(i)) {
                passwords.add(i);
            }
        }
        return passwords.size();
    }

    /**
     * First start with a brute force method by checking whether a number satisfies all requirements for all numbers
     * between the two values in the input with stricter requirements
     *
     * @param start:
     * @param end:
     * @return The amount of passwords that meet the requirements
     */
    public int generateStricterPasswords(int start, int end) {
        ArrayList<Integer> passwords = new ArrayList<>();
        for (int i = start + 1; i < end; i++) {
            if (checkAdjacentStrict(i) && checkIncreasing(i)) {
                passwords.add(i);
            }
        }
        return passwords.size();
    }
}
