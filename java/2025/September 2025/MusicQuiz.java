// Mini Quiz

// Question class - used for each question
class Question {
    String question;
    String opt_a, opt_b, opt_c, opt_d;
    char correct_ans;

    Question(String q, String a, String b, String c, String d, char correct) {
        question = q;
        opt_a = a;
        opt_b = b;
        opt_c = c;
        opt_d = d;
        correct_ans = correct;
    }

    void showQuestionDetails() {
        System.out.println(question);
        System.out.println("  A: " + opt_a);
        System.out.println("  B: " + opt_b);
        System.out.println("  C: " + opt_c);
        System.out.println("  D: " + opt_d);
    }

    boolean isValid(char ans) {
        if(ans < 'A' | ans > 'D') return false;
        else return true;
    }

    boolean inputAns() throws java.io.IOException {
        char ans, ignore;

        do {
            System.out.println("Enter A, B, C, or D: ");
            ans = (char) System.in.read();

            do {
                ignore = (char) System.in.read();
            } while(ignore != '\n');

        } while( !isValid(ans) );

        if(ans == correct_ans) {
            System.out.println("Correct!");
            return true;
        }
        else {
            System.out.println("Wrong!");
            return false;
        }
    }
}


class MusicQuiz {
    public static void main(String[] args) throws java.io.IOException {
        int score = 0;

        // Create questions
        Question q1 = new Question("What is the name of the cyclic rhythmic framework used in Indian Classical songs?", 
        "Raga", "Tala", "Son Clave", "Wazn", 'B');

        Question q2 = new Question("Which region of the world is Calypso music from?", "Middle East", "Greece", "Africa", "Caribbean", 'D');
        
        Question q3 = new Question("What is a common time signature used in Greek folk music?", "4/4", "3/4", "5/8", "6/8", 'C');
        
        // Ask questions
        q1.showQuestionDetails();
        if(q1.inputAns()) score++;
        System.out.println("Score: " + score);
        
        q2.showQuestionDetails();
        if(q2.inputAns()) score++;
        System.out.println("Score: " + score);

        q3.showQuestionDetails();
        if(q3.inputAns()) score++;
        System.out.println("Score: " + score);
    }
}
