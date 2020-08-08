import java.util.*;
import java.io.*;

public class UnionFind {
    private int id[];
    public UnionFind(int n){
        id = new int[n];
        for(int i = 0; i<n ; i++){
             id[i] = i;
        }
    }

    public boolean find(int a, int b){
        return id[a]==id[b];
    }

    public void union(int a, int b, int n){
        int a1 = a;
        int a2 = b;
        if(id[a]!=id[b]){
            for(int i = 0; i< n ;i++){

                if(id[i]==a2){
                    id[i] = id[a1]; /* here if you do id[i] = a1 it will put a1 in the place but not the the earlier unions made by a2*/
                }
            }

        }


    }
        

    
    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);
        System.out.println("Please enter a number");
        int n = ss.nextInt();
        UnionFind uf = new UnionFind(n);
        for(int i=0; i<n ; i++)
        {
        System.out.println(uf.id[i]);
        }
        System.out.println(uf.find(2,3));
        uf.union(2,3, n);
        uf.union(3,4,n);
        System.out.println(uf.find(2,4));
        for(int i=0; i<n ; i++)
        {
        System.out.print(uf.id[i]);
        }

        
       /* while(ss.hasNextInt())
        {
            int m = ss.nextInt();
            int p = ss.nextInt();

        
        System.out.println(n);
        System.out.println(m);
        System.out.println(p);
        }*/

    }
    
}