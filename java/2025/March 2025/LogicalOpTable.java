/* Logical Operators Table
 * In this program, I have demonstrated the comparison statements that Java provides in a table.
 * In order to do this, I have used two boolean variables - 'p' and 'q'.
 * How to run: this program does not have any additional requirements and can be run directly in the command line.
*/

class LogicalOpTable {
    public static void main(String[] args) {
        // Initialize variables
        boolean p, q;

        // Table headers
        System.out.println("P\tQ\tAND\tOR\tXOR\tNOT");
      
        p = true; q = true;
        System.out.print(p + "\t" + q + "\t");
        System.out.print((p&q) + "\t" + (p|q) + "\t");
        System.out.println((p^q) + "\t" + (!p));

        p = true; q = false;
        System.out.print(p + "\t" + q + "\t");
        System.out.print((p&q) + "\t" + (p|q) + "\t");
        System.out.println((p^q) + "\t" + (!p));

        p = false; q = true;
        System.out.print(p + "\t" + q + "\t");
        System.out.print((p&q) + "\t" + (p|q) + "\t");
        System.out.println((p^q) + "\t" + (!p));

        p = false; q = false;
        System.out.print(p + "\t" + q + "\t");
        System.out.print((p&q) + "\t" + (p|q) + "\t");
        System.out.println((p^q) + "\t" + (!p));
    }
}

