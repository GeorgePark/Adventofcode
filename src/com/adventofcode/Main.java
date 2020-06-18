package com.adventofcode;

import com.adventofcode.day1.*;

public class Main {

    public static void main(String[] args) {
        FuelCounterUpper Day1 = new FuelCounterUpper();
        int fuel = Day1.calculateFuel(false);
        System.out.println(fuel);
        int fuelIncludingFuel = Day1.calculateFuel(true);
        System.out.println(fuelIncludingFuel);
    }
}