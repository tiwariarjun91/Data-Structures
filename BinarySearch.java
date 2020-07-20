

public class BinarySearch {

    public static int rank( int n,  int[] p) {
        int low = 0;
        int high = p.length - 1;
        int result = 0;
        while (low <= high) {
           int  mid = low + high  / 2;
            if (n <p[mid]) {
                high = mid - 1;
                return 1;
            } else if (n > p[mid]) {
                low = mid + 1;
                return 1;
            } else {
                result = mid;
                return result;
            }
            
        }
            return result;
    }

    public static void main( String[] args) {
         int a = 3;
         int[] k = { 1, 3, 5, 7, 8, 9, 20, 22, 24, 25, 34, 40, 45, 67, 70, 77, 89, 100, 120, 124, 134, 156, 178,
                198, 201, 220 };
        int r ;
        r = rank(a, k);
        System.out.println("The number "+a+" is at "+r+" position !!!!!!");
    }
}