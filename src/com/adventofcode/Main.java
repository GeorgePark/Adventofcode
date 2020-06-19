package com.adventofcode;

import com.adventofcode.day1.*;
import com.adventofcode.day2.GravityAssist;

public class Main {

    private static void day1() {
        FuelCounterUpper Day1 = new FuelCounterUpper();
        int fuel = Day1.calculateFuel(false);
        System.out.println(fuel);
        int fuelIncludingFuel = Day1.calculateFuel(true);
        System.out.println(fuelIncludingFuel);
    }

    private static void day2() {
        GravityAssist Day2 = new GravityAssist();
        int gravityAssistValue = Day2.run();
        System.out.println(gravityAssistValue);

        int targetOutput = 19690720;
        int[] inputs = Day2.run(targetOutput);
        System.out.println(inputs[0] + " " + inputs[1]);
    }

    public static void main(String[] args) {
        day1();
        day2();
    }
}