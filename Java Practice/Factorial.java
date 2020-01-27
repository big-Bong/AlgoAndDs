import java.util.Scanner;

public class Factorial {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter value for which factorial needs to be calculated: ");
		int n = input.nextInt();
		Factorial f = new Factorial();
		System.out.println("The factorial for the input is: "+f.factorial(n));
	}

	public int factorial(int n) {
		if(n == 0) {
			return 1;
		}
		else {
			return n*factorial(n-1);
		}
	}
}