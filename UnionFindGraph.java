import java.util.*;

public class UnionFindGraph{
    public int id[];
     int ne;

    public UnionFindGraph(int n){
        id = new int[n];
        for(int i = 0; i<n ; i++){
            id[i] = i;
        }

    }

    public int root(int n){
        
        if(id[n] != n){
            n = id[n];
            root(n);
        }
        else{
           ne = n;            
        }
         return ne; 

    }

    public boolean find(int n, int m){
        return root(n)==root(m);


    }

    public void union(int n, int m){
        int q = m;
        id[q] = n; 


    }

    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);
        System.out.println("Please enter a number");
        int n = ss.nextInt();
        UnionFindGraph uf = new UnionFindGraph(n);
        for(int i=0; i<n ; i++)
        {
        System.out.print(uf.id[i]);
        }
        System.out.println(uf.find(2,3));
        uf.union(2,3);
        uf.union(3,4);
        System.out.println(uf.root(2));
        System.out.println(uf.root(3));
        System.out.println(uf.root(4));

        
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