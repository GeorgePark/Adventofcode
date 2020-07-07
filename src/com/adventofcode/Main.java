package com.adventofcode;

import com.adventofcode.day1.*;
import com.adventofcode.day2.*;
import com.adventofcode.day4.*;

public class Main {

    private static void day1() {
        FuelCounterUpper day1 = new FuelCounterUpper();
        int fuel = day1.calculateFuel(false);
        System.out.println(fuel);
        int fuelIncludingFuel = day1.calculateFuel(true);
        System.out.println(fuelIncludingFuel);
    }

    private static void day2() {
        GravityAssist day2 = new GravityAssist();
        int gravityAssistValue = day2.run();
        System.out.println(gravityAssistValue);

        int targetOutput = 19690720;
        int[] inputs = day2.run(targetOutput);
        System.out.println(inputs[0] + " " + inputs[1]);
    }

    private static void day4(){
        // Range of passwords (147981-691423)
        long startTime = System.nanoTime();
        PasswordProtection day4 = new PasswordProtection();
        int numberOfPasswords = day4.generatePasswords(147981, 691423);
        System.out.println(numberOfPasswords);
        long stopTime = System.nanoTime();
        System.out.println((stopTime-startTime) / 1000000);
        startTime = System.nanoTime();
        numberOfPasswords = day4.generateStricterPasswords(147981, 691423);
        System.out.println(numberOfPasswords);
        stopTime = System.nanoTime();
        System.out.println((stopTime-startTime) / 1000000);
    }

    public static void main(String[] args) {
//        day1();
//        day2();
//        day4();

    }
}