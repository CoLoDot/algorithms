package algorithms

import (
	"fmt"
)

// Fibonacci example
func Fibonacci(size int) []int {
	result := []int{0, 1}
	for i := 1; i < size-1; i++ {
		result = append(result, result[i-1]+result[i])
	}
	fmt.Printf("%v", result)
	return result
}

func memoRecurFib(n int) int {
	if n < 2 {
		return n
	}
	return memoRecurFib(n-1) + memoRecurFib(n-2)
}

// RecursiveFibonacci example
func RecursiveFibonacci(max int) []int {
	result := []int{}
	for i := 0; i < max; i++ {
		result = append(result, memoRecurFib(i))
	}
	fmt.Printf("%v", result)
	return result
}
