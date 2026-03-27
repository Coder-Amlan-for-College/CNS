import java.util.*;
public class VigenereCipherEncryption{
   
   public static char[] prepareKey(char[]k,int n){
       char[]arr = new char[n];
       int m=k.length;
       for(int i=0;i<n;i++){
          arr[i]=k[i%m];
       }
       return arr;
   }
    public static String vigereneCipherEncryption(char[]k,char[]plain_text){
      char[]key = prepareKey(k,plain_text.length);
      
      int n = plain_text.length;
      char[]ct = new char[plain_text.length];
      
      for(int i=0;i<n;i++){
        ct[i]=(char)((key[i]-'A'+plain_text[i]-'A')%26+'A');
      }
      return new String(ct);
   }
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     System.out.print("Plain Text: ");
     String plain_text = sc.next().trim().toUpperCase();
     System.out.print("Key: ");
     String key = sc.next().trim().toUpperCase();
     
     String ct=vigereneCipherEncryption(key.toCharArray(),plain_text.toCharArray());
     System.out.println("Cipher Text: "+ct);
     sc.close(); 
   }
}