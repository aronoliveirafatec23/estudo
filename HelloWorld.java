import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        String name = "";
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        name = sc.next();
        System.out.println(String.format("Hello World - %s!", name));
    }
}