package capture_1_stackandqueue;

import java.util.Stack;

public class ReverseStack_main {
	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<Integer>();
		//入栈 1 2 3 4 5
		stack.push(1);
		stack.push(2);
		stack.push(3);
		stack.push(4);
		stack.push(5);
		
		//翻转栈，使得出栈1 2 3 4 5
		ReverseStack.reverse(stack);  
		
		while (!stack.isEmpty()) {
			System.out.println(stack.pop());
		}
	}
}
