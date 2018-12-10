package capture_1_stackandqueue;

public class HanoiStack_main {
	public static void main(String[] args) {
		int num = 4;

		// solution 1
		HanoiStack hanoistack = new HanoiStack();
		int steps1 = hanoistack.hanoiProblem1(num, "left", "mid", "right");
		System.out.println("It will move " + steps1 + " steps.");
		System.out.println("===================================");
	}
}
