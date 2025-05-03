/* Gallons to litres converter
 * This program converts gallons to litres, for 1-100 gallons.
 * How to run: this program does not have any additional requirements and can be run directly in the command line.
 */

 class GalToLitTable {
    public static void main(String[] args) {
        double gallons, litres;
        int counter;

        counter = 0;
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
