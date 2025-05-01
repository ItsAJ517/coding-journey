/*
 * Gallons to litres converter
 * This program converts gallons to litres, from 1 - 100.
 * How to run: this file does not have any additional requirements and can be run directly in the command line.
 */

 class GalToLitTable {
    public static void main(String[] args) {
        // Initialize variables
        double gallons, litres;
        int counter;

        counter = 0;

        // Begin conversions
        for(gallons = 1; gallons <= 100; gallons++) {
            litres = gallons * 3.7854;
            System.out.println(gallons + " gallons is " + litres + " litres");

            counter++;
            if(counter == 10) {
                System.out.println();
                counter = 0;
            }
        }
    }
}
