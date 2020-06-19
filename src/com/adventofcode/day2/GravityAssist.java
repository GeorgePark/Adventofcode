package com.adventofcode.day2;

public class GravityAssist {
    // The Intcode program used
    private int [] gravityAssistProgram = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,
            10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,
            79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,
            115,2,119,1, 119,10,0,99,2,14,0,0};

    private void ResetProgram(){
        gravityAssistProgram = new int[]{1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,
                10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,
                79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,
                115,2,119,1, 119,10,0,99,2,14,0,0};
    }

    /**
     * Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to
     * the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the
     * program, replace position 1 with the value 12 and replace position 2 with the value 2.
     */
    private void FixValues(){
        gravityAssistProgram[1] = 12;
        gravityAssistProgram[2] = 2;
    }

    /**
     * Overloading previous method to allow for custom values when setting initial values in position 1 and 2
     * @param i: value of the first position
     * @param j: value of the second position
     */
    private void FixValues(int i, int j){
        gravityAssistProgram[1] = i;
        gravityAssistProgram[2] = j;
    }

    /**
     * Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three
     *     integers immediately after the opcode tell you these three positions - the first two indicate the positions
     *     from which you should read the input values, and the third indicates the position at which the output
     *     should be stored.
     * @param i: value of the head of the Intcode program
     */
    private void DoOpcode1(int i){
        int value1 = gravityAssistProgram[gravityAssistProgram[i+1]];
        int value2 = gravityAssistProgram[gravityAssistProgram[i+2]];
        int position3 = gravityAssistProgram[i+3];
        gravityAssistProgram[position3] = value1 + value2;
    }

    /**
     * Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
     * integers after the opcode indicate where the inputs and outputs are, not their values.
     * @param i: value of the head of the Intcode program
     */
    private void DoOpcode2(int i){
        int value1 = gravityAssistProgram[gravityAssistProgram[i+1]];
        int value2 = gravityAssistProgram[gravityAssistProgram[i+2]];
        int position3 = gravityAssistProgram[i+3];
        gravityAssistProgram[position3] = value1 * value2;
    }

    private void DoOpcodes() {
        int i = 0;
        try {
            while (gravityAssistProgram[i] != 99) {
                if (gravityAssistProgram[i] == 1) {
                    DoOpcode1(i);
                } else if (gravityAssistProgram[i] == 2) {
                    DoOpcode2(i);
                } else {
                    System.out.println("This shouldn`t happen, Opcode not recognised" + " " + gravityAssistProgram[i] + " " + i);
                }
                i+=4;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at
     * the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates
     * what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an
     * unknown opcode means something went wrong.
     * @return The value at the front of the Intcode program
     */
    public int run() {
        FixValues();
        DoOpcodes();
        return gravityAssistProgram[0];
    }

    /**
     * Overloading previous run method to allow for
     * @param value: value to be set at the first position
     * @return
     */
    public int[] run(int value) {
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                ResetProgram();
                FixValues(i, j);
                DoOpcodes();
                if (gravityAssistProgram[0] == value) {
                    return new int[] {i,j};
                }
            }
        }
        return new int[] {};
    }
}
