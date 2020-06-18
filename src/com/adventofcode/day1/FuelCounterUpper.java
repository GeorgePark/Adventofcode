package com.adventofcode.day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately
calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs
you to bring him measurements from fifty stars.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
The Elves quickly load you into a spacecraft and prepare to launch.
At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel
required yet.
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take
its mass, divide by three, round down, and subtract 2.
For example:
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for
the mass of each module (your puzzle input see Input Day1.txt), then add together all the fuel values.
What is the sum of the fuel requirements for all of the modules on your spacecraft?
*/
public class FuelCounterUpper {

    /**
     * Sets the value of @requiredFuel to the required fuel level
     * @return requiredFuel, the required amount of fuel
     */
    public int calculateFuel (boolean withFuel) {
        int requiredFuel = 0;
        try {
            Scanner scanner = new Scanner(new File("./Input/Day1.txt"));
            while (scanner.hasNextLine()) {
                if (withFuel) {
                    requiredFuel += calculateFuelWithFuel(Integer.parseInt(scanner.nextLine()));
                } else {
                    requiredFuel += findFuel(Integer.parseInt(scanner.nextLine()));
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return requiredFuel;
    }

    /**
     * To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2
     * @param payload The payload mass for which the fuel needs to be calculated
     * @return The calculated amount of fuel to launch the payload
     */
    private int findFuel(int payload){
        return Math.floorDiv(payload, 3) - 2;
    }


    /**
     * Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.
     * However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require
     * negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead
     * handled by wishing really hard, which has no mass and is outside the scope of this calculation.
     * @param payload The payload mass for which the fuel needs to be calculated
     * @return The calculated amount of fuel to launch the payload including fuel to launch fuel
     */
    private int calculateFuelWithFuel (int payload) {
        int requiredFuel = findFuel(payload);
        int extraFuel = findFuel(requiredFuel);
        while (extraFuel > 0) {
            requiredFuel += extraFuel;
            extraFuel = findFuel(extraFuel);
        }
        return requiredFuel;
    }
}
