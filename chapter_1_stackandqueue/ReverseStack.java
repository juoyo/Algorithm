package capture_1_stackandqueue;

import java.util.Stack;

public class ReverseStack {
	Stack<Integer> stack = new Stack<Integer>();
	//·µ»ØÕ»µ×ÔªËØ²¢´ÓÕ»ÖĞÉ¾³ı
	public static int GetAndRemoveLastElement(Stack<Integer> stack) {
		int result = stack.pop();
		if(stack.isEmpty()) {
			return result;
		} else {
			int last = GetAndRemoveLastElement(stack);
			stack.push(result);
			return last;
		}
	}
	
	//ÄæĞòÕ»
	public static void reverse(Stack<Integer> stack) {
		if (stack.isEmpty()) {
			return ;
		} 
		int i = GetAndRemoveLastElement(stack);
		reverse(stack);
		stack.push(i);
	}
}
