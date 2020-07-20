import java.util.*;
public class Average {
     public static void main(String[] args) {

        int i;
        int sum = 0;
        int n;
        int count ;
        Scanner ss = new Scanner(System.in);
        System.out.println("How many numbers do you wish to enter");
        count = ss.nextInt();
        

        for(i = 0; i< count ; i++){
            System.out.println("Please enter the number "+ (i+1)+" ");
            n = ss.nextInt();
            sum = sum + n;
        }

        n = sum/count;
        System.out.println("The sum of "+count+" numbers is "+sum+" and the average is "+ n);


        
    }
}